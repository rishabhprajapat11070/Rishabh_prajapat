from flask import Flask,render_template,request,Response,redirect,url_for
import os
import time 
import psycopg2
import time


def get_db():
    conn = psycopg2.connect(
        host="db.endgtpkrhllvqqqehozg.supabase.co",
        database="postgres",
        user="postgres",
        password="Rishabhprajapat11070@",
        port="5432"
    )
    return conn
    

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
        cur = db.cursor()

        cur.execute(
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


