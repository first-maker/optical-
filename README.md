
  # Your Flask Project Name

Brief description or introduction to your Flask project.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [ Table of Content ](#Table of Content )
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
## Table of Content
project
1. app.py 
     ###  Main Functian for the app

2. datbas
3. license.txt
4. pyfile
     ### All Python  file will py here
   * addre.py
     ### this file has one functian 
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
     ### this file has four  functian
     >apology : To send erorr Message  
     >login_required : To confirm user Login  
     >password_confiarm :To confirm password requirement
     >messag :To send text Message 

   * model.py
      ### this file has two  functian
     > model: To add new  Model
     >updateproduct :To add update   Model
     

   * payment.py
      ### this file has three  functian
     >paypal_payment :
     >capture_payment:
     >paypal_capture_function

   * register.py
           ### this file two  functian

   * resetPassword.py.
       ### this file two  functian

   * sqlRequest.py
        ### this file two  functian

   * updates.py
           ### this file two  functian

   * user.py
           ### this file two  functian

   * UserUpdate.py
           ### this file two  functian

   * Viwer.py
   *       ### this file two  functian


5. static
    * imag
    * payment
    * uploads
    * layout.j
    * model.js
    * script.js
    * search.js
    * style.css
      
7. templates
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


├── src
│   ├── controller
│   │   ├── **/*.css
│   ├── views
│   ├── model
│   ├── index.js
├── public
│   ├── css
│   │   ├── **/*.css
│   ├── images
│   ├── js
│   ├── index.html
├── dist (or build
├── node_modules
├── package.json
├── package-lock.json 
└── .gitignore
