#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

uId = 1

con = lite.connect('emails.db')

with con:

    cur = con.cursor()    
    cur.execute("INSERT INTO Emails VALUES(1,'bu@gmail.com','inbox')")
    cur.execute("SELECT Id,Email,Label FROM Emails WHERE Id=:Id AND Label=:Label", 
        {"Id": uId,"Label":"inbox"})        
    con.commit()
    
    row = cur.fetchone()
    if row != None :
    	print len(row)
    	print row
    else :
    	print "vide"