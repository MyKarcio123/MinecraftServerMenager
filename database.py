import sqlite3
from os import path,mkdir,getenv
from pathlib import Path

def firstLaunch():
    dir = path.expandvars(r'%APPDATA%\ServerMenager\servers.sqlite')
    if not Path(dir).is_file():
        mkdir(getenv('APPDATA')+"\ServerMenager")
    conn = sqlite3.connect(dir)
    database = conn.cursor()
    database.execute('''CREATE TABLE IF NOT EXISTS servers
    (id integer PRIMARY KEY AUTOINCREMENT, name text NOT NULL, dir text NOT NULL)''')

def add(name,dirk):
    dir = path.expandvars(r'%APPDATA%\ServerMenager\servers.sqlite')
    conn = sqlite3.connect(dir)
    database = conn.cursor()
    params = (name,dirk)
    sql = '''INSERT INTO servers(id,name,dir) VALUES(NULL,?,?)'''
    database.execute(sql,params)
    conn.commit()

def refresh(object):
    dir = path.expandvars(r'%APPDATA%\ServerMenager\servers.sqlite')
    conn = sqlite3.connect(dir)
    database = conn.cursor()
    database.execute("SELECT * FROM servers")

    rows = database.fetchall()

    object.clear()

    for row in rows:
        object.addItem(row[1])

def getPath(name):
    dir = path.expandvars(r'%APPDATA%\ServerMenager\servers.sqlite')
    conn = sqlite3.connect(dir)
    database = conn.cursor()
    sql = "SELECT * FROM servers WHERE name='"+name+"'"
    database.execute(sql)

    rows = database.fetchall()

    return rows[0][2]