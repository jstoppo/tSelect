
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
        """Handles GET requests"""

        con = mdb.connect(host, user, password, dbname)
        qry = "select * from N110920"
        val = ""
        result = mdb.query(qry,val,con)

        print(result)
        
   
        resp.media = result



app = falcon.API(middleware=[CORSComponent()])
app.add_route('/n50bc', n50bc())