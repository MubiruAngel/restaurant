from flask import Flask,render_template,url_for,redirect
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact",methods = ['GET','POST'])
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/online")
def tonline():
    return render_template("online.html")                     




if __name__==("__main__"):
    app.run(debug=True)
