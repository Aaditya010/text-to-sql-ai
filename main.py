from fastapi import FastAPI
import sqlite3

app=FastAPI()

"""Database Setup"""

def init_db():
  conn=sqlite3.connect("database.db")
  cursor=conn.cursor()

  cursor.execute("DROP TABLE IF EXISTS customers")

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS customers (
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER,
               spending INTEGER
  )
  """)

  cursor.execute("DELETE FROM customers") #Danger

  cursor.execute("INSERT INTO customers VALUES (1,'Messi','39','1000')")
  cursor.execute("INSERT INTO customers VALUES (2,'Ronaldo','41','900')")
  cursor.execute("INSERT INTO customers VALUES (3,'Neymar','33','700')")
  cursor.execute("INSERT INTO customers VALUES (4,'Mbappe','26','800')")
  cursor.execute("INSERT INTO customers VALUES (5,'Haaland','25','800')")

  conn.commit()
  conn.close()

init_db()

@app.get("/")
def home():
  return{"message":"Running sql to text"}

@app.get("/customers")
def get_customers():
  conn=sqlite3.connect("database.db")
  cursor=conn.cursor()

  cursor.execute("SELECT * FROM customers")
  data=cursor.fetchall()

  conn.close()

  return{"Data":data}




