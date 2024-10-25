from flask import Flask, render_template

app = Flask("JobScrapper")

@app.route("/")
def home():
    return "hello world! <a href='/hello'>go to there </a>"

@app.route("/hello")
def hello():
    return render_template("home.html",name="Chanwoo")

app.run(debug=True)