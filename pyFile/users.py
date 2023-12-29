import sqlite3
from flask import ( render_template, redirect, url_for, session,Blueprint)
from pyFile.helpers import* 
from pyFile.sqlRequest import paymentview_user ,orderTrack,mainInvoiceList,sqliteHandel,conifg_user
from pyFile.data import adminvalue
admin =Blueprint('admin',__name__, static_folder='static', template_folder='templates')
brofile =Blueprint('brofile',__name__, static_folder='static', template_folder='templates')

# admin page
@admin.route('/admin', methods=["POST", "GET"])
@login_required
def admins():
    admin_functian=adminvalue
    try:
      type =conifg_user(session["user_id"]) 
      if type[0]["U_type"] == "admin":
            return render_template(
                "admin.html", response=type, admin_functian=admin_functian
            )
      else:
            return redirect(url_for("index"))
    except sqlite3.Error as error:
        return render_template("admin.html",admin_functian=admin_functian)


# user Profial
@brofile.route("/brofile", methods=["POST", "GET"])
@login_required
def brofiles():
    InvoiceList=mainInvoiceList(session["user_id"])  
    user_payment=paymentview_user(session["user_id"])
    orderTracks=orderTrack(session["user_id"])
    try:
      type =conifg_user(session["user_id"]) 
      if type[0]["U_type"] == "user":
            return render_template("user.html", response=type ,user_payment=user_payment ,orderTrack=orderTracks ,invoice=InvoiceList)
      else:
            return redirect(url_for("index"))

    except sqlite3.Error as error:
        return redirect(url_for("index"))



