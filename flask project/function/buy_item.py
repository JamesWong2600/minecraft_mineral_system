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
from bs4 import BeautifulSoup
from flask import Markup
import jinja2
import yaml
with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    ip = cfg['SQLip']
    port = cfg['SQLport']
    database= cfg['database']  
def buy_item():    
    i = 0 
    e = 0
    p = 0
    g = 0
    total = 0
    mtotal = 0
    soldtotal=0
    index=0
    fndex=0
    connection = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    moneymydb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    usermydb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    serverdb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    fdb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    moneymycursor = moneymydb.cursor()
    mycursor = connection.cursor()
    usermycursor = usermydb.cursor()
    servercursor = serverdb.cursor()
    fcursor = fdb.cursor()
    username = str(request.form['user'])
    password = str(request.form['pass'])
    print(username)
    print(password)
    minerallist = ["iron", "coal", "diamond", "copper", "redstone", "gold", "emerald"]
    amountlist = ["amount0","amount1", "amount2", "amount3", "amount4", "amount5", "amount6"]
    userminerallist = ["iron", "coal", "diamond", "copper", "redstone", "gold", "emerald"]  
    current = [0] * 7      
    while index < 7: 
        try:
            sql= f"UPDATE usermineral SET {minerallist[index]} = {minerallist[index]} + {request.form[amountlist[index]]} WHERE username = '{username}'"
            sql2= f"UPDATE mineral SET {minerallist[index]} = {minerallist[index]} + {request.form[amountlist[index]]} WHERE id = '0'"
            index = index + 1  
            mycursor.execute(sql)  
            fcursor.execute(sql2)  
            connection.commit()
            fdb.commit()
        except mysql.connector.Error as g:
            print('Error')       
    for x in userminerallist:
        usermycursor.execute(f"SELECT {x} FROM usermineral WHERE username = '{username}'")
        userminerallist[e] = usermycursor.fetchall()
        userminerallist[e] = str(userminerallist[e])    
        userminerallist[e] = userminerallist[e].replace('[(', '')
        userminerallist[e] = userminerallist[e].replace(',)]', '')
        userminerallist[e] = int(userminerallist[e])    
        print(userminerallist[e]) 
        mtotal = mtotal + userminerallist[e]
        e = e + 1  
    for x in minerallist:
        servercursor.execute(f"SELECT {x} FROM mineral WHERE id ='0'")
        minerallist[i] = servercursor.fetchall()
        minerallist[i] = str(minerallist[i])    
        minerallist[i] = minerallist[i].replace('[(', '')
        minerallist[i] = minerallist[i].replace(',)]', '')
        minerallist[i] = int(minerallist[i])    
        total = total + minerallist[i]
        i = i + 1        
    if userminerallist[0] == 0:
        current[0] = 50 
    else:
        current[0]=round(50*(1-(userminerallist[0]/total)),2)
    if userminerallist[1] == 0:
        current[1] = 10 
    else:
        current[1]=round(10*(1-(userminerallist[1]/total)),2)
    if userminerallist[2] == 0:
        current[2] = 500 
    else:      
        current[2]=round(500*(1-(userminerallist[2]/total)),2)
    if userminerallist[3] == 0:
        current[3] = 40 
    else:      
        current[3]=round(40*(1-(userminerallist[3]/total)),2)
    if userminerallist[4] == 0:
        current[4] = 60 
    else:      
        current[4]=round(60*(1-(userminerallist[4]/total)),2)
    if userminerallist[5] == 0:
        current[5] = 200 
    else:      
        current[5]=round(200*(1-(userminerallist[5]/total)),2)
    if userminerallist[6] == 0:
        current[6] = 600 
    else:      
        current[6]=round(600*(1-(userminerallist[6]/total)),2)  
    while g < 7:
        nef = request.form[amountlist[g]]
        nef = nef.replace('[(', '')
        nef = nef.replace(',)]', '')
        nef = int(nef)    
        soldtotal = soldtotal + nef*current[g]
        print("sd")
        print(soldtotal)
        g=g+1
    sql2= f"UPDATE usermineral SET money = money - {soldtotal} WHERE username = '{username}'"
    mycursor.execute(sql2)  
    connection.commit()        
    moneymycursor.execute(f"SELECT money FROM usermineral WHERE username ='{username}'")  
    money = moneymycursor.fetchall()
    money = str(money)    
    money = money.replace("[('", '')
    money = money.replace("',)]", '')  
    money = round(float(money),2)
    moneymycursor.close()
    mycursor.close()
    usermycursor.close()
    servercursor.close()
    fcursor.close()
    connection.close()
    moneymydb.close()
    usermydb.close()
    serverdb.close()
    fdb.close()
    mineraltotal = round(current[0]*userminerallist[0]+current[1]*userminerallist[1]+current[2]*userminerallist[2]+current[3]*userminerallist[3]+current[4]*userminerallist[4]+current[5]*userminerallist[5]+current[6]*userminerallist[6],2)        
    return username,password,userminerallist[0],userminerallist[1],userminerallist[2],userminerallist[3],userminerallist[4],userminerallist[5],userminerallist[6],mineraltotal,money