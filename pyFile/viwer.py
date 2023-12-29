import sqlite3
from flask import ( request, render_template,  flash,Blueprint)
from pyFile.helpers import*
from pyFile.sqlRequest import conifg_user
from pyFile.sqlRequest import sqliteHandel
viwer =Blueprint('viwer',__name__, static_folder='static', template_folder='templates')


@viwer.route("/viwer", methods=["GET", "POST"])
@login_required

def viwerData():
    listviwer=['Company',  'Invoice' ,  'Branchs' , 'Broduct', 'Payment' , 'Brands','Orders' , 'Users', ]
    conn = sqlite3.connect("stor.db")
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute ("""SELECT * FROM order_trak   ORDER BY order_id DESC""")
        records = cursor.fetchall()  
        order_trak=sqliteHandel(records)  

        cursor.execute ("""SELECT * FROM users""")
        records = cursor.fetchall()  
        users=sqliteHandel(records)  
        cursor.execute ("""SELECT * FROM payment""")
        records = cursor.fetchall()  
        payment=sqliteHandel(records)  
        cursor.execute ("""SELECT * FROM branchs""")
        records = cursor.fetchall()  
        branchs=sqliteHandel(records)  
        cursor.execute ("""SELECT * FROM invoice""")
        records = cursor.fetchall()  
        invoice=sqliteHandel(records)  
        cursor.execute ("""SELECT * FROM brand""")
        records = cursor.fetchall()  
        brand=sqliteHandel(records)  
        cursor.execute ("""SELECT * FROM company""")
        records = cursor.fetchall()  
        company=sqliteHandel(records)  
        cursor.execute ("""SELECT * FROM product""")
        records = cursor.fetchall()  
        product=sqliteHandel(records)  
        conn.close()
        return render_template("viwer.html",order_trak=order_trak,
                               users=users ,payment=payment ,
                               branchs=branchs,invoice=invoice,
                               brand=brand,company=company,
                               product=product,listviwer=listviwer
                               )
    except sqlite3.Error as error:
            flash(error)
            return render_template("viwer.html")

