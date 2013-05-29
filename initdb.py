#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('emails.db')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Emails(Id INT, Email TEXT,Label TEXT)")
