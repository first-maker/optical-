from pyFile.db import db
from flask import (Flask, request, render_template, redirect, make_response, url_for, flash, session, jsonify,Blueprint)
from flask_session import Session
from pyFile.helpers import*
from pyFile.data import *
company =Blueprint('company',__name__, static_folder='static', template_folder='templates')

@company.route('/company', methods=["POST", "GET"])
@login_required
def companys():
    user_type = db.execute("SELECT * FROM users WHERE user_id =? ", session["user_id"])
    if  user_type[0]["U_type"] == "user":
            flash("Access is denied!")
            return redirect("/")
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        tell = request.form.get("tell")
        commercialNo = request.form.get("commercialNo")
        vat = request.form.get("vat")
        company_type = request.form.get("company_type")
        company_address = request.form.get("company_address")
        if not email:
            flash("Email is required!")
            return render_template("add_company.html")

        if not name:
            flash("Company Name is required!")
            return render_template("add_company.html")
        if not tell:
            flash("Tell  is required!")
            return render_template("add_company.html")
        if not commercialNo:
            flash("commercial No is required!")
            return render_template("add_company.html")
        if not vat:
            flash("Vat No is required!")
            return render_template("add_company.html")
        if not company_type:
            flash("Select Company Type!")
            return render_template("add_company.html")
        if not company_address:
            flash("Address is required!")
            return render_template("add_company.html")
        confiarm_name = db.execute("SELECT * FROM company WHERE company_name =? ", name)
        if  len(confiarm_name) > 0:
            flash(name)
            flash("company Added already")
            return render_template("add_company.html")
        print(session["user_id"])

        db.execute(
            "INSERT INTO company (company_email,company_name,company_tell,commercialNo,vat_no,company_type,company_address,user_id)VALUES (?,?,?,?,?,?,?,?);",
            email,
            name,
            tell,
            commercialNo,
            vat,
            company_type,
            company_address, session["user_id"]
        )
        
        # print(add_copmany)
        return render_template("add_company.html", message=name, names=typelist)
    else:
       return render_template("add_company.html", names=typelist)


