import sqlite3
from flask import ( request, render_template,  flash,Blueprint)
from pyFile.helpers import*
from werkzeug.security import  generate_password_hash
reset =Blueprint('reset',__name__, static_folder='static', template_folder='templates')



@reset.route("/reset", methods=["GET", "POST"])
def resetPassword():
    conn = sqlite3.connect("stor.db")
    if request.method == "POST":
         
        useridReset = request.form.get("useridReset")
      
        if useridReset :
            return render_template("reset.html" ,datain=useridReset )
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        userId=request.form.get("userId")
        if password:
            
            if not password and not confirmation:
               flash("Password And Password Confirma  required!")
            elif password != confirmation :
                flash("Password And Password Confirma  note same!")
                return render_template("reset.html" ,datain=useridReset)
            password = generate_password_hash(password)
            

            cursor = conn.cursor()
            cursor.execute(""" UPDATE users SET hash =:hash WHERE user_id=:user_id;""",  {"hash":   password,  "user_id": userId })
            conn.commit()  
            cursor.close()
            message="Your Password has Update!"
            return render_template("reset.html"  ,message=message)
   
        confiarmUser = request.form.get("confiarmUser")

        if  confiarmUser:
            userName = request.form.get("userName")
            print(userName,confiarmUser)
            cursor = conn.cursor()
             
            cursor.execute(""" SELECT * FROM  users  WHERE user_name = :user_name and email=:email or phone=:phone""",
              { 'user_name': userName, 'email': confiarmUser,  'phone': confiarmUser})
            records = cursor.fetchall()   
            conn.commit()  
            cursor.close()
            
            if len(records) ==1:
                userid=records[0][0]
                message="Enter Your New Password"
                return render_template("reset.html" ,datain=userid , message=message )
            else:
                 flash('Not Correct Enter')
                 return render_template("reset.html" ,dataOut='dataOut' )
            
            
        
            
        
            
        
    return render_template("reset.html" ,dataOut='dataOut')

