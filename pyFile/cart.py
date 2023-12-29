from pyFile.db import db
from flask import (Flask, request, render_template, redirect, make_response, url_for, flash, session, jsonify,Blueprint)
from flask_session import Session
from pyFile.helpers import*
from pyFile.data import adminvalue
from pyFile.sqlRequest import iteam_view
cart =Blueprint('cart',__name__, static_folder='static', template_folder='templates')


def hndell_dat(session):
    shows = []
    iteam_count=0
    total_amount=0
    for key in session :
               for i in key :
                   iteam_list = iteam_view(i)  
                   try:
                      iteam_list = iteam_view(i)  
                      after_discount=(int(iteam_list[0]['retialPrice'])-(int(iteam_list[0]['retialPrice'])*int(iteam_list[0]['discount'])/100))
                      totlaiteam=after_discount*key[i]
                      iteam_list[0]["count"] = key[i]
                    #    add net amonut after discoun for 1 iteam
                      iteam_list[0]["after_discount"]=after_discount
                      iteam_list[0]["totlaiteam"]=totlaiteam
                      iteam_count +=int(key[i]) 
                      total_amount += totlaiteam
                   except:
                       pass
                   shows.extend(iteam_list)
    tota_dict={'quant':iteam_count,'total':total_amount}
    return [tota_dict,shows]

    

# cart itaem
@cart.route("/cart", methods=["POST", "GET"])
def cartView():
    if request.args.get("updat"):
        iteam=request.args.get("updat")
        x = iteam.split(",")
        id=x[0]
        count=x[1]
        if "iteams" in session:
             print("g",session["iteams"])
             for key in session["iteams"] :
                for i  in key :
                     if id == i:
                           key[i]=int(count)
             print(session["iteams"])
             return jsonify("EDit")
        else:
             return jsonify("Error")  
        

    if request.args.get("qcard"):
        remov_iteam = request.args.get("qcard")
        if "iteams" in session:
             for key in session["iteams"] :
                for i  in key :
                     if remov_iteam == i:
                        index=session["iteams"].index(key)
                        del session["iteams"][index]
             return jsonify("EDit")
        else:
             return jsonify("Can Not Romve")              
    if request.method == "POST":
        iteam = request.form.get("card_id")
        if "iteams" in session:
            all_keys = set().union(*(d.keys() for d in session["iteams"]))
            if iteam in all_keys :
                for x in  session["iteams"]: 
                        for i in x:
                            if iteam == i:
                                x[i] =x[i]+1
            else:
                session["iteams"].append({iteam:1})
        else:
            session["iteams"] = [{iteam:1}]
        
        handell_iteam=(hndell_dat(session["iteams"]))
        
        # redirect("/")
        return render_template("cart.html", response=handell_iteam[1] ,total=handell_iteam[0])
    else:
        if "iteams" in session:
            handell_iteam=(hndell_dat(session["iteams"]))
            return render_template("cart.html",response=handell_iteam[1] ,total=handell_iteam[0])
        else:
            return render_template("index.html")
        
    
