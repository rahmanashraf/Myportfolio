from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
app.secret_key = b'_5#ysdfhsgh"fgdsg\nfgsxec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

from modules import *

#app routes
from routes.app.routes import *

#admin routes
from routes.admin.routes import *

if __name__=='__main__':
    # db.create_all()
    app.run(debug=True)    