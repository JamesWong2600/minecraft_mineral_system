from flask import Flask, render_template, redirect, url_for, request
import mysql.connector
from win32gui import GetWindowText, GetForegroundWindow
import os.path
from importlib import import_module
from bs4 import BeautifulSoup
import psutil
import time
import pynvml
from s_tui.sources.rapl_power_source import RaplPowerSource
import yaml

app = Flask(__name__)

STATIC_DIR = os.path.abspath('static\css\style.css')
STATIC_DIR = os.path.abspath('static\ironignot.png')


with open("config.yaml") as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
    ip = cfg['SQLip']
    port = cfg['SQLport']
    host = cfg['hostip']
    hostport = cfg['hostport']
    database= cfg['database']
    
a = 0
k = 0
cpu = 0
usernamevalue = {}
passwordvalue = {}
poverty1value = {}
poverty2value = {}
poverty3value = {}
poverty4value = {}
poverty5value = {}
poverty6value = {}
poverty7value = {}
totalvaluevalue = {}
moneyvalue = {}
c1value = {}
c2value = {}
c3value = {}
c4value = {}
c5value = {}
c6value = {}
c7value = {}

@app.route('/')
def index():
    i = 0
    total = 0
    tx = ", min=0.0"
    my_str = str(psutil.cpu_freq())
    my_str = my_str.split(tx,2)[0]
    intfeq = str(my_str.replace('scpufreq(current=',''))
    strfeq = str(intfeq)+"Mhz"
    cpu = str(psutil.cpu_percent())
    ramper = psutil.virtual_memory()[2]
    ram = str(round(psutil.virtual_memory()[3]/1000000000,2))+' GB'
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    powerusage = str(round(int(pynvml.nvmlDeviceGetPowerUsage(handle) / 1000),2))
    source = RaplPowerSource()
    source.update()
    summary = dict(source.get_sensors_summary())
    cpu_power_total = str(sum(list(map(float, [summary[key] for key in summary.keys() if key.startswith('package')]))))
    print(cpu_power_total)
    power = f'{powerusage}W'
    mydb = mysql.connector.connect(host=ip, port=port, user="root2", password="20050118",database=database)
    minerallist = ["iron", "coal", "diamond", "copper", "redstone", "gold", "emerald"]   
    mycursor = mydb.cursor()
    for x in minerallist:
      mycursor.execute(f"SELECT {x} FROM mineral WHERE id ='0'")
      minerallist[i] = mycursor.fetchall()
      minerallist[i] = str(minerallist[i])    
      minerallist[i] = minerallist[i].replace('[(', '')
      minerallist[i] = minerallist[i].replace(',)]', '')
      minerallist[i] = int(minerallist[i])    
      total = total + minerallist[i]
      i = i + 1  
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
    mycursor.close
    return render_template("index.html",variable=minerallist[0],variable2=minerallist[1],variable3=minerallist[2],variable4=minerallist[3],
    variable5=minerallist[4],variable6=minerallist[5],variable7=minerallist[6],current1=current1,current2=current2,current3=current3
    ,current4=current4,current5=current5,current6=current6,current7=current7,cpu=cpu,ram=ram,ramper=ramper,feq=strfeq,intfeq=intfeq,powerusage=power
    ,power=powerusage)
    
 

@app.route('/loginpage', methods=['GET', 'POST'])
def loginpage():
    return render_template("loginpage.html",) 

@app.route('/poverty', methods=['GET', 'POST'])
def povety():
    from function.mineral_list import mineral_for_server
    from function.check_login import check_login
    from function.login_sucessful import login_sucessful
    username,password,poverty1,poverty2,poverty3,poverty4,poverty5,poverty6,poverty7,totalvalue,money = login_sucessful()
    va1, va2, va3, va4, va5, va6, va7, c1, c2, c3, c4, c5, c6,c7 = mineral_for_server()
    return render_template("playerpovety.html", poverty1=poverty1,poverty2=poverty2,poverty3=poverty3,poverty4=poverty4,
    poverty5=poverty5,poverty6=poverty6,poverty7=poverty7,totalvalue=totalvalue,money=money,username=usernamevalue['username'],password=passwordvalue['username'],
    current1=c1,current2=c2,current3=c3
    ,current4=c4,current5=c5,current6=c6,current7=c7) 

@app.route('/currenthardware', methods=['GET', 'POST'])
def currenthardware():
    tx = ", min=0.0"
    my_str = str(psutil.cpu_freq())
    my_str = my_str.split(tx,2)[0]
    intfeq = str(my_str.replace('scpufreq(current=',''))
    strfeq = str(intfeq)+"Mhz"
    cpu = str(psutil.cpu_percent())
    ramper = psutil.virtual_memory()[2]
    ram = str(round(psutil.virtual_memory()[3]/1000000000,2))+' GB'
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    powerusage = str(round(int(pynvml.nvmlDeviceGetPowerUsage(handle) / 1000),2))
    source = RaplPowerSource()
    source.update()
    summary = dict(source.get_sensors_summary())
    cpu_power_total = str(sum(list(map(float, [summary[key] for key in summary.keys() if key.startswith('package')]))))
    print(cpu_power_total)
    power = f'{powerusage}W'
    return render_template("hardwaremonitor.html", money=money,username=usernamevalue['username'],password =passwordvalue['username']
   ,cpu=cpu,ram=ram,ramper=ramper,feq=strfeq,intfeq=intfeq,powerusage=power
  ,power=powerusage)
        
@app.route('/playerpovety', methods=['GET', 'POST'])
def playerpovety():
    from function.mineral_list import mineral_for_server
    from function.check_login import check_login
    from function.login_sucessful import login_sucessful
    status = check_login()
    if status == 1:
      username,password,poverty1,poverty2,poverty3,poverty4,poverty5,poverty6,poverty7,totalvalue,money = login_sucessful()
      va1, va2, va3, va4, va5, va6, va7, c1, c2, c3, c4, c5, c6,c7 = mineral_for_server()
      usernamevalue['username'] = username
      passwordvalue['username'] = password
      poverty1value['username'] = poverty1
      poverty2value['username'] = poverty2
      poverty3value['username'] = poverty3
      poverty4value['username'] = poverty4
      poverty5value['username'] = poverty5
      poverty6value['username'] = poverty6
      poverty7value['username'] = poverty7
      totalvaluevalue['username'] = totalvalue
      moneyvalue['username'] = money
      c1value['username'] = c1
      c2value['username'] = c2
      c3value['username'] = c3
      c4value['username'] = c4
      c5value['username'] = c5
      c6value['username'] = c6
      c7value['username'] = c7
      return render_template("playerpovety.html", poverty1=poverty1,poverty2=poverty2,poverty3=poverty3,poverty4=poverty4,
      poverty5=poverty5,poverty6=poverty6,poverty7=poverty7,totalvalue=totalvalue,money=money,username=usernamevalue['username'],password=passwordvalue['username'],
      current1=c1,current2=c2,current3=c3
      ,current4=c4,current5=c5,current6=c6,current7=c7) 
    else: 
      va1, va2, va3, va4, va5, va6, va7, c1, c2, c3, c4, c5, c6,c7 = mineral_for_server()
      return render_template("index.html",variable=va1,variable2=va2,variable3=va3,variable4=va4,
            variable5=va5,variable6=va6,variable7=va7,errormsg="invaid",
            current1=c1,current2=c2,current3=c3
                  ,current4=c4,current5=c5,current6=c6,current7=c7) 
    
@app.route('/logined_playerpovety', methods=['GET', 'POST'])
def logined_playerpovety():
    return render_template("playerpovety.html", poverty1=poverty1value['username'],poverty2=poverty2value['username'],poverty3=poverty3value['username'],poverty4=poverty4value['username'],
    poverty5=poverty5value['username'],poverty6=poverty6value['username'],poverty7=poverty7value['username'],totalvalue=totalvaluevalue['username'],money=moneyvalue['username'],username=usernamevalue['username'],password=passwordvalue['username'],
    current1=c1value['username'],current2=c2value['username'],current3=c3value['username']
    ,current4=c4value['username'],current5=c5value['username'],current6=c6value['username'],current7=c7value['username'])   
    
@app.route('/shop', methods=['GET', 'POST'])
def shop():
    return render_template("shop.html")    

@app.route('/playerpovetypage', methods=['GET', 'POST'])
def playerpovetypage():
    from function.mineral_list import mineral_for_server
    from function.buy_item import buy_item   
    username,password,poverty, poverty2, poverty3,poverty4,poverty5,poverty6,poverty7,totalvalue,money = buy_item()
    va1, va2, va3, va4, va5, va6, va7, c1, c2, c3, c4, c5, c6,c7 = mineral_for_server()
    return render_template("playerpovety.html", username=username,password=password,poverty1=poverty,poverty2=poverty2,poverty3=poverty3,poverty4=poverty4,
    poverty5=poverty5,poverty6=poverty6,poverty7=poverty7,totalvalue=totalvalue,money=money,current1=c1,current2=c2,current3=c3
    ,current4=c4,current5=c5,current6=c6,current7=c7)  
      
 
@app.route("/money", methods=['GET', 'POST'])
def money():
    from function.mineral_list import mineral_for_server
    if 'sell' in request.form:
      from function.sell_item import sell_item   
      username,password,poverty, poverty2, poverty3,poverty4,poverty5,poverty6,poverty7,totalvalue,money = sell_item()
      va1, va2, va3, va4, va5, va6, va7, c1, c2, c3, c4, c5, c6,c7 = mineral_for_server()
      return render_template("playerpovety.html", password=password,poverty1=poverty,poverty2=poverty2,poverty3=poverty3,poverty4=poverty4,
      poverty5=poverty5,poverty6=poverty6,poverty7=poverty7,totalvalue=totalvalue,money=money,username=username,current1=c1,current2=c2,current3=c3
      ,current4=c4,current5=c5,current6=c6,current7=c7)   
    if 'take' in request.form:
      from function.take_item import take_item   
      token = take_item()
      return render_template("tokenpage.html", token=token)     
    if 'buy' in request.form:
      from function.buy_item import buy_item   
      username,password,poverty, poverty2, poverty3,poverty4,poverty5,poverty6,poverty7,totalvalue,money = buy_item()
      va1, va2, va3, va4, va5, va6, va7, c1, c2, c3, c4, c5, c6,c7 = mineral_for_server()
      return render_template("playerpovety.html", username=username,password=password,poverty1=poverty,poverty2=poverty2,poverty3=poverty3,poverty4=poverty4,
      poverty5=poverty5,poverty6=poverty6,poverty7=poverty7,totalvalue=totalvalue,money=money,current1=c1,current2=c2,current3=c3
      ,current4=c4,current5=c5,current6=c6,current7=c7)



if __name__=='__main__':
 app.run(debug=True,host=host,port=hostport)
