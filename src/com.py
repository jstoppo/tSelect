import os
import sys
import mysql.connector
import json




class mysqldb(object):
    def __init__(self):
        self.help = "This class is a wrapper for mysql access"

    def connect(self,host, user, password, dbname):

        print(host,user,password,dbname)

        try:
            
            con = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )
            return con

        except Exception as e:
            if con is not None:
                con.close()

            pass

    def insert(self,sql,val,con):
        mycursor = con.cursor()
        

        #sql = "INSERT INTO n50rics (symbol,name) VALUES (%s,%s)"
        #val = (sym,name)
        mycursor.execute(sql, val)

        con.commit()

        print(mycursor.rowcount, "record inserted.")

    
    
    def createtable(self,tablestatement,con):
        mycursor = con.cursor()
        

        #sql = "INSERT INTO n50rics (symbol,name) VALUES (%s,%s)"
        #val = (sym,name)
        mycursor.execute(tablestatement)
#        mycursor.execute(sql, val)

        con.commit()

        print(mycursor.rowcount, "table created")
        return True


    
    
    def query(self,tablestatement,val,con):
        mycursor = con.cursor()
        
        mycursor.execute(tablestatement,val)
        #result = mycursor.fetchall()
        #return result

        row_headers=[x[0] for x in mycursor.description] #this will extract row headers
        rv = mycursor.fetchall()
        json_data=[]
        for result in rv:
                json_data.append(dict(zip(row_headers,result)))
        return json_data


    def executeqry(self,tablestatement,val,con):
        mycursor = con.cursor()
        

        #sql = "INSERT INTO n50rics (symbol,name) VALUES (%s,%s)"
        #val = (sym,name)
        mycursor.execute(tablestatement,val)
#        mycursor.execute(sql, val)

        con.commit()

        print(mycursor.rowcount, "table created")
        return True


    
            
            
                    

            

            
