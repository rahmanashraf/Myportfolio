from run import db
from flask_login.mixins import UserMixin


class Blogs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_img = db.Column(db.String(150))
    blog_title = db.Column(db.String(50))
    blog_url = db.Column(db.Text)
    blog_content = db.Column(db.String(150))

class Home(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    home_content = db.Column(db.String(1000))


class Skills (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skills_img = db.Column(db.String(150))
    skills_title = db.Column(db.String(50))

class Projects(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    project_url = db.Column(db.Text)
    project_img = db.Column(db.String(100))

# Login
class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)

class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_name = db.Column(db.String(100))
    contact_email = db.Column(db.String(100))
    contact_title= db.Column(db.String(100))
    contact_message = db.Column(db.Text)

