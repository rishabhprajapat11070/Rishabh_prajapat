from flask import Flask,render_template,request,Response,redirect,url_for
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



if __name__=="__main__":
    app.run(debug=True)
