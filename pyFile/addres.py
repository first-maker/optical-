from pyFile.db import *
from flask import (Flask,flash, request, render_template,Blueprint)
from flask_session import Session
from pyFile.helpers import*
from pyFile.data import *
addres =Blueprint('addres',__name__, static_folder='static', template_folder='templates')
import sqlite3

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


def datpaseSelect(x):
    addres_list=[]
    conn = sqlite3.connect(dbsqlite)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
 
    cursor.execute( """ SELECT * FROM  address where user_id=:user_id """,
            {"user_id": x, })
    conn.commit()
    records = cursor.fetchall()   
    for r in records:
           addres_list.append(dict(r))

    return addres_list
    

@addres.route('/addres', methods=["POST", "GET"])
@login_required
def updat_address():
    conn = sqlite3.connect(dbsqlite)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    data = get_location()
    model_messag=[]
    addres_list=datpaseSelect(session["user_id"])
    if request.method == "GET":            
        if len(addres_list) > 0:
           if addres_list[0]["user_id"] ==session["user_id"]:
            model_messag="Do you Want update Your Address"
            return render_template("addres.html",countries=countries ,data=data , addresmessag=model_messag,addres_list=addres_list ,updata="done")  
        else :
            
         return render_template("addres.html",countries=countries ,data=data) 


    if request.method == "POST":
        countery_name = request.form.get("countery_name")
        userIP = request.form.get("userIP")
        Region = request.form.get("Region")
        city_name = request.form.get("city_name")
        district_name = request.form.get("district_name")
        street = request.form.get("street")
        buliding_number = request.form.get("buliding_number")
        unit_number = request.form.get("unit_number")
        zip_code = request.form.get("zip_code")
        extend_zip_code = request.form.get("extend_zip_code")
        location_description = request.form.get("location_description")
        location_url = request.form.get("location") 
        UpdateAddras = request.form.get("UpdateAddras") 
        addAddreas = request.form.get("addAddreas") 
        print(addAddreas)
        if UpdateAddras:
            cursor = conn.cursor()
            cursor.execute(""" UPDATE address SET countery_name=:countery_name,Region=:Region,city_name=:city_name,
                           district_name=:district_name,street=:street,buliding_number=:buliding_number,unit_number=:unit_number,
                           zip_code=:zip_code,extend_zip_code=:extend_zip_code,userIP=:userIP,location_description=:location_description,location_url=:location_url WHERE address_id=:address_id;""",  
                            {
                   "countery_name":countery_name,
                   "Region":Region,
                   "city_name":city_name,
                   "district_name":district_name,
                   "street":street,
                   "buliding_number":buliding_number,
                   "unit_number":unit_number,
                   "zip_code":zip_code,
                   "extend_zip_code":extend_zip_code,
                   "userIP":userIP,
                   "location_description":location_description,
                   "location_url":location_url,
                   "address_id": UpdateAddras, })
            conn.commit()
            model_messag=" Your Address Update successfully"
            addres_list=datpaseSelect(session["user_id"])
            return render_template("addres.html",countries=countries ,data=data ,addres_list=addres_list ,updata="done", addresmessag = model_messag )
        if addAddreas:
          try:  
            cursor.execute(
                """insert into address(countery_name,Region,city_name,district_name,street,buliding_number,unit_number,zip_code,extend_zip_code,userIP,location_description,location_url,user_id) values(
                                       :countery_name,:Region,:city_name,:district_name,:street,:buliding_number,:unit_number,:zip_code,:extend_zip_code,:userIP,:location_description,:location_url,:user_id)""",
                {
                   "countery_name":countery_name,
                   "Region":Region,
                   "city_name":city_name,
                   "district_name":district_name,
                   "street":street,
                   "buliding_number":buliding_number,
                   "unit_number":unit_number,
                   "zip_code":zip_code,
                   "extend_zip_code":extend_zip_code,
                   "userIP":userIP,
                   "location_description":location_description,
                   "location_url":location_url,
                   "user_id": session["user_id"], },)

            conn.commit()
            rec=cursor.fetchall()
            print("ca",rec)
            conn.close()
            addres_list=datpaseSelect(session["user_id"])
            model_messag=" Your Address Add successfully"
            return render_template("addres.html",countries=countries ,data=data ,addres_list=addres_list ,updata="done", addresmessag = model_messag )
          except sqlite3.Error as error:
              print("ca",error)
              return render_template("addres.html",countries=countries ,data=data ,addres_list=addres_list ,updata="done", addresmessag = model_messag )
        return render_template("addres.html",countries=countries ,data=data) 

    
 







