
from datetime import date
from flask import Flask,render_template

app=Flask(__name__)
data="Mən Azərbaycanlı veb developer namizədiyəm. Bu günə qədər hər zaman arxasıyca qaçdığım, həmişə marağında olduğum peşə məhz bu idi. İnşallah arzuladığım həyata bu yol ilə sahib olacağam."
lang="WEB DEVELOPER"


def calculateAge(birthDate=date(1995, 10, 21)):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
years=calculateAge()     


@app.route('/')
def index ():
    return render_template("index.html",data=data,lang=lang)

@app.route('/blog')
def blog ():
    return render_template("blog.html")

@app.route('/brief')
def brief ():
    return render_template("brief.html")

@app.route('/about')
def about ():
    return render_template("about.html",years=years)

@app.route('/contact2')
def contact2 ():
    return render_template("contact2.html")


if __name__ == '__main__':
    app.run(debug=True)