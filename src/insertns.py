import os
import sys
import pandas as pd
import mysql.connector
from com import mysqldb
import logging

mdb = mysqldb()

#logging.basicConfig(level=logging.INFO)

host="localhost"
user="john"
password="password"
dbname="tradedb"



#logging.info("connected to - " +str(mydb))
#logging.info(mydb)


usage_str = "<symbol file>"




def write_db(symfl):
    #df = pd.read_csv(fl)
    
    table_sql = "CREATE TABLE if not exists symboltable(id int AUTO_INCREMENT PRIMARY KEY,n50_symbol varchar(100),ns_symbol varchar (100),EQ_BENCHMARK varchar(100))"
    
    #val = (sym,name)
    try:
        con = mdb.connect(host,user,password,dbname)
        print("Connection successful!")
    except Exception as e:
        print("Not able to connect to database!"+e)

    try:
        create_table = mdb.createtable(table_sql,con)
        print("Table created!")
    except Exception as e:
        print("Exception occurred"+e)

    try:

        
        print("Reading csv")
        f1 = symfl
        print(f1)
        df = pd.read_csv(f1,error_bad_lines=False,nrows=101)
        df.columns = ["n50_symbol","ns_symbol","EQ_BENCHMARK"]
        print(df)
        #sym,name = symfl.split(",")
        print("Inserting symbols..")
        #symfh = open(symfl,"r")
        for i,row in df.iterrows():
            print(row['n50_symbol'],row['ns_symbol'],row['EQ_BENCHMARK'])
            insert_sql = "INSERT INTO symboltable (n50_symbol,ns_symbol,EQ_BENCHMARK) VALUES (%s,%s,%s)"
            val = row['n50_symbol'],row['ns_symbol'],row['EQ_BENCHMARK']
            execute = mdb.executeqry(insert_sql, val,con)
            print(execute)
            print("Symbols Inserted")
       
        
        print("data inserted")

    except Exception as e:
        print(e)

def main(argv):
    if(len(argv)!=2):
      sys.stderr.write(usage_str)
      sys.exit(1)
      
    symfl = argv[1]  
    
    print("Create NS Symbols Database")
    insert_db = write_db(symfl)
    #print("Inserted successfully!")




    



if __name__ ==  '__main__':
	#print(sys.argv[1:])
    main(sys.argv)
	


