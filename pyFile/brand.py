from pyFile.db import db
from flask import (Flask, request, render_template, redirect, make_response, url_for, flash, session, jsonify,Blueprint)
from flask_session import Session
from pyFile.helpers import*
from pyFile.data import brand_list

brand =Blueprint('brand',__name__, static_folder='static', template_folder='templates')

@brand.route('/brand', methods=["POST", "GET"])
@login_required
def brandADD():
    user_type = db.execute("SELECT * FROM users WHERE user_id =? ", session["user_id"])

    if  user_type[0]["U_type"] == "user":
            flash("Access is denied!")
            return redirect("/")
    cofiarm_name = db.execute("SELECT * FROM company where company_type='Supplier' ")
    if request.method == "GET":
        return render_template("brand.html" , response=cofiarm_name, brand_list=brand_list)
    else:
        company_id = request.form.get("companyname")
        brand_name = request.form.get("brand_name")
        brand_type = request.form.get("brandType")
        manufactory = request.form.get("Manufactory")
        brand_description = request.form.get("Description")
        print(company_id)
        if  company_id =='Open this select menu' or not company_id:
            flash("Supplier name is required !")
            return render_template("brand.html", response=cofiarm_name, brand_list=brand_list)
        if not brand_name:
            flash("Brand is required !")
            return render_template("brand.html", response=cofiarm_name, brand_list=brand_list)
        if   brand_type =='Open this select menu' or not brand_type:
            flash("Brand Type is required !")
            return render_template("brand.html", response=cofiarm_name, brand_list=brand_list)      
        if not manufactory:
            flash("Manufactory Type is required !")
            return render_template("brand.html", response=cofiarm_name, brand_list=brand_list)
        if not brand_description:
            flash("Description Type is required !")
            return render_template("brand.html", response=cofiarm_name, brand_list=brand_list)
            
        confiarm_name = db.execute("SELECT * FROM brand WHERE brand_name =?  ", brand_name)
        if  len(confiarm_name) > 0:
            flash(brand_name)
            flash("company Added already")
            return render_template("brand.html", response=cofiarm_name, brand_list=brand_list)

        db.execute(
            "INSERT INTO brand (brand_name,brand_type,manufactory,brand_description,company_id,user_id)VALUES (?,?,?,?,?,?);",
            brand_name,
            brand_type,
            manufactory,
            brand_description,
            company_id,
            session["user_id"]
        )
        return render_template("brand.html" , response=cofiarm_name , brand_list=brand_list ,brand_messag=brand_name)



