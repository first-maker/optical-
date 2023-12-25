# optical-
install python 
install vs code
 https://www.python.org/downloads/

https://code.visualstudio.com/
     
<!-- in c direct install pip -->
pip install pip
<!-- to upgrade pip -->
python.exe -m pip install --upgrade pip

<!-- flask install  -->
pip install Flask

<!-- to use cs50 for sqlite -->
pip install cs50 

<!-- to icnstall Session libary -->
-- pip install Flask-Session

pip install python-dotenv
<!-- install pytz -->
pip install pytz

<!-- to handell cash -->
pip install Flask-Caching  
  pip install -U flask-caching   
<!-- install email  -->
pip install Flask-Mail
from flask_mail import Mail, Message
import flask

<!--add  dotenv to make .env file -->
pip install dotenv
pip install python-dotenv
py -m venv new_environment
<!-- Adding and configuring virtualenv [optional]
Then, launch the terminal and head to the folder you’ll use for this project. Type in the following. -->
  py -m venv new_environment 
  <!-- add env file -->
$ python3 -m venv venv # use `virtualenv venv` on Python 2
source venv/bin/activate
 
% how import libary   email
from config import app, mail
from mailbox import Message






% <!-- to work flask with depage  -->
flask --app  app.py --debug run

% add uponta
% https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview

% wsl --install

% % Installation of WSL from the Microsoft Store

% or Windows Subsystem for Linux 

% 3. Download Ubuntu from the Microsoft Store
% Install Ubuntu from the command line
% wsl --list --online to see all available distros.

% wsl --install -d Ubuntu-20.04


% Use wsl -l -v to see all your currently installed distros and which version of WSL they are using:
% sudo apt update
% sudo apt full-upgrade
% sudo apt install x11-apps


% sudo apt install octave
% octave --gui &

% /in opunto
apt install sqlite3

% 
pip install numpy

project
├── app
│   └── folder
│       └── file.py
└── pyFile
│        └── brand.py
│        └── 
└── static
│    │
│    └──imag
│    │    └── media img 
│    └── uploads
│    │   └── uplded files 
│    └──script.js
│    └──styles.css
    
         



% mysql
pip install pyproject-toml
pip install flask-mysqldb 

pip install pymysql

pip install python-time


pip install pycountry

pip install geopy


 pip install flask-qrcode

  pip3 install pywhatkit 

  # Your Flask Project Name

Brief description or introduction to your Flask project.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Explain the purpose of your Flask project and its main features briefly.

## Installation

Provide instructions on how to install your project:

1. Clone the repository: `git clone https://github.com/yourusername/your-project.git`
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage

Explain how to use/run your Flask project:

1. Set environment variables if needed.
2. Run the Flask application:
   ```bash
   python app.py
