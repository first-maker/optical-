from pyFile.db import db
from flask import (request, render_template, redirect,flash,session,jsonify, Blueprint,
)
from pyFile.helpers import *
from pyFile.data import *
from pyFile.sqlRequest import conifg_user,sqliteHandel
updateproduct=Blueprint('updateproduct',__name__, static_folder='static', template_folder='templates')

model = Blueprint(
    "model", __name__, static_folder="static", template_folder="templates"
)
import sqlite3

@updateproduct.route("/updateproduct", methods=["GET", "POST"])
@model.route("/model", methods=["POST", "GET"])
@login_required
def addModel():
    conn = sqlite3.connect("stor.db")
    conn.row_factory = sqlite3.Row

    conifg_users=conifg_user(session["user_id"]) 
    if conifg_users[0]["U_type"] == 'user':
             flash("Access is denied!")
             return redirect("/")

    compny_name = db.execute("SELECT * FROM company where company_type='Supplier' ")
# whil get company name the retiren copmany type
    if request.args.get("companyname"):
       
        session["company_id"] =request.args.get("companyname")
        brand_type = db.execute(
            "SELECT * FROM brand WHERE company_id=? GROUP BY brand_type ",
            request.args.get("companyname"),
        )
        return jsonify(brand_type)
    else:
        brand_type = []

# whil get company type then return brand name
    if request.args.get("brandType"):
        # session to show difrent optian on the model page apout thye type 
        session["brandType"]=request.args.get("brandType")
        brand_name = db.execute(
            "SELECT * FROM brand WHERE brand_type =? and company_id=? ", request.args.get("brandType"), session["company_id"])
        return jsonify(brand_name)
    else:
        brand_name = []
        # return jsonify(brand_name)

    if request.method == "GET":
        return render_template("model.html", compny_name=compny_name, cotgery=cotgery ,lens_cute=lens_cute ,lens_index=lens_index ,power=power)
    else:
        product_id =request.form.get("product_id")
        productUpdate =request.form.get("productUpdate") 
        company_id = request.form.get("companyname")  
        brand_type = request.form.get("brand_type")
        brand_id = request.form.get("brand_name")
        ModelName=request.form.get("ModelName")
        Model_no = request.form.get("Model_no")
        # fram box 
        cotegery = request.form.get("cotegery") #not yet
        CotegeryHistory = request.form.get("CotegeryHistory")  #not yet
        product_colluectian = request.form.get("collection")
        color = request.form.get("color")
        size = request.form.get("size")
        bridge = request.form.get("bridge")
        temple = request.form.get("temple")
    #    mix box 
        lens_type=request.form.get("lens_type")
        Lensmaterial=request.form.get("Lensmaterial")
        Lensdesign=request.form.get("Lensdesign")
 #  lens box 
        lens_index_valu=request.form.get("lens_index")
        lens_cute_vale = request.form.getlist('lens_cute')
        cute_vale=''
        for i in lens_cute_vale:
            cute_vale += i +','
        # contact lens 
        Duration=request.form.get("contactDuration")
    #    static 
        quant = request.form.get("quant")
        wholePrice = request.form.get("wholePrice")
        retialPrice = request.form.get("retialPrice")
        discount = request.form.get("discount")
        tax = request.form.get("tax")
        UPCcode = request.form.get("UPCcode")
        SKUCode = request.form.get("SKUCode")
        description = request.form.get("description")
        serieal=''
        model_messag=''
        if brand_type == 'Frams':
            serieal =  company_id + ',' + brand_id +','+ Model_no+  ',' +  brand_type+','+ ModelName  +  ','  + color+',' +  size +',' +bridge +',' + temple
            model_messag='Frame  '+  serieal + ' Add sucuseus! '
        elif brand_type == 'Lens':  
            serieal =  company_id + ',' + brand_id +','+ Model_no+  ',' +  brand_type+','+ ModelName  +  ',' + color+',' +  size  + ',' +  Lensdesign + ',' +Lensmaterial+ ',' +  lens_type + ',' + cute_vale + ',' +  lens_index_valu 
            model_messag= 'LENS ' + serieal  + ' Add sucuseus! '
        elif brand_type == 'ContactLens': 
             serieal = company_id + ',' + brand_id +','+ Model_no+  ',' +  brand_type+','+ ModelName  +  ',' + color+',' +  size  + ',' +  Lensdesign + ','   +Lensmaterial + ',' +  lens_type  + ',' +  Duration
             model_messag= 'ContactLens ' + serieal  + ' Add sucuseus! ' 
            #  model_messag= 'ContactLens '+ serieal + 'Add sucuseus!'
        elif brand_type == 'Devices' or  brand_type == 'Accessories' or  brand_type == 'Othar': 
             serieal = company_id + ',' + brand_id + ','+ Model_no+  ',' +  brand_type+ ','+ ModelName +',' +  size  
             model_messag= 'Proudect '+ serieal + ' Add sucuseus! '
        if company_id:
         try:
            cursor = conn.cursor()
            # inserting data into table usercontent
            cursor.execute(
                """insert into product(item_description,discount,retialPrice,wholePrice,quant,Collection_name,SKUCode,
                        UPCcode,temple_length,lens_size,bridge_size,color,Model_no, brand_id, company_id,tax,
                        lens_type,lens_index,lens_cute,user_id,serieal,ModelName,
                        Lensmaterial ,  lens_design, Duration , framCotegery , framCotegeryHistory,brand_type) values(
                           :description,:discount,:retialPrice,:wholePrice,:quant,:Collection,:SKUCode,:UPCcode,
                           :temple,:size,:bridge,:color,:Model_no, :brand_id,:company_id,:tax,
                           :lens_type ,:lens_index,:lens_cute,:user_id,:serieal,:ModelName, 
                           :Lensmaterial ,  :lens_design, :Duration , :framCotegery , :framCotegeryHistory,:brand_type)""",
                {
                    "description": description,"discount": discount,                  
                    "retialPrice": retialPrice,"wholePrice": wholePrice,                  
                    "quant": quant,"Collection": product_colluectian,                    
                    "SKUCode": SKUCode,"UPCcode": UPCcode,                    
                    "temple": temple, "size": size,
                    "bridge": bridge,"color": color,                  
                    "Model_no": Model_no,"brand_type": brand_type,                  
                    "brand_id": brand_id,"company_id": company_id,                   
                    "tax": tax,"lens_type":lens_type,               
                    "lens_index":lens_index_valu,"lens_cute":cute_vale,
                    "user_id": session["user_id"],"serieal":serieal,
                    "ModelName":ModelName, "Lensmaterial" : Lensmaterial,             
                    "lens_design" : Lensdesign, "Duration" : Duration,   
                    "framCotegery" : cotegery, "framCotegeryHistory": CotegeryHistory
                },)

            conn.commit()
            conn.close()

            return render_template(
                "model.html",
                response="Date add",model_messag=model_messag,
                compny_name=compny_name,
                cotgery=cotgery,)
            
         except sqlite3.Error as error:
            # using flash function of flask to flash errors.
            print(error)
            flash(f"{error}")
            return render_template(
                "model.html", compny_name=compny_name, cotgery=cotgery  ,lens_cute=lens_cute ,lens_index=lens_index ,power=power
            )
            # updat proudeat 
        if product_id:
               cursor = conn.cursor()
               cursor.execute( """ SELECT * FROM   product  INNER JOIN brand ON brand.brand_id = product.brand_id 
                                   INNER JOIN company ON company.company_id=product.company_id 
                                   where product_id=:product_id""",{'product_id':product_id})
            #    cursor.execute( """ SELECT * FROM  product where product_id=:product_id""",{'product_id':product_id})
               conn.commit()   
               records = cursor.fetchall()  
               product=sqliteHandel(records)
               conn.close()
               return render_template("updateProduects.html", compny_name=compny_name, cotgery=cotgery ,lens_cute=lens_cute ,lens_index=lens_index ,power=power,product=product)
        if productUpdate:
            try:
                cursor = conn.cursor()
                cursor.execute(""" UPDATE product SET  item_description=:description,discount=:discount,retialPrice=:retialPrice,
                               wholePrice=:wholePrice,Collection_name=:Collection,SKUCode=:SKUCode,UPCcode=:UPCcode,
                           temple_length=:temple,lens_size=:size,bridge_size=:bridge,color=:color,Model_no=:Model_no,tax=:tax,
                           lens_type=:lens_type ,lens_index=:lens_index,lens_cute=:lens_cute,ModelName=:ModelName, 
                           Lensmaterial=:Lensmaterial ,lens_design=:lens_design,Duration= :Duration ,framCotegery= :framCotegery ,
                           framCotegeryHistory= :framCotegeryHistory  
                           WHERE product_id=:product_id;""", 
                            {
                    "description": description,"discount": discount,                  
                    "retialPrice": retialPrice,"wholePrice": wholePrice,                  
                    "Collection": product_colluectian,                    
                    "SKUCode": SKUCode,"UPCcode": UPCcode,                    
                    "temple": temple, "size": size,
                    "bridge": bridge,"color": color,                  
                    "Model_no": Model_no,                          
                    "tax": tax,"lens_type":lens_type,               
                    "lens_index":lens_index_valu,"lens_cute":cute_vale,
                #    "serieal":serieal,
                    "ModelName":ModelName, "Lensmaterial" : Lensmaterial,             
                    "lens_design" : Lensdesign, "Duration" : Duration,   
                    "framCotegery" : cotegery, "framCotegeryHistory": CotegeryHistory,
                    'product_id':productUpdate})
                conn.commit()
                cursor.execute( """ SELECT * FROM   product  INNER JOIN brand ON brand.brand_id = product.brand_id 
                                   INNER JOIN company ON company.company_id=product.company_id 
                                   where product_id=:product_id""",{'product_id':productUpdate})
            #    cursor.execute( """ SELECT * FROM  product where product_id=:product_id""",{'product_id':product_id})
                conn.commit()   
                records = cursor.fetchall()  
                product=sqliteHandel(records)
                conn.close()
                
                return render_template("updateProduects.html",model_messag="Proudeact Update", compny_name=compny_name, cotgery=cotgery ,lens_cute=lens_cute ,lens_index=lens_index ,power=power,product=product)

                # return render_template( "updateProduects.html", response="Proudeact Update",model_messag=model_messag, compny_name=compny_name, cotgery=cotgery,)
            except sqlite3.Error as error:
            # using flash function of flask to flash errors.
               print(error)
               flash(f"{error}")
            return render_template( "updateProduects.html", compny_name=compny_name, cotgery=cotgery  ,lens_cute=lens_cute ,lens_index=lens_index ,power=power)
        return render_template( "viwer.html")


