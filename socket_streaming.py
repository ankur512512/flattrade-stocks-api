import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import flattrade_get_api_token
import logging
import time
import pandas as pd

#sample
logging.basicConfig(level=logging.DEBUG)

#flag to tell us if the websocket is open
socket_opened = False

#application callbacks
def event_handler_order_update(message):
    print("order event: " + str(message))


SYMBOLDICT = {}
def event_handler_quote_update(message):
    global SYMBOLDICT
    #e   Exchange
    #tk  Token
    #lp  LTP
    #pc  Percentage change
    #v   volume
    #o   Open price
    #h   High price
    #l   Low price
    #c   Close price
    #ap  Average trade price

    print("quote event: {0}".format(time.strftime('%d-%m-%Y %H:%M:%S')) + str(message))
    
    key = message['e'] + '|' + message['tk']

    if key in SYMBOLDICT:
        symbol_info =  SYMBOLDICT[key]
        symbol_info.update(message)
        SYMBOLDICT[key] = symbol_info
    else:
        SYMBOLDICT[key] = message

    print(SYMBOLDICT[key])

def open_callback():
    global socket_opened
    socket_opened = True
    print('app is connected')
    
    api.subscribe('NSE|26000', feed_type='d')
    #api.subscribe(['NSE|22', 'BSE|522032'])

#end of callbacks

def get_time(time_string):
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')

    return time.mktime(data)

#start of our program
api = NorenApiPy()

 
# Got the token from file flattrade_get_api_token.py
usersession=flattrade_get_api_token.token #'175e667c2ed78d9695aaf6c5751db6a41b56ebb674d5bd71b24c3300a1917ad8'
userid = flattrade_get_api_token.USER

print(f'Token is: {usersession}')

ret = api.set_session(userid= userid, password = '', usertoken= usersession)

if ret != None:   
    ret = api.start_websocket(order_update_callback=event_handler_order_update, subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback)
    
    while True:
        if socket_opened == True:
            print('q => quit')
            prompt1=input('what shall we do? ').lower()    

            print('Fin') #an answer that wouldn't be yes or no
            break   

        else:
            continue
