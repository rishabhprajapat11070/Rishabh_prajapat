from flask import Flask,render_template,request,Response,redirect,url_for
import os
import time

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    return render_template("portfoilo.html")

@app.route("/submit",methods=['POST'])
def Submit():
    if request.method == "POST":
        user = request.form.get("user_name")
        mail = request.form.get("user_mail")
        userMSG = request.form.get("user_msg")
        
        with open("mail_name.txt","+a") as f: 
            f.write(f"{user} , {mail}\n{userMSG} ,{time.perf_counter()}")
    return redirect(url_for("home"))


port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
