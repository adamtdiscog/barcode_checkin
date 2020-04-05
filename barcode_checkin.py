#!/usr/bin/env python3

import os
import time
import sys
import datetime
import MySQLdb
from datetime import datetime


db = MySQLdb.connect("localhost","root","pw","Checkin")
c= db.cursor()


while True:
    user_input = input("Scan ID: ")
    read_from_db = c.execute("SELECT * FROM users WHERE barcode LIKE %s", ("%" + user_input + "%",))
    result = c.fetchall()
    #print (result)
    today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print (today)
    if len(result) == 1:
        print ('Name:' , result[0][1], '| barcode: ' , result[0][3], ' | crew position: ' , result[0][4])
        c.execute("INSERT INTO Data (first_name,last_init,crew,time) VALUES (%s,%s,%s,%s)", (result[0][1],result[0][2][:1],result[0][4],today,))
        db.commit()
           
    else:
        print ("Register new user")
        fn = input("First Name: ")
        ln = input("Last Name: ")
        bc = input("Scan ID: ")
        cp = input("IP or Student: ")
        c.execute("INSERT INTO users (first_name,last_name,barcode,crew_position) VALUES (%s,%s,%s,%s)", (fn,ln,bc,cp,))
        db.commit()

 
