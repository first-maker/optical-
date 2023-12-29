import json
from pyFile.sqlRequest import *
from pyFile.cart import  hndell_dat
import os 
from flask import ( render_template ,session, jsonify,Blueprint)
from pyFile.helpers import*
from requests.auth import HTTPBasicAuth
import os.path
import ast

from pyFile.data import *

payment =Blueprint('payment',__name__, static_folder='static', template_folder='templates')

payments =Blueprint('/payments/<order_id>/capture',__name__, static_folder='static', template_folder='templates')



# # # # PAYPAL SANDBOX
PAYPAL_BUSINESS_CLIENT_ID = "AZt3SPH-xJlDM6_UQRyZesLw-x2FI8aAFzVNICjP-H-RbaPhYZQlXK633UtDOOPwmZp-LK1lZtHrtWxC"
PAYPAL_BUSINESS_SECRET = "ELssbsSV8X2XFcMvRWj6Da4eD6e1qyByWo03IG1JZKqVidAxp0_RSivsB4Y7omGYDEK_PEa4KViUj98_"
PAYPAL_API_URL = f"https://api-m.sandbox.paypal.com"

# # # # PAYPAL LIVE Details
# PAYPAL_BUSINESS_CLIENT_ID = os.getenv("PAYPAL_LIVE_BUSINESS_CLIENT_ID")
# PAYPAL_BUSINESS_SECRET = os.getenv("PAYPAL_LIVE_BUSINESS_SECRET")
# PAYPAL_API_URL = f"https://api-m.paypal.com"
 
# PAYPAL payment price
# IB_TAX_APP_PRICE = float(10.00)
IB_TAX_APP_PRICE_CURRENCY = "USD"
 
@payment.route("/payment")
@login_required
def paypal_payment():
    handell_iteam=''
    if "iteams"  not in session:
        return render_template("index.html")

    userdatiles=conifg_user(session['user_id'])
    if session["iteams"]:
       handell_iteam=hndell_dat(session["iteams"])
       IB_TAX_APP_PRICE = float(handell_iteam[0]["total"])

    return render_template("payment.html",response=userdatiles ,paypal_business_client_id=PAYPAL_BUSINESS_CLIENT_ID,price=IB_TAX_APP_PRICE, data_view=handell_iteam[1] ,total=handell_iteam[0], currency=IB_TAX_APP_PRICE_CURRENCY)
 

@payments.route("/payments/<order_id>/capture", methods=["POST"])
def capture_payment(order_id):  # Checks and confirms payment
    # print(order_id)
    captured_payment = paypal_capture_function(order_id) 
    # return jsonify('done')
    
    if is_approved_payment(captured_payment):
        # print("approved")
        #  save transiciati datiles 
        directory = './static/payment/'
        filename = f"{order_id}.txt"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(file_path, 'w') as file:
             file.write(json.dumps(captured_payment)) # use `json.loads` to do the reverse
             file.close()
        try:
           conn = sqlite3.connect("stor.db")
           cursor = conn.cursor()
           conn.row_factory = sqlite3.Row
           handell_iteam=hndell_dat(session["iteams"])
           totalAmount=handell_iteam[0]["total"]
           payment_fee=0
           payment_net=totalAmount-payment_fee
           totalQuanet=handell_iteam[0]["quant"]
           paymentdatiels=json.dumps(handell_iteam[1])
           
           payment_order_id=order_id
           payment_status = "COMPLETED"
           cursor.execute(
                        """insert into payment(totalAmount,payment_fee,payment_net,totalQuanet,paymentdatiels,payment_order_id,payment_status,user_Id) values(
                  :totalAmount,:payment_fee,:payment_net,:totalQuanet,:paymentdatiels,:payment_order_id,:payment_status,:user_Id)""",
                        {
                            "totalAmount": totalAmount,
                            # "product_type": request.form.get("product_type"),
                            "payment_fee": payment_fee,
                            "payment_net": payment_net,
                            "totalQuanet": totalQuanet,
                            "paymentdatiels": paymentdatiels,
                            "payment_order_id": payment_order_id,
                            "payment_status": payment_status,
                            "user_Id": session["user_id"],
                        },
                    )
           
           conn.commit()
           payment_id=cursor.lastrowid

           cursor.execute(
                        """insert into order_trak(order_number,stat,notes,user_id,payment_id) values(
                  :order_number,:stat,:notes,:user_id,:payment_id)""",
                        {
                            "order_number": 1,
                            "stat": 0,
                            "notes": 'N',
                            "payment_id": payment_id,
                            "user_id": session["user_id"],
                        },
                    )  
           conn.commit()

           order_trak_id=cursor.lastrowid
           userdatiles=conifg_user(session["user_id"])
           cursor.execute(
                        """insert into invoice(totalAmount,commercial_no,totalQuanet,payment_status,userName,userTell,userIdNo,companyNamy
                         ,branch_name,invoiceType,taxValue,taxAmount,user_Id,branch_id,payment_id,order_id) values(:totalAmount,:commercial_no,
                         :totalQuanet,:payment_status,:userName,:userTell,:userIdNo,:companyNamy
                         ,:branch_name,:invoiceType,:taxValue,:taxAmount,:user_Id,:branch_id,:payment_id,:order_id)""",
                        {
                            'totalAmount':totalAmount,'totalQuanet':totalQuanet,'commercial_no':15579347666,
                            'payment_status':payment_status,'userName':userdatiles[0]['first_name']+ userdatiles[0]['last_name'] ,
                            'userTell':userdatiles[0]['phone'],'userIdNo':userdatiles[0]['email'],'companyNamy':'Hussam Optics',
                            'branch_name':'Online','invoiceType':'Cash','taxValue':15,
                            'taxAmount':totalAmount*(15/100),'user_Id':session["user_id"],'branch_id':1000,'payment_id':payment_id,'order_id':order_trak_id
             
                        },
                    )
           
           conn.commit()
           invoice_id=cursor.lastrowid
           
           for i in handell_iteam[1]:
               productDescrptian= i['brand_name']  +',' + i['Model_no'] +',' + i['brand_description'] 
               cursor.execute("""insert into invoice_datieals (iteamAmount ,iteamquent, Price,discout,netPrice,productDescrptian
                              ,product_id,invoice_id)values(:iteamAmount ,:iteamquent,:Price,:discout,:netPrice,:productDescrptian,
                              :product_id,:invoice_id)""",
                              {

                   'iteamAmount':i['totlaiteam'] ,'iteamquent':i['count'] , 'Price': i['retialPrice'] ,
                   'discout': i['discount'] ,'netPrice': int(i['retialPrice'])-( int(i['retialPrice'])  * (int(i['discount'])/100) ),
                   'productDescrptian':productDescrptian ,
                   'product_id':i['product_id'] ,'invoice_id':invoice_id

        
              })
           conn.commit()    
           
           cursor.execute(""" SELECT first_name,phone,email FROM users WHERE user_id =:user_id  """,   {'user_id':session["user_id"] })
           conn.commit()    
           records = cursor.fetchall() 
        #    print(session["user_id"] )

           messags=messag(invoice_id,order_trak_id,records[0])
           conn.close()
           
        except sqlite3.Error as error:
        #    print(error)
             pass
             
            #  romve seiant after confiarm payment 
        try:
           for key in list(session.keys()):
            #    print(key)
               if key =="iteams":
                    session.pop(key);
        except KeyError:
            pass
    return jsonify(captured_payment)
 

def paypal_capture_function(order_id):
    #   post_route=f"https://api.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture"
    post_route = f"/v2/checkout/orders/{order_id}/capture"
    paypal_capture_url = PAYPAL_API_URL + post_route
    basic_auth = HTTPBasicAuth(PAYPAL_BUSINESS_CLIENT_ID, PAYPAL_BUSINESS_SECRET)
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url=paypal_capture_url, headers=headers, auth=basic_auth)
    response.raise_for_status()
    json_data = response.json()
    return json_data
 
def is_approved_payment(captured_payment):
    status = captured_payment.get("status")
    amount = captured_payment.get("purchase_units")[0].get("payments").get("captures")[0].get("amount").get("value")
    currency_code = captured_payment.get("purchase_units")[0].get("payments").get("captures")[0].get("amount").get("currency_code")
    print(f"Payment happened. Details: {status}, {amount}, {currency_code}")
    if status == "COMPLETED":
        return True
    else:
        return False

