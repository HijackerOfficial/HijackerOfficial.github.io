from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import models

app = Flask(__name__) # untuk memetakan folder
app.config['SECRET_KEY'] = '3618ggdhagGHF7F6ffhdsj6##8e20'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/band'
db = SQLAlchemy(app)

@app.route("/") #untuk memetakan url
def hello_world(): #untuk membuat fuction yang berisi program / website
    return render_template("hijacker.html")

@app.route("/about_personil")
def about_personil():
    return render_template("about personil.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about_label")
def about_label():
    return render_template("about label.html")

@app.route("/galerry")
def galerry():
    return render_template("galerry.html")

@app.route("/dashboard")
def dashboard():
    return render_template("admin.html")

if __name__  == '__main__': #untuk menjalankan program secara otomatis 
    app.run(debug=True) # jalankan semua program / website
