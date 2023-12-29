from pyFile.db import db
from flask import (Flask, request, render_template, redirect, make_response, url_for, flash, session, jsonify,Blueprint)
from flask_session import Session
from pyFile.helpers import*
from werkzeug.security import check_password_hash, generate_password_hash
register =Blueprint('register',__name__, static_folder='static', template_folder='templates')

login =Blueprint('login',__name__, static_folder='static', template_folder='templates')

@register.route("/register", methods=["GET", "POST"])
def registers():
    """Register user"""
    if request.method == "POST":
        # get datieal from post form
        password = request.form.get("password")
        confiarm_password = request.form.get("confirmation")
        username = request.form.get("username")
        # Ensure username was submitted

        # Ensure password was submitted
        if not request.form.get("first_name"):
            flash("must provide First  Name")
            return render_template("register.html")

        elif not request.form.get("last_name"):
            flash("must provide Last  Name")
            return render_template("register.html")


        elif not request.form.get("email"):
            flash("must provide   Email")
            return render_template("register.html")


        elif not request.form.get("phone"):
            flash("must provide Tell Number")
            return render_template("register.html")
        elif not username:
            flash("must provide username")
            return render_template("register.html")
        elif not password:
            flash("must provide password")
            return render_template("register.html")
        elif not confiarm_password:
            flash("must confiarm password")
            return render_template("register.html")
       
        if password != confiarm_password:
            flash("password do not much")
            return render_template("register.html")
        duplicate = db.execute("select * from users  WHERE user_name =?", username)

        if len(duplicate) >= 1:
            flash("User name  Used")
            return render_template("register.html")
      
        if len(username) < 5 or len(username) > 15:
            flash("User Name at lest 5 digit mix 15 digit")
            return render_template("register.html")
        
        email_duplicate = db.execute("select * from users  WHERE email =?", request.form.get("email"))       
        if len(email_duplicate) >= 1:
            flash("Email   Used")
            return render_template("register.html")
        phone_duplicate = db.execute("select * from users  WHERE phone =?", request.form.get("phone"))   
        print(phone_duplicate)   
        if len(phone_duplicate) >= 1:
            flash("Tell is Used for Another User")
            return render_template("register.html")

        if password_confiarm(password) != True:
            flash(password_confiarm(password))
            return render_template("register.html")
        if not  request.form.get("user_type"):
            user_type="user"
        else:
            user_type= request.form.get("user_type")
            print(request.form.get("phone"))
        password = generate_password_hash(password)
        try:
          db.execute("INSERT INTO users (user_name,first_name,last_name,email,phone,hash,U_type)VALUES (?,?,?,?,?,?,?);",username,
            request.form.get("first_name"),
            request.form.get("last_name"),
            request.form.get("email"),
            request.form.get("phone"),
            password,
            user_type )
        except:
            flash(f"{'eroer to add '}")
            return render_template("register.html")
        return render_template("register.html", success="Successful Register")

        # return render_template("register.html", success="Successful Register")
    else:
        return render_template("register.html")


list=[]
@register.route("/login", methods=["GET", "POST"])
def logins():

    """Log user in"""
    # Forget any user_id

    try:
        if session["user_id"]:
           session.pop("user_id")
        # del session["user_id"]
    except KeyError:
        pass

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE user_name = ?", request.form.get("username")
        )
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)
        # print( session)
        # del session["user_id"]

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]
        user = db.execute("SELECT * FROM users WHERE user_name = ?", session["user_id"])
        session["type"] = rows[0]["U_type"]
        # print( session)

        if rows[0]["U_type"] == "user":
            return redirect("cart")
        elif rows[0]["U_type"] == "admin":
            return redirect("admin")
        # Redirect user to home page
    # User reached route via GET (as by clicking a link or via redirect)


    else:
       
        return render_template("login.html")
    
    
