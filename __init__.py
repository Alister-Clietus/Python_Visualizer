
from itertools import repeat
from flask import Flask,render_template,request,flash,redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from werkzeug.security import generate_password_hash,check_password_hash
from model import User



db = SQLAlchemy()
DB_NAME = "Userdetails.db"

def main():
    app=Flask(__name__)
    app.config['SECRET_KEY']='ASDFGHJKLQEWERTYUIO'
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqllite///{DB_NAME}'
    db.init_app(app)
    create_database(app)
    return app

app=main()



def create_database(app):
    if not path.exits("/" +DB_NAME):
        db.create_all(app=app)
        print("Create database")



@app.route('/login',methods=["GET","POST"])
def Login():
    data=request.form
    print(data)
    return render_template("LoginPage.html")



@app.route('/signup',methods=["GET","POST"])
def Signup():
    if request.method == "POST":
        firstname=request.form.get("firstname")
        second_name=request.form.get("secondname")
        user_name=request.form.get("usr")
        email=request.form.get("email")
        psw=request.form.get("psw")
    
        if len(email)<4:
           flash("Email Must Be GreaterThan 4", category="error")
        elif user_name<2:
            flash("Entered Username Not Valid")   
        elif len(firstname)<2:
            flash("First Name Must Be Greater Than One", category="error")
        elif len(second_name)==0:
            flash("Second Name Cannot Be Zero")    
        elif psw!= psw-repeat:
            flash("Password NoT Matching", category="error")
        else:
            new_user=User(First_Name=firstname,Second_name=second_name,User_Name=user_name,Email=email,Password=generate_password_hash(psw,method="sha123"))
            db.session.add(new_user)
            db.session.commit
            flash("Account Created successfully" , category="success")
            return redirect(url_for("Login"))
    else:
        return render_template("SignupPage.html")            
       



if __name__=='__main__':
    app.run(debug=True)