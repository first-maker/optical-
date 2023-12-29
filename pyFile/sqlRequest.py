
import sqlite3
import ast
def readBroudectList(product_type):
    broudect_list = []
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """SELECT product_id ,brand_name,Model_no,serieal ,framCotegery
        FROM product INNER JOIN company ON company.company_id = product.company_id
        INNER JOIN brand ON brand.brand_id = product.brand_id where brand.brand_type=:brand_type""",  { "brand_type":product_type, })
        records = cursor.fetchall()
        broudect_list=sqliteHandel(records)

        cursor.close()
        
    except sqlite3.Error as error:
        pass
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return broudect_list





def cotegryList(search):
    
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute(""" SELECT * FROM  addMedia  INNER JOIN product ON product.product_id=addMedia.product_id 
        INNER JOIN brand ON brand.brand_id = product.brand_id 
        INNER JOIN company ON company.company_id=product.company_id WHERE Model_no  LIKE ? or Collection_name LIKE ?  or framCotegery  LIKE ?""" ,
         (f'%{search}%',f'%{search}%',f'%{search}%',))
        records = cursor.fetchall()   
        broudect_list=sqliteHandel(records)
        print('s',broudect_list)
        cursor.close()
        
    except sqlite3.Error as error:
        pass
    finally:
        if sqliteConnection:
            sqliteConnection.close()

    return broudect_list


def allPProdueact():  
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  addMedia  INNER JOIN product ON product.product_id=addMedia.product_id 
        INNER JOIN brand ON brand.brand_id = product.brand_id 
        INNER JOIN company ON company.company_id=product.company_id """,)
        records = cursor.fetchall() 
        cursor.close()   
        broudect_list=sqliteHandel(records)
        return  broudect_list
    except sqlite3.Error as error:
        # print(error)
        pass
    finally:
        if sqliteConnection:
            sqliteConnection.close()

def fram_cetgeray(value):
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  addMedia  INNER JOIN product ON product.product_id=addMedia.product_id 
        INNER JOIN brand ON brand.brand_id = product.brand_id 
        INNER JOIN company ON company.company_id=product.company_id where product.framCotegery=:framCotegery """,
        { 'framCotegery':value})
        records = cursor.fetchall() 
        cursor.close()   
        broudect_list=sqliteHandel(records)
        print(broudect_list)
        return  broudect_list
    except sqlite3.Error as error:
        print(error)
        # pass
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def newOffetTopSell(value):
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  addMedia  INNER JOIN product ON product.product_id=addMedia.product_id 
        INNER JOIN brand ON brand.brand_id = product.brand_id 
        INNER JOIN company ON company.company_id=product.company_id where product.framCotegeryHistory=:framCotegeryHistory """,
        { 'framCotegeryHistory':value})
        records = cursor.fetchall() 
        cursor.close()   
        broudect_list=sqliteHandel(records)
        return  broudect_list
    except sqlite3.Error as error:
        print(error)
        # pass
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def hotseller():
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  addMedia  INNER JOIN product ON product.product_id=addMedia.product_id 
        INNER JOIN brand ON brand.brand_id = product.brand_id 
        INNER JOIN company ON company.company_id=product.company_id where product.discount >20""",
)
        records = cursor.fetchall() 
        cursor.close()   
        broudect_list=sqliteHandel(records)
        return  broudect_list
    except sqlite3.Error as error:
        print(error)
        # pass
    finally:
        if sqliteConnection:
            sqliteConnection.close()



def cotegryList_collection(value,branch):
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  addMedia  INNER JOIN product ON product.product_id=addMedia.product_id 
        INNER JOIN brand ON brand.brand_id = product.brand_id 
        INNER JOIN company ON company.company_id=product.company_id  """ ,)
        records = cursor.fetchall()    
        broudect_list=sqliteHandel(records)

        cursor.close()
        
    except sqlite3.Error as error:
        pass
        # print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")            


    newlist=[]

    for i in broudect_list :
            # to get framsy type
            if i['framCotegery'] == value and i['Collection_name'] == branch :
                newlist.append(i)
                return newlist
            # to get new collectia
            elif i['framCotegeryHistory'] == value and i['Collection_name'] == branch :
               newlist.append(i)
               return newlist
        #    to get contact lens 
            elif i['brand_type'] == value and i['lens_cute'] == branch :
               newlist.append(i)
               return newlist
        #    to get offers 
            elif i['framCotegeryHistory'] == value  and i['framCotegeryHistory'] == branch  :
               newlist.append(i)
               return 
        #    to get acceray 
            elif i['brand_type'] == value and i['Collection_name'] == branch :
               newlist.append(i)
               return newlist




def iteam_view(value):
    broudect_list = []
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  addMedia  INNER JOIN product ON product.product_id=addMedia.product_id 
        INNER JOIN brand ON brand.brand_id = product.brand_id 
        INNER JOIN company ON company.company_id=product.company_id where product.product_id=:product_id """,
        {
            'product_id':value
        })
        records = cursor.fetchall()   
        
        broudect_list=sqliteHandel(records)   
        cursor.close()
        
    except sqlite3.Error as error:
        pass
        # print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
        return  broudect_list  
        
            


def paymentview_user(userid):
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  payment   where user_Id=:user_Id  ORDER BY payment_id DESC""", {'user_Id': userid})
        records = cursor.fetchall()   
        
        cursor.close()   
        broudect_list=sqliteHandel(records)
        for i in broudect_list:
            if i['paymentdatiels']:
                d=ast.literal_eval(i['paymentdatiels'])
                i['paymentdatiels']=d
      
    except sqlite3.Error as error:
        pass
        # print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
        return  broudect_list  


def  conifg_user(userid):  
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM users WHERE user_id =:user_Id """,
        {
            'user_Id': userid
        })
        records = cursor.fetchall()   
        broudect_list=sqliteHandel(records)  
        return    broudect_list



def  invoiceDatiles(invoiceId):  
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  invoice  INNER JOIN invoice_datieals ON invoice_datieals.invoice_id=invoice.invoice_id 
                       where invoice.invoice_id=:invoice_id or invoice.payment_id=:payment_id   """,
        {
            'invoice_id':invoiceId,
            'payment_id':invoiceId
        })
        records = cursor.fetchall()   
        invoiceList=sqliteHandel(records)

        return    invoiceList

def  invoiceDatilesByPaumeant(payment):  
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  invoice  INNER JOIN invoice_datieals ON invoice_datieals.invoice_id=invoice.invoice_id 
                       where  invoice.payment_id=:payment_id    """,
        {
   
            'payment_id':payment
        })
        records = cursor.fetchall()   
        invoiceList=sqliteHandel(records)

        return    invoiceList


def  mainInvoiceList(userid):  
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute( """ SELECT * FROM  invoice  where user_Id=:user_Id """,{'user_Id': userid })
        records = cursor.fetchall()   
        invoiceList=sqliteHandel(records)
        return    invoiceList

def orderTrack(user_id):
    try:
        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute ("""SELECT * FROM order_trak where user_id=:user_id  ORDER BY order_id DESC""",{"user_id": user_id})
# or invoice.payment_id=:invoice_id DESC 
        records = cursor.fetchall()       
        orderTracks=sqliteHandel(records)
    except sqlite3.Error as error:
        pass
    return orderTracks



# user_id  user_name email phone
def  resetPassword(name , id):  

        sqliteConnection = sqlite3.connect("stor.db")
        sqliteConnection.row_factory = sqlite3.Row
        cursor = sqliteConnection.cursor()
        cursor.execute(""" SELECT * FROM users WHERE user_name =:user_name and email=:email or phone=:phone  """,
        {
            'user_name': name,
            'email': id,
            'phone': id,
        })
        records = cursor.fetchall()   
        broudect_list=sqliteHandel(records)

        return    broudect_list
    
    
  #  handell sqlite reture to dicinary
def sqliteHandel(i):
    list=[]
    for r in i:
        list.append(dict(r))
    return list
