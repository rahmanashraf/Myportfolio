from run import db

class Blogs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_img = db.Column(db.String(150))
    blog_title = db.Column(db.String(50))
    blog_content = db.Column(db.String(150))


