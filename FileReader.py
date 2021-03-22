import re
import time
import sqlite3
from Regexes import regexes
from FindCard import ScanContent

def ScanFile(filename):
    scan = {}
    try:
        with open(filename,'r') as files:
            filedata = files.read()
            scan = ScanContent(filedata)
    except Exception as E:
        print(E)
    finally:
        return scan









# a=(r'C:\Users\Suhas\PycharmProjects\scaner_project\king.txt')
# b=['adhar','mobile','e1mail']

# print(scanfile(r'C:\Users\Suhas\PycharmProjects\scaner_project\king.txt',['adhar','mobile','email']))
# c=scanfile(a,b)
# print(c)
