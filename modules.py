from run import db

class Blogs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_img = db.Column(db.String(150))
    blog_title = db.Column(db.String(50))
    blog_content = db.Column(db.String(150))

class Home(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    home_content = db.Column(db.String(1000))


class Skills (db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skills_img = db.Column(db.String(150))
    skills_title = db.Column(db.String(50))


