'''
creating database and tables in it
'''
import sqlite3
import os

con = sqlite3.connect("dbtestdelete.db")

c = con.cursor()
'''
c.execute("""CREATE TABLE robert (
        Name text,
        phone text,
        message text
)""")

c.execute("INSERT INTO robert VALUES ('Robert','0724942856','The Lords is God')")


programers =[
        ('Shadrack','072245643','I am now a CEO'),
        ('John','078965324','I chose Network code'),
        ('Wilkister','078653457','I chose automation code')
        ]
c.executemany("INSERT INTO robert VALUES(?,?,?)",programers)
'''
c.execute("SELECT rowid,* FROM robert")
print(c.fetchone()[1])
#print(c.fetchmany()[0])
print(c.fetchall()[0])

con.commit()

#print("Command executed successful")

con.close()
