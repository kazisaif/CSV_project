from io import TextIOWrapper
from flask import Flask, render_template, request
#from flask_mysqldb import MySQL
import pandas as pd
import pymysql as p

from io import TextIOWrapper
import csv

app = Flask(__name__)


def getconnect():
    return p.connect(host="localhost", user="root", password="rootroot", database="newbootcamp")


@app.route("/", methods=["GET","POST"])

#
#def hello():
 #   cur = db.connection.cursor()
#    names = []
#    cur.execute("select * from movies")
 #   for i in cur:
#        names.append(i)
 #   return render_template('index.html', names = names)


def upload():
    
    if request.method=='POST':
        csv_file=request.files['data_file']
        #csv_file=TextIOWrapper(csv_file,encoding='utf-8')
        #csv_reader1=csv.reader(csv_file,delimiter=',')
        csv_reader=pd.read_csv(csv_file,delimiter=',')
        csv_reader.dropna(inplace=True)

        
        for row in csv_reader:
            #print(row[0],row[1],row[2])
            table = []
            table.append([row[0],row[1],row[2]])

        senddata(table)
        
        records=[]
        db=getconnect()
        cur=db.cursor()
        cur.execute("select * from movies")
        for i in cur:
            records.append(i)
       
    return render_template('index.html',names=records)


def insertrec(t):
    db=getconnect()
    cr=db.cursor()
    sql = "insert into movies(title,content_rating,genre) values(%s,%s,%s)"
    cr.execute(sql, t)

    db.commit()
    db.close()

    print("Committed")


def senddata(table):
    for data in table:
        insertrec(data)
    print("Record Save Successfull")

if __name__ == "__main__":
    app.run(debug = True)
