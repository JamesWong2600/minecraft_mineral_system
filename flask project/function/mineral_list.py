from flask import Flask, render_template, redirect, url_for, request
from flask_socketio import SocketIO
import mysql.connector
from win32gui import GetWindowText, GetForegroundWindow
from threading import Lock
import os.path
import random
import re
import sys
from flask_socketio import emit
from importlib import import_module
import yaml
with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    ip = cfg['SQLip']
    port = cfg['SQLport']
    database= cfg['database']
def mineral_for_server():
    f = 0
    total = 0
    mydb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)  
    minerallist = ["iron", "coal", "diamond", "copper", "redstone", "gold", "emerald"]  
    mycursor = mydb.cursor()
    for x in minerallist:
        mycursor.execute(f"SELECT {x} FROM mineral WHERE id ='0'")
        minerallist[f] = mycursor.fetchall()
        minerallist[f] = str(minerallist[f])    
        minerallist[f] = minerallist[f].replace('[(', '')
        minerallist[f] = minerallist[f].replace(',)]', '')
        minerallist[f] = int(minerallist[f])    
        total = total + minerallist[f]
        f = f + 1  
    if minerallist[0] == 0:
        current1 = 50 
    else:
        current1=round(50*(1-(minerallist[0]/total)),2)
    if minerallist[1] == 0:
        current2 = 10 
    else:
        current2=round(10*(1-(minerallist[1])/total),2)
    if minerallist[2] == 0:
        current3 = 500 
    else:      
        current3=round(500*(1-(minerallist[2]/total)),2)
    if minerallist[3] == 0:
        current4 = 40 
    else:      
        current4=round(40*(1-(minerallist[3]/total)),2)
    if minerallist[4] == 0:
        current5 = 60   
    else:      
        current5=round(60*(1-(minerallist[4]/total)),2)
    if minerallist[5] == 0:
        current6 = 200 
    else:      
        current6=round(200*(1-(minerallist[5]/total)),2)
    if minerallist[6] == 0:
        current7 = 600 
    else:      
        current7=round(600*(1-(minerallist[6]/total)),2) 
    mydb.close
    mycursor.close
    return minerallist[0], minerallist[1] ,minerallist[2] ,minerallist[3] ,minerallist[4] ,minerallist[5], minerallist[6],current1,current2,current3,current4,current5,current6,current7
    #return render_template("index.html",variable=minerallist[0],variable2=minerallist[1],variable3=minerallist[2],variable4=minerallist[3],
    #variable5=minerallist[4],variable6=minerallist[5],variable7=minerallist[6],current1=current1,current2=current2,current3=current3
    #,current4=current4,current5=current5,current6=current6,current7=current7,errormsg="invaid")   
         
    