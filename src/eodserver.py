
import falcon
#from falcon_cors import CORS


import os
import sys
#import zipfile
import time
from com import mysqldb
#from time import time, strftime
import pandas as pd
#import logging
import json


import talib as ta

mdb = mysqldb()

#logging.basicConfig(level=logging.INFO)

host="localhost"
user="john"
password="password"
dbname="tradedb"



class CORSComponent:

    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('Access-Control-Allow-Origin', '*')

        if (req_succeeded
            and req.method == 'OPTIONS'
            and req.get_header('Access-Control-Request-Method')
        ):
            # NOTE: This is a CORS preflight request. Patch the
            #   response accordingly.

            allow = resp.get_header('Allow')
            resp.delete_header('Allow')

            allow_headers = req.get_header(
                'Access-Control-Request-Headers',
                default='*'
            )

            resp.set_headers((
                ('Access-Control-Allow-Methods', allow),
                ('Access-Control-Allow-Headers', allow_headers),
                ('Access-Control-Max-Age', '86400'),  # 24 hours
            ))


class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote



class n50bc:
    def on_get(self, req, resp):

        t = pd.Timestamp.now()
        dt = time.strftime('%d%m%y', time.localtime())
        if(t.hour < 20):
            dt = time.strftime('%d%m%y', time.localtime(time.time() - 86400))


        con = mdb.connect(host, user, password, dbname)
        #dt = "170920"
        qry = "SELECT * FROM N"+dt+" where EQ_BENCHMARK=\"NIFTY_50\""
        print(qry)
        val = ""
        result = mdb.query(qry,val,con)
        #print(result)     
        dt1 = time.strftime('%d-%m-%Y', time.localtime(time.time() - 86400))
        resp.media = result,dt1

class n50nextbc:
    def on_get(self, req, resp):
        t = pd.Timestamp.now()
        dt = time.strftime('%d%m%y', time.localtime())
        if(t.hour < 20):
            dt = time.strftime('%d%m%y', time.localtime(time.time() - 86400))


        con = mdb.connect(host, user, password, dbname)
        #dt = "170920"
        qry = "SELECT * FROM N"+dt+" where EQ_BENCHMARK=\"NIFTY_NEXT_50\""
        print(qry)
        val = ""
        result = mdb.query(qry,val,con)
#        print(result)
        dt1 = time.strftime('%d-%m-%Y', time.localtime(time.time() - 86400))
        resp.media = result,dt1


class candlestick:
    def on_post(self, req, resp):
        print("aa")
        print(req)
        print(req.query_string)
        

        # t = pd.Timestamp.now()
        # dt = time.strftime('%d%m%y', time.localtime())
        # if(t.hour < 20):
        #     dt = time.strftime('%d%m%y', time.localtime(time.time() - 86400))

        # con = mdb.connect(host, user, password, dbname)
        # #dt = "170920"
        # qry = "SELECT SYMBOL, OPEN_PRICE,HIGH_PRICE, LOW_PRICE, CLOSE_PRICE FROM N"+dt+" where EQ_BENCHMARK=\"Compulsory_R_S\""
        # print(qry)
        # val = ""
        # result = mdb.query(qry,val,con)
        # #df = pd.DataFrame(result,columns=('SYMBOL','OPEN_PRICE','HIGH_PRICE','LOW_PRICE','CLOSE_PRICE'))
        # df = pd.DataFrame(result)
        # df.set_index(['SYMBOL'], inplace = False) 
        # print(df)

        # #print(result)
        # r = ta.CDLMARUBOZU(df['OPEN_PRICE'],df['HIGH_PRICE'],df['LOW_PRICE'],df['CLOSE_PRICE'])
        # print(r[r != 0])
        # dt1 = time.strftime('%d-%m-%Y', time.localtime(time.time() - 86400))
        
        resp.media = req



app = falcon.API(middleware=[CORSComponent()])
app.add_route('/n50bc', n50bc())
app.add_route('/candlestick', candlestick())
app.add_route('/n50nextbc', n50nextbc())