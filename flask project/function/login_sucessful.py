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
import jinja2
import yaml
with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    ip = cfg['SQLip']
    port = cfg['SQLport']
    database= cfg['database']
def login_sucessful():
    i = 0
    e = 0
    total = 0
    mtotal = 0
    status = 0
    mydb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    moneymydb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    minerallist = ["iron", "coal", "diamond", "copper", "redstone", "gold", "emerald"]  
    username = str(request.form['username'])
    password = str(request.form['password'])
    print(username,password)
    limitusername = username
    mycursor = mydb.cursor()
    moneymycursor = moneymydb.cursor()
    for x in minerallist:
      mycursor.execute(f"SELECT {x} FROM usermineral WHERE username ='{username}' and password='{password}'")
      minerallist[i] = mycursor.fetchall()
      minerallist[i] = str(minerallist[i])    
      minerallist[i] = minerallist[i].replace('[(', '')
      minerallist[i] = minerallist[i].replace(',)]', '')
      minerallist[i] = int(minerallist[i])    
      total = total + minerallist[i]
      i = i + 1        
    moneymycursor.execute(f"SELECT money FROM usermineral WHERE username ='{username}'")  
    money = moneymycursor.fetchall()
    money = str(money)    
    print(money)
    money = money.replace("[('", '')
    money = money.replace("',)]", '')  
    money = round(float(money),2)
    money = str(money) 
    if minerallist[0] == 0:
      current1 = 50 
    else:
      current1=round(50*(1-(minerallist[0]/total)),2)
    if minerallist[1] == 0:
      current2 = 10 
    else:
      current2=round(10*(1-(minerallist[1]/total)),2)
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
    moneymydb.close
    mycursor.close
    moneymycursor.close
    mineraltotal = round(current1*minerallist[0]+current2*minerallist[1]+current3*minerallist[2]+current4*minerallist[3]+current5*minerallist[4]+current6*minerallist[5]+current7*minerallist[6],2)  
    return limitusername,password,minerallist[0],minerallist[1],minerallist[2],minerallist[3],minerallist[4],minerallist[5],minerallist[6],mineraltotal,money
