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
  
    