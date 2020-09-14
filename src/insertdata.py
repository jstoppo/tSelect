import os
import sys
import zipfile
import time
import pandas as pd
import logging
import mysql.connector

logging.basicConfig(level=logging.INFO)

mydb = mysql.connector.connect(
  host="localhost",
  user="john",
  password="password",
  database="tradedb"
)

logging.info("connected to - " +str(mydb))
#logging.info(mydb)


usage_str = "<symbol file>"



def write_data(records):
    sym,name = records.split(",")
    #print(name)
    #exit()

    mycursor = mydb.cursor()

    sql = "INSERT INTO n50rics (symbol,name) VALUES (%s,%s)"
    val = (sym,name)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")




def main(argv):

    if(len(argv)!=2):
	    sys.stderr.write(usage_str)
	    sys.exit(1)

    symfl = argv[1]
    print(symfl)
    symfh = open(symfl,"r")
    for i in symfh:
        #print(i)
        write_data(i)


    
    
    
    
    mydb.close()



if __name__ ==  '__main__':
	#print(sys.argv[1:])
	main(sys.argv)


