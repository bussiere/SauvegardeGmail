import libgmail

email = "ttestbussiere@gmail.com"

import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email, '#####')
mail.list()

label = "inbox"
# Out: list of "folders" aka labels in gmail.
mail.select(label) # connect to inbox.
result, data = mail.search(None, "ALL")
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string


import sqlite3 as lite
import sys



con = lite.connect('emails.db')

with con:

    cur = con.cursor()    

    for idem in id_list:
        cur.execute("SELECT Id FROM Emails WHERE Id=:Id and Label=:Label", {"Id": idem,"Label":label})        
        con.commit()
        row = cur.fetchone()
        if row == None :
            result, data = mail.fetch(idem, "(RFC822)")
            f = open('%s%d'%(label,idem), 'w')
            f.write(data[0][1])
            f.close()
            cur.execute("INSERT INTO Emails VALUES(:Id,:Email,:Label)",{"Id": idem,"Email": email,"Label":label})
            con.commit()