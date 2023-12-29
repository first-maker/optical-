
from flask import (request, render_template, redirect,flash, session,Blueprint)
from flask_session import Session
from pyFile.helpers import*
from pyFile.data import *
import sqlite3
from pyFile.sqlRequest import conifg_user 
branch =Blueprint('branch',__name__, static_folder='static', template_folder='templates')

@branch.route("/branch", methods=["GET", "POST"])
@login_required
def addbranch():
        broudect_list=[]
        branchs=[]
        conn = sqlite3.connect("stor.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute( """ SELECT * FROM  users where U_type='admin'""",)
        
        records = cursor.fetchall()   
        for r in records:
           broudect_list.append(dict(r))
    
        conifg_users=conifg_user(session["user_id"])      
        if conifg_users[0]["U_type"] == 'user':
             flash("Access is denied!")
             return redirect("/")

        if request.method == "POST":
            branch_name = request.form.get("branch_name")
            branch_type = request.form.get("branch_type")
            branch_stat = request.form.get("branch_stat")     
            user_id = request.form.get("user_id")
            if branch_name :
              cursor.execute( """ SELECT * FROM  branchs where branch_name=:branch_name""",{'branch_name':branch_name})
              records = cursor.fetchall()   
              if len(records)>=1:
                flash('This Branh Name Add Already')
                return render_template("branch.html", broudect_list=broudect_list)
              
            try:
              cursor.execute(
                """insert into branchs(branch_name,branch_type,branch_stat,user_id) values(
                                       :branch_name,:branch_type,:branch_stat,:user_id)""",
                {
                   "branch_name":branch_name,
                   "branch_type":branch_type,
                   "branch_stat":branch_stat,
                   "user_id":user_id,
                },)
              conn.commit()
              cursor.close()
              message=branch_name + " : Add successfully"+' Branch admin ID :'+ user_id 
              return render_template("branch.html", broudect_list=broudect_list,message=message)
            except sqlite3.Error as error:
                flash(error)
                print("Failed to read data from sqlite table", error)
                return render_template("branch.html", broudect_list=broudect_list)
        else:
          cursor.close() 
          return render_template("branch.html", broudect_list=broudect_list)

   