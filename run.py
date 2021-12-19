from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from flask_mail import Mail,Message



app=Flask(__name__)
# UPLOAD_FOLDER = 'static/uploads'
app.secret_key = b'_5#ysdfhsgh"fgdsg\nfgsxec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587   
app.config['MAIL_USERNAME'] = "airbnbaku@gmail.com"
app.config['MAIL_PASSWORD'] = "everythingwillbegood2022"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

db=SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"

from modules import *

#app routes
from routes.app.routes import *

#admin routes
from routes.admin.routes import *

if __name__=='__main__':
    # db.create_all()
    app.run(debug=True)    