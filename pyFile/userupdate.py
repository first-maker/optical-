import sqlite3
from flask import ( request, render_template,  flash,Blueprint)
from pyFile.helpers import*
from pyFile.sqlRequest import conifg_user

update =Blueprint('update',__name__, static_folder='static', template_folder='templates')

# useridReset userIdUpdat
@update.route("/update", methods=["GET", "POST"])
@login_required
def userupdate():
    userDatiles=''
    conn = sqlite3.connect("stor.db")
    if request.method == "POST":
        userIdUpdat = request.form.get("userIdUpdat")
        userUpdate = request.form.get("userUpdate")
        if userIdUpdat:
           userDatiles=conifg_user(userIdUpdat)
           return render_template("update.html",userDatiles=userDatiles)
        if userUpdate:
           userDatiles=conifg_user(userUpdate)
           return render_template("updatuser.html", userDatiles=userDatiles)
        userId=request.form.get("userId")
        user_id=request.form.get("user_id")
        phone=request.form.get("phone")
        last_name=request.form.get("last_name")
        first_name=request.form.get("first_name")
        email=request.form.get("email")
        U_type=request.form.get("user_type")
        status=request.form.get("status")
      #    update user by users
        if userId:
            if not phone or not last_name  or not first_name or not email:
                 userDatiles=conifg_user(userId)
                 flash('Please Enter all field')
                 return render_template("update.html" ,userDatiles=userDatiles )
            else : 
             try:
                cursor = conn.cursor()
                cursor.execute(""" UPDATE users SET phone=:phone,last_name=:last_name ,first_name=:first_name ,email=:email
                           WHERE user_id=:user_id;""",  {"phone":   phone,'last_name':last_name,'first_name':first_name,   'email':email, "user_id": userId })
                conn.commit()
                userDatiles=conifg_user(userId)
                message='Your Details Had been update Successful'
                cursor.close()
                return render_template("update.html" ,userDatiles=userDatiles ,message=message )
             except sqlite3.Error as error:     
                    flash('error to fetch data')
                    userDatiles=conifg_user(userId)
                    return render_template("update.html" ,userDatiles=userDatiles )

               #   updat user datiles bu admin
        if user_id:
            if not phone or not last_name  or not first_name or not email:
                 userDatiles=conifg_user(user_id)
                 return render_template("updatuser.html" ,userDatiles=userDatiles )
            else:
             try:  
                cursor = conn.cursor()
                cursor.execute(""" UPDATE users SET phone=:phone,last_name=:last_name ,first_name=:first_name ,email=:email ,status=:status,U_type=:U_type
                           WHERE user_id=:user_id;""",  {"phone":   phone,'last_name':last_name,'first_name':first_name,  'email':email, "user_id": user_id  ,'status':status,"U_type":U_type,})
                conn.commit()
                afterupdat=conifg_user(user_id)
                message='Your Details Had been update Successful'
                cursor.close()
                return render_template("updatuser.html" ,userDatiles=afterupdat ,message=message )
             except sqlite3.Error as error:
                 flash('error to fetch data',error)
                 userDatiles=conifg_user(user_id)
                 return render_template("updatuser.html" ,userDatiles=userDatiles )

                    
    return redirect("/brofile")

