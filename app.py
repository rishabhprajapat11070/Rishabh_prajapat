from flask import Flask,render_template,request,Response,redirect,url_for
import os
import time 
import mysql.connector
import time


def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishabhprajapat11070",
        database="user_data"
    )
    

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("portfolio.html")

@app.route("/submit",methods=['POST'])
def Submit():
    if request.method == "POST":
        user = request.form.get("user_name")
        mail = request.form.get("user_mail")
        userMSG = request.form.get("user_msg")
        
        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
            (user, mail, userMSG)
        )

        db.commit()
        db.close()

    return render_template("thanks.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")




port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)


