from run import app
from flask import Flask,redirect,url_for,render_template,request
@app.route("/")
def portfolio():
    from modules import Blogs
    blogs = Blogs.query.all()
    return render_template("app/index.html", blogs=blogs)