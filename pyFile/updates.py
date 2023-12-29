import sqlite3
from flask import ( request, render_template,  flash,Blueprint)
from pyFile.helpers import*
from pyFile.sqlRequest import conifg_user ,sqliteHandel
from pyFile.data import typelist,brand_list

updateCompany =Blueprint('updateCompany',__name__, static_folder='static', template_folder='templates')
updateBrand =Blueprint('updateBrand',__name__, static_folder='static', template_folder='templates')
updatTrack =Blueprint('updatTrack',__name__, static_folder='static', template_folder='templates')
updateBranch=Blueprint('updateBranch',__name__, static_folder='static', template_folder='templates')
deleteInvoice=Blueprint('deleteInvoice',__name__, static_folder='static', template_folder='templates')
# updateCompany
@updateCompany.route("/updateCompany", methods=["GET", "POST"])
@login_required
def updateCompanys():
    conifg_users=conifg_user(session["user_id"]) 
    if conifg_users[0]["U_type"] == 'user':
        flash("Access is denied!")
        return redirect("/")
    """Show history of payment transactions"""
    conn = sqlite3.connect("stor.db")
    conn.row_factory = sqlite3.Row
    company_id = request.form.get("companyId")
    cursor = conn.cursor()
    cursor.execute ("""SELECT * FROM company where company_id=:company_id """,{'company_id':company_id})
    records = cursor.fetchall()  
    company=sqliteHandel(records)  
    companyUpdate = request.form.get("companyUpdate")
    if request.method == "POST":
      if company_id:
        return render_template("updateCompany.html", company=company ,names=typelist )
      
      if companyUpdate:
        company_email = request.form.get("email")
        company_name = request.form.get("name")
        company_tell = request.form.get("tell")
        commercialNo = request.form.get("commercialNo")
        vat_no = request.form.get("vat")
        company_type = request.form.get("company_type")
        company_address = request.form.get("company_address")
        cursor = conn.cursor()
        cursor.execute(""" UPDATE company SET company_email=:company_email,company_name=:company_name ,company_tell=:company_tell ,commercialNo=:commercialNo
                               ,vat_no=:vat_no,company_type=:company_type,company_address=:company_address
                           WHERE company_id=:company_id;""",  {"company_email":   company_email,'company_name':company_name,'company_tell':company_tell,
                                                      'commercialNo':commercialNo, "vat_no": vat_no 
                                                      ,'company_type':company_type,"company_address":company_address,'company_id':companyUpdate})
        conn.commit()
        
        cursor.execute ("""SELECT * FROM company where company_id=:company_id """,{'company_id':companyUpdate})
        records = cursor.fetchall()  
        company=sqliteHandel(records)  
        conn.close()
        return render_template("updateCompany.html", company=company,  message=company_name,names=typelist )

    return render_template("updateCompany.html", company=company ,names=typelist )


# updateBrand
@updateBrand.route("/updateBrand", methods=["GET", "POST"])
@login_required
def updateBrands():
    conifg_users=conifg_user(session["user_id"]) 
    if conifg_users[0]["U_type"] == 'user':
        flash("Access is denied!")
        return redirect("/")
    """Show history of payment transactions"""
    conn = sqlite3.connect("stor.db")
    conn.row_factory = sqlite3.Row
    brand_id = request.form.get("brand_id")
    cursor = conn.cursor()
    cursor.execute ("""SELECT * FROM brand where brand_id=:brand_id """,{'brand_id':brand_id})
    records = cursor.fetchall()  
    brand=sqliteHandel(records)  
   
    brandUpdate = request.form.get("brandUpdate")
    if request.method == "POST":
      if brand_id:
        return render_template("updateBrand.html", brand=brand,brand_list =brand_list )     
      if brandUpdate:
        brand_name = request.form.get("brand_name")
        brand_type = request.form.get("brand_type")
        manufactory = request.form.get("manufactory") 
        brand_description = request.form.get("brand_description")
        print(brand_name,brand_type,manufactory)
        cursor = conn.cursor()
        cursor.execute(""" UPDATE brand SET brand_name=:brand_name,brand_type=:brand_type ,manufactory=:manufactory ,brand_description=:brand_description
                               
                           WHERE brand_id=:brand_id;""",  {"brand_name":   brand_name,'brand_type':brand_type,'manufactory':manufactory,
                                                      'brand_description':brand_description,'brand_id':brandUpdate})
        conn.commit()
        
        cursor.execute ("""SELECT * FROM brand where brand_id=:brand_id """,{'brand_id':brandUpdate})
        records = cursor.fetchall()  
        brand=sqliteHandel(records)  
        conn.close()
        return render_template("updateBrand.html", brand=brand,brand_list =brand_list ,message=brand_name)     


    return render_template("updateBrand.html")

# updatTrack
@updatTrack.route("/updatTrack", methods=["GET", "POST"])
@login_required
def updatTracks():
    conifg_users=conifg_user(session["user_id"]) 
    if conifg_users[0]["U_type"] == 'user':
        flash("Access is denied!")
        return redirect("/")
    """Show history of payment transactions"""
    conn = sqlite3.connect("stor.db")
    conn.row_factory = sqlite3.Row
    order_id = request.form.get("order_id")
    cursor = conn.cursor()
    cursor.execute ("""SELECT * FROM order_trak where order_id=:order_id    ORDER BY order_id DESC""",
                    {"order_id":order_id})
    records = cursor.fetchall()  
    order=sqliteHandel(records)  
   
    orderUpdate = request.form.get("orderUpdate")
    if request.method == "POST":
      if order_id:
        return render_template("updateTrack.html", order=order)     
      if orderUpdate:
        orderstat = request.form.get("orderstat")
        cursor = conn.cursor()
        cursor.execute(""" UPDATE order_trak SET stat=:orderstat
                               
                           WHERE order_id=:order_id;""",  {"orderstat":orderstat,'order_id':orderUpdate})
        conn.commit()
        
        cursor.execute ("""SELECT * FROM order_trak where order_id=:order_id """,{'order_id':orderUpdate})
        records = cursor.fetchall()  
        order=sqliteHandel(records)  
        conn.close()
        return render_template("updateTrack.html", order=order,message=orderUpdate)     


    return render_template("updateTrack.html")


# updateBranch
@updateBranch.route("/updateBranch", methods=["GET", "POST"])
@login_required
def updateBranchs():
        conifg_users=conifg_user(session["user_id"])  
        print(conifg_users)
        # if conifg_users[0]["U_type"] == 'user':
        #      flash("Access is denied!")
        #      return redirect("/")
        conn = sqlite3.connect("stor.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute( """ SELECT * FROM  users where U_type='admin'""",)
        records = cursor.fetchall()   
        broudect_list=sqliteHandel(records)  
            
    
        if request.method == "POST":
            branch_id = request.form.get("branch_id")
            branchUpdate = request.form.get("branchUpdate")
            cursor = conn.cursor()
            cursor.execute( """ SELECT * FROM  branchs where branch_id=:branch_id """,{'branch_id':branch_id})
            records = cursor.fetchall()
            Branch=sqliteHandel(records) 
            if branch_id :
              return render_template("updateBranch.html", Branch=Branch,broudect_list=broudect_list) 
            if branchUpdate:
                branch_name = request.form.get("branch_name")
                branch_type = request.form.get("branch_type")
                branch_stat = request.form.get("branch_stat")     
                user_id = request.form.get("user_id")
                cursor.execute( """ SELECT * FROM  branchs where branch_name=:branch_name""",{'branch_name':branch_name})
                records = cursor.fetchall()   
                # if len(records)>=1:
                #      cursor.execute( """ SELECT * FROM  branchs where branch_id=:branch_id""",{'branch_id':branchUpdate})
                #      records = cursor.fetchall()
                #      Branch=sqliteHandel(records) 
                #      for i in Branch:
                #         if i['branch_name'] == branch_name:
                #             if  branchUpdate != i['branch_id']:
                #                print(branchUpdate,branchUpdate)
                #                flash('This Branh Name Add Already')
                #                return render_template("updateBranch.html", Branch=Branch,broudect_list=broudect_list) 

                cursor.execute(""" UPDATE branchs SET branch_name=:branch_name,branch_type=:branch_type,branch_stat=:branch_stat,user_id=:user_id
                    WHERE branch_id=:branchUpdate;""",  {"branch_name":branch_name,'branch_type':branch_type,'branch_stat':branch_stat,'user_id':user_id,'branchUpdate':branchUpdate})
                conn.commit()
  
               
                cursor.execute( """ SELECT * FROM  branchs where branch_id=:branch_id """,
                           {'branch_id':branchUpdate}) 
                records = cursor.fetchall()
                Branch=sqliteHandel(records) 
                cursor.close()
                message=branch_name + " : Update successfully"+'  Admin ID : '+  user_id +' For '+branch_name+ ' Branch '
                return render_template("updateBranch.html", Branch=Branch,broudect_list=broudect_list,message=message) 
        else:
          cursor.close() 
          return render_template("updateBranch.html")
    
        
# deleteInvoice
@deleteInvoice.route("/deleteInvoice", methods=["GET", "POST"])
@login_required
def deleteInvoices():
        conn = sqlite3.connect("stor.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        conifg_users=conifg_user(session["user_id"])          
        if request.method == "POST":
            invoice_id = request.form.get("invoice_id")  
            if  invoice_id:   
               cursor.execute( """ SELECT * FROM  invoice where invoice_id=:invoice_id""",{'invoice_id':invoice_id})
               conn.commit()
               records = cursor.fetchall()  
               invoice=sqliteHandel(records)
               if conifg_users[0]["U_type"] == 'user':
                   if invoice[0]['status']=='2':
                       flash("Invoice Already  Cancel Beofer")
                       
                       return render_template("invoice.html",invoice=invoice)
                   if invoice[0]['status']=='1':
                       flash("Invoice Pending To Cancel")
                       return render_template("invoice.html",invoice=invoice)
                   else:
                      cursor = conn.cursor()
                      cursor.execute(""" UPDATE invoice SET status=:status  WHERE invoice_id=:invoice_id;""",  {"status":1,'invoice_id':invoice_id})
                      conn.commit()
                      flash("A request to cancel invoice No. 1 has been submitted, and the request will be executed within 15 working days")
                      return render_template("invoice.html",invoice=invoice)
               else:
                   if invoice[0]['status']=='2':
                         flash("Invoice Already  Cancel Beofer")
                         return render_template("invoice.html",invoice=invoice)
                   else:
                        cursor.execute(""" UPDATE invoice SET status=:status  WHERE invoice_id=:invoice_id;""",  {"status":2,'invoice_id':invoice_id})
                        conn.commit()
                        cursor.execute( """ SELECT user_id ,totalAmount FROM  invoice where invoice_id=:invoice_id""",{'invoice_id':invoice_id})
                        conn.commit()
                        records = cursor.fetchall()  
                        invoicedatiles=sqliteHandel(records) 
                        cursor.execute( """ SELECT wallet FROM  users where user_id=:user_id""",{'user_id': invoicedatiles[0]['user_Id']})
                        records = cursor.fetchall()  
                        wallet=sqliteHandel(records) 
                        wallet[0]['wallet']
                        amount= float(wallet[0]['wallet'])+float(invoicedatiles[0]['totalAmount'])

                        cursor.execute(""" UPDATE users SET wallet =:wallet  WHERE user_id=:user_id;""",  {"wallet":amount, 'user_id':invoicedatiles[0]['user_Id']})
                        conn.commit()
                        cursor.execute( """ SELECT * FROM  invoice where invoice_id=:invoice_id""",{'invoice_id':invoice_id})
                        conn.commit()
                        records = cursor.fetchall()  
                        invoice=sqliteHandel(records)
                        flash("Invoice Cancel")
                        return render_template("invoice.html",invoice=invoice)
        return render_template("invoice.html",invoice=invoice)


