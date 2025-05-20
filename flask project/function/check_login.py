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
def check_login():
    status = 0
    mydb = mysql.connector.connect(host=ip, port = port, user="root2", password="20050118",database=database)
    username = str(request.form['username'])
    password = str(request.form['password'])
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT iron FROM usermineral WHERE username ='{username}' and password='{password}'")
    value = mycursor.fetchall()
    strvalue = str(value)
    print(value)
    mydb.close
    mycursor.close
    if strvalue == "[]":
      return status
    else:  
      status = 1
      return status

    #if status == 1:
    #  print(status)
     # return status
    

