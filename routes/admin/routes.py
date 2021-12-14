from run import app
from flask import Flask,flash,redirect,url_for,render_template,request

@app.route("/admin/blog", methods=["GET","POST"])
def blog():
    from modules import Blogs
    import os
    from run import db
    from werkzeug.utils import secure_filename
    blogs = Blogs.query.all()
    if request.method == "POST":
        file = request.files['blog_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/uploads/', filename))
        blog_title = request.form["blog_title"]
        blog_content = request.form["blog_content"]
        blg = Blogs(
            blog_title = blog_title,
            blog_content = blog_content,
            blog_img = os.path.join('static/uploads/', filename),
        )
        db.session.add(blg)
        db.session.commit()
        return redirect ("/admin/blog")
    return render_template("admin/blog.html", blogs=blogs)

@app.route("/blogDelete/<int:id>",methods=["GET","POST"])
def blog_delete(id):
    from modules import Blogs
    import os
    from run import db
    blogs = Blogs.query.filter_by(id=id).first()
    filename = blogs.blog_img
    os.unlink(os.path.join(filename))
    db.session.delete(blogs)
    db.session.commit()
    return redirect ("/admin/blog")
