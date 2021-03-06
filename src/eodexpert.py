
import os
import sys
import zipfile
import time
from com import mysqldb
#from time import time, strftime
import pandas as pd
import logging

mdb = mysqldb()

logging.basicConfig(level=logging.INFO)

host="localhost"
user="john"
password="password"
dbname="tradedb"

def get_bhavcopy_data(dt):
    logging.info("getting data - bhavcopy")
    
    #dt = "210920" 
    #return dt
    fl = "PR"+dt+".zip"
    fl1 = "../data/bhavcopydata/PR"+dt+".zip"
    os.system("curl -o "+fl1+" https://archives.nseindia.com/archives/equities/bhavcopy/pr/"+fl+"")
    time.sleep(2)
    with zipfile.ZipFile(fl1,"r") as zip_ref:
        zip_ref.extractall("../data/bhavcopydata/PR"+dt)
    
    logging.info("bhavcopy downloaded and unzipped at " +fl1)
    
    return dt

	
def benchmark_defn(dt):
    logging.info("writting into db")
    logging.info("cleanup bhavcopy data")
    fl = "../data/bhavcopydata/PR"+dt+"/Pd"+dt+".csv"
    print(fl)
    df_n = pd.read_csv(fl,error_bad_lines=False,skiprows=(60), nrows=50)
    bench_value = "NIFTY_50"
    data_insert = write_db(dt,df_n,bench_value) 

    df_n = pd.read_csv(fl,error_bad_lines=False,skiprows=(112), nrows=50)
    bench_value = "NIFTY_Next_50"
    data_insert = write_db(dt,df_n,bench_value) 
	
    df_n = pd.read_csv(fl,error_bad_lines=False,skiprows=(164), nrows=1429)
    bench_value = "Compulsory_R_S"
    data_insert = write_db(dt,df_n,bench_value) 	

	

def write_db(dt,df,bench_value):
    
    #print(df.info)
    df.columns=["MKT","SERIES","SYMBOL","SECURITY","PREV_CL_PR","OPEN_PRICE","HIGH_PRICE","LOW_PRICE","CLOSE_PRICE","NET_TRDVAL","NET_TRDQTY","IND_SEC","CORP_IND","TRADES","HI_52_WK","LO_52_WK"]
    
    table_sql = "CREATE TABLE if not exists ""N" + dt + " (SYMBOL VARCHAR(255),SECURITY VARCHAR(255), PREV_CL_PR FLOAT, OPEN_PRICE FLOAT, HIGH_PRICE FLOAT, LOW_PRICE FLOAT, CLOSE_PRICE FLOAT, NET_TRDVAL DOUBLE,NET_TRDQTY DOUBLE, HI_52_WK FLOAT, LO_52_WK FLOAT, EQ_BENCHMARK VARCHAR(255))"
    #print(table_sql)
    con = mdb.connect(host, user, password, dbname)
    
    #print(con)
    create_table = mdb.createtable(table_sql,con)
    print(create_table)
    print(df)
    for i,row in df.iterrows():
        print(row['CLOSE_PRICE'], row['SYMBOL'])
        insert_qry = "insert into ""N" +dt+ " (SYMBOL,SECURITY,PREV_CL_PR,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,NET_TRDVAL,NET_TRDQTY,HI_52_WK,LO_52_WK,EQ_BENCHMARK) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (row['SYMBOL'],row['SECURITY'],row['PREV_CL_PR'],row['OPEN_PRICE'],row['HIGH_PRICE'],row['LOW_PRICE'],row['CLOSE_PRICE'],row['NET_TRDVAL'],row['NET_TRDQTY'],row['HI_52_WK'],row['LO_52_WK'],bench_value)
        print(insert_qry)
        execute = mdb.executeqry(insert_qry, val,con)
        print(execute)


    #exit()
    #bc = open(fl,"r")


    con.close()

def main():
    
    logging.info("get eod data - bhavcopy")
    #dt = time()
    #t = strftime("%y", time())
    dt = time.strftime('%d%m%y', time.localtime())
    print(dt)
    #dt = "220920"
    #dt = time.strftime('%d%m%y', time.localtime())
    print("*************************"+dt+"******************************")

    #exit()

    bc_date = get_bhavcopy_data(dt)
    logging.info("bhavcopy downloaded for the date - " +bc_date)
    logging.info("insert bhavcopy in db")
    benchmark_defn(bc_date)



if __name__ ==  '__main__':
	#print(sys.argv[1:])
	main()
