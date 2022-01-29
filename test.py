import pandas as pd
import pymysql as p
from flask import Flask,request,render_template

 


app = Flask(__name__)



@app.route("/", methods=["GET","POST"])

def load():
    if request.method=='POST':
        csv_file=request.files['data_file']
        df=pd.read_csv(csv_file)
        df.dropna(inplace=True)
        records=[]
        table = []
        for i in df.itertuples():
            #print(i[0],i[1],i[2])
            table.append([i[0],i[1],i[2]])

    d=getconnect()
    cur=d.cursor()
    cur.execute("select * from movies")
    for i in cur:
        records.append(i)
    
    senddata(table)
    return render_template('index.html',names=records)

def getconnect():
    return p.connect(host="localhost", user="root", password="rootroot", database="newbootcamp")


def insertrec(t):
    db = getconnect()
    cr = db.cursor()

    sql = "insert into movies(title,content_rating,genre) values(%s,%s,%s)"
    cr.execute(sql, t)

    db.commit()
    db.close()

    
def senddata(table):
    for data in table:
        insertrec(data)
    print("Data transfered Successfully...!")

if __name__ == "__main__":
    app.run(debug = True)


