from run import app
from flask_login.utils import login_user
from flask import Flask,flash,redirect,url_for,render_template,request
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, logout_user, current_user
from run import login_manager


# Login
@login_manager.user_loader
def load_user(user_id):
    from modules import Login
    return Login.query.get(int(user_id))

@app.route("/admin",methods=["GET","POST"])
def admin_login():
    from modules import Login
    from run import db
    login = Login(
        admin_username = "admin",
        admin_password = "admin",
        log_bool = False
    )
    db.session.add(login)
    db.session.commit()
    
    if request.method == "POST":
        if login.admin_username == request.form["admin_username"] and login.admin_password == request.form["admin_password"]:
            login_user(login, remember=login.log_bool)
            return redirect (url_for("home"))

        else:
            return redirect(url_for("admin_login"))
 
    return render_template("admin/login.html", login = login)

# Logout
@app.route("/logout")
@login_required
def admin_logout():
    logout_user()
    return redirect (url_for("portfolio"))

@app.route("/admin/contact", methods=["GET", "POST"])
def admin_contact():
    from modules import Contact
    from flask_mail import Mail,Message
    from run import db
    from run import mail
    contact=Contact.query.all()
    if request.method=="POST":
        contact_name=request.form["contact_name"]
        contact_email=request.form["contact_email"]
        contact_message=request.form["contact_message"]
        contact_title=request.form["contact_title"]
        salam=Contact(
            contact_name=contact_name,
            contact_message=contact_message,
            contact_email=contact_email,
            contact_title=contact_title
        )
        msg=Message(contact_title, body=contact_message + " " + contact_email + " " + "tərəfindən göndərilmişdir" , sender=contact_email, recipients = ["airbnbaku@gmail.com"])
        mail.send(msg)
        db.session.add(salam)
        db.session.commit()
        return redirect("/")
    return render_template("admin/contact.html", contact=contact)


@app.route("/admin/blog", methods=["GET","POST"])
@login_required
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
        blog_url = request.form["blog_url"]
        blg = Blogs(
            blog_title = blog_title,
            blog_content = blog_content,
            blog_url=blog_url,
            blog_img = os.path.join('static/uploads/', filename),
        )
        db.session.add(blg)
        db.session.commit()
        return redirect ("/admin/blog")
    return render_template("admin/blog.html", blogs=blogs)

@app.route("/blogDelete/<int:id>",methods=["GET","POST"])
@login_required
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


@app.route("/blogEdit/<int:id>",methods=["GET","POST"])
@login_required
def blog_edit(id):
    from modules import Blogs
    from run import db
    newBlogs = Blogs.query.filter_by(id=id).first()
    if request.method=="POST":
        blogs = Blogs.query.filter_by(id=id).first()
        blogs.blog_title = request.form["blog_title"]   
        blogs.blog_content = request.form["blog_content"]
        blogs.blog_url=request.form["blog_url"]
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_blog.html",newBlogs=newBlogs)




@app.route("/admin/home", methods=["GET","POST"])
@login_required
def home():
    from modules import Home
    import os
    from run import db
    from werkzeug.utils import secure_filename
    homes = Home.query.all()
    if request.method == "POST":
        home_content = request.form["home_content"]
        home = Home(
            home_content = home_content,
        )
        db.session.add(home)
        db.session.commit()
        return redirect ("/admin/home")
    return render_template("admin/home.html", homes=homes)

@app.route("/homeDelete/<int:id>",methods=["GET","POST"])
@login_required
def home_delete(id):
    from modules import Home
    from run import db
    homes = Home.query.filter_by(id=id).first()
    db.session.delete(homes)
    db.session.commit()
    return redirect ("/admin/home")

@app.route("/homeUpdate/<int:id>",methods=["GET","POST"])
@login_required
def home_edit(id):
    from modules import Home
    from run import db
    newHome = Home.query.filter_by(id=id).first()
    if request.method=="POST":
        homes = Home.query.filter_by(id=id).first()  
        homes.home_coontent = request.form["home_content"]
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_home.html",newHome=newHome)


@app.route("/admin/skills", methods=["GET","POST"])
@login_required
def skills():
    from modules import Skills
    import os
    from run import db
    from werkzeug.utils import secure_filename
    skills = Skills.query.all()
    if request.method == "POST":
        file = request.files['skills_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/uploads/', filename))
        skills_title = request.form["skills_title"]
        sklls = Skills(
            skills_title = skills_title,
            skills_img = os.path.join('static/uploads/', filename),
        )
        db.session.add(sklls)
        db.session.commit()
        return redirect ("/admin/skills")
    return render_template("admin/skills.html", skills=skills)

@app.route("/skillsDelete/<int:id>",methods=["GET","POST"])
@login_required
def skills_delete(id):
    from modules import Skills
    import os
    from run import db
    skills = Skills.query.filter_by(id=id).first()
    filename = skills.skills_img
    os.unlink(os.path.join(filename))
    db.session.delete(skills)
    db.session.commit()
    return redirect ("/admin/skills")

@app.route("/admin/projects",methods=["GET","POST"])
@login_required
def project():
    from modules import Projects
    import os
    from run import db
    from werkzeug.utils import secure_filename
    projects = Projects.query.all()
    if request.method=="POST":
        file = request.files['project_img']
        filename = secure_filename(file.filename)   
        file.save(os.path.join('static/uploads/', filename))
        project_url = request.form["project_url"]
        prjct = Projects(
            project_url = project_url,
            project_img = os.path.join('static/uploads/', filename),
        )
        db.session.add(prjct)
        db.session.commit()
        return redirect("/")
    return render_template("admin/project.html", projects=projects)

@app.route("/projectDelete/<int:id>",methods=["GET","POST"])
@login_required
def project_delete(id):
    from modules import Projects
    import os
    from run import db
    projects = Projects.query.filter_by(id=id).first()
    filename = projects.project_img
    os.unlink(os.path.join(filename))
    db.session.delete(projects)
    db.session.commit()
    return redirect ("/admin/projects")

