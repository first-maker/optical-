
  # online stor for opical shop
optical  online store 
#### Video Demo: 
 <URL https://www.youtube.com/watch?v=9s3_l0uM89U>
#### Description:

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [ Table_of_Content ](#Table_of_Content )
- [Usage](#usage)
- [License](#license)

## Introduction

The program is a website specialized in eyeglass trading
Products are organized and added in an organized manner. A system for electronic payment, order delivery and follow-up is also provided
## Installation

Provide instructions on how to install your project:

1. Clone the repository: `gh repo clone first-maker/optical-`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
## Table_of_Content
project
1. app.py 
     ###  Main function for the app

2. datbas
3. license.txt
4. requirements.txt :
   >all pip will need it to start app uses
   >
6. pyfile
     ###All Python file will be in this direction
   * addre.py
     ### this file has one function 
     >get_ip  : to get loctian datiles
     >
     >get_location : Handle location details
     >
     >datpaseSelect : To select user address details 
     >
     >updat_address  : to add Or edit The address
     >
   * branch.py
     ###  this file has one function
     >addbranch : To add new company branch
     >
   * brand.py
       ###  this file has one function
     >brandADD  :To add new  Brand
     >
   * cart.py
      ### this file has one function
     >hndell_dat :Handle cart items
     >
     > cartView :To view items in cart
     >
   * copmany.py
     ###  this file has one function
     >companys :To add new company 
     >

   * data.py
     > this file has  dictionaries for data static display
     > 
   * dp.dp
     >to declare database
     >
   * helpers.py
     ### this file has four  function
     >apology : To send erorr Message  
     >login_required : To confirm user Login  
     >password_confiarm :To confirm password requirement
     >messag :To send text Message 

   * model.py
      ### this file has two  function
     > model: To add new  Model
     >updateproduct :To  update   Model
   * payment.py
      ### this file has four  function 
     >paypal_payment :to get  payment  then return answer for
     >
     >capture_payment:To Handle payment request ,then will added order  details to orders table and invoices table
     >
     >paypal_capture_function :To get response details from paypal
     >
     >is_approved_payment:to confirm if payment request is approved or not
     >

   * register.py
     ### this file has two  function
     >registers : to register users
     >
     >logins : to confirm users login
     >

   * resetPassword.py
       ### this file has one  function
     >resetPassword: to reset password
     >

   * sqlRequest.py
        ### this file has many function to request data from database
     >readBroudectList
     >
     >cotegryList
     >
     >cotegryList_collection
     >
     >iteam_view
     >
     >paymentview_user
     >
     >conifg_user
     >
     >invoiceDatiles
     >
     >orderTrack
     >
     >mainInvoiceList
     >
     >resetPassword
     >
     >sqliteHandel

   * updates.py
     ### this file has five  function
     >updateCompany:To update company details
     >
     >updateBrand : To update Branch details
     >
     >updatTrack  : To update orders Track details
     >updateBranch :To update Branch details
     >
     >deleteInvoice:To update Invoices details
     >

   * user.py
     ### this file two  function
     >admin :Page for admins data
     >
     >brofile : Page for users data
     >

   * UserUpdate.py
     ### this file one  function
     >userupdate : To update users details
     >
   * Viwer.py
     ### this file one  function
     >viwerData :to view all data for admins page
     >


7. static
    * imag:
    > this folder for static media used in app design 
         * sosial:
            > this folder for static media used for sosiaal media icon
      > 
   
    * payment
          > this folder to save text file for all paymen transaction
      >
      

    * uploads
      >this folder to save all files uploaded to app
    * layout.js
      > JS file used for layout template
      > 
    * model.js
      >JS file used for model template
      >
    * script.js
      >JS file used for all template
      >
    * search.js
      >JS file used for search template
      >
    * style.css
      >CSS file used for APP design
      > 
8. templates
    ### this Folder has all html templates to will needed to view app
   * add_company.html
   * addJop.html
   *addre.html
   * admin.html
   * branch.html
   * brand.html
   * cart.html
   * email.html
   * error.html
   * help.html
   * history.html
   * index.html
   * invoice.html
   * layout.html
   * learn.html
   * login.html
   * model.html
   * netfectian.html
   * newJop.html
   * orderTrack.html
   * ourBranch.html
   * payhistory.html
   * payment.html
   * register.html
   * reset.html
   * search.html
   * update.html
   * updateBranch.html
   * updateBrand.html
   * updateCompany.html
   * updateProduects.html
   * updateTrack.html
   * updatUser.html
   * upload.html
   * user.html
   * viwer.html
## Usage

Explain how to use/run your Flask project:
1. Run the Flask application:
   ```bash
   python app.py
   ```to work flask with depage 
   flask --app  app.py --debug run

## License
```license.text
© 2024 Copyright: Hussain Codes Company

 
