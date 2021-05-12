import mysql.connector
from datetime import datetime
from flask import Flask, jsonify
import json

with open("username.txt","r") as f:
    username = f.read()
with open("pasword.txt","r") as f:
    pasword = f.read()

app = Flask(__name__)
db = mysql.connector.connect(host="localhost",user=username,passwd=pasword,auth_plugin='mysql_native_password',database="testdatabase")


@app.route("/")
def index():
    print("hello world")
    cur = db.cursor()
    cur.execute("SELECT name,gender,id FROM Test;")
    #cur.callproc('SelectAllNamesByAge2')
    
    
    return jsonify(data=cur.fetchall())

#IN personsGender enum('M','F','O')



if __name__ == "__main__":
    app.run(debug=True)


# with open("username.txt","r") as f:
#     username = f.read()
# with open("pasword.txt","r") as f:
#     pasword = f.read()

# users = [("Janis", datetime.now(), "M"),
# ("Marie-Aline", datetime.now(), "F"),
# ("Janis", datetime.now(), "M")]




#mycursor.execute("SELECT * FROM Test;")


# for x in mycursor:
#     print(x)

# mycursor.executemany("INSERT INTO Test(name,created,gender) VALUES (%s,%s,%s);", users)
# db.commit()