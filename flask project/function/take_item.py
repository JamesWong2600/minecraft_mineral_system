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
import random
import yaml
with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    ip = cfg['SQLip']
    port = cfg['SQLport']
    database= cfg['database']
def take_item():
    e = 0
    q = 0
    index=0
    token = random.randint(122233,875565)
    connection = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    usermydb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    serverdb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    serverdb2 = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    mycursor = connection.cursor()
    mycursor2 = usermydb.cursor()
    mycursor3 = serverdb.cursor()
    mycursor4 = serverdb2.cursor()
    username = str(request.form['user'])
    password = str(request.form['pass'])
    print(username)
    print(password)
    minerallist = ["iron", "coal", "diamond", "copper", "redstone", "gold", "emerald"]
    amountlist = ["amount0","amount1", "amount2", "amount3", "amount4", "amount5", "amount6"]
    userminerallist = ["iron", "coal", "diamond", "copper", "redstone", "gold", "emerald"]  
    current = [0] * 7     
    for x in userminerallist:
        mycursor.execute(f"SELECT {x} FROM usermineral WHERE username = '{username}'")
        userminerallist[e] = mycursor.fetchall()
        userminerallist[e] = str(userminerallist[e])    
        userminerallist[e] = userminerallist[e].replace('[(', '')
        userminerallist[e] = userminerallist[e].replace(',)]', '')
        userminerallist[e] = int(userminerallist[e])    
        e = e+1
    mycursor3.execute(f"SELECT UUID FROM usermineral WHERE username = '{username}'")  
    ID = mycursor3.fetchall()
    uID = str(ID)
    print(uID)
    uID = uID.replace("[('", "")
    uID = uID.replace("',)]", "")
    for x in minerallist:
        sql2= f"UPDATE usermineral SET {x} = {x} - {request.form[amountlist[q]]} WHERE username = '{username}'"
        mycursor2.execute(sql2)  
        usermydb.commit()
        q = q+1
    sql1= "INSERT INTO takemineral (id, UUID, token, iron, coal, diamond, copper, redstone, gold, emerald) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    params = [username,uID,token,request.form[amountlist[0]],request.form[amountlist[1]],request.form[amountlist[2]],request.form[amountlist[3]], request.form[amountlist[4]],request.form[amountlist[5]],request.form[amountlist[6]]]
    mycursor4.executemany(sql1,[params])  
    serverdb2.commit()
    mycursor.close
    mycursor2.close
    mycursor3.close
    mycursor4.close
    connection.close
    usermydb.close
    serverdb.close
    serverdb2.close

    return token