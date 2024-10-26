from flask import Flask, render_template, request
from practice1 import scraping



app = Flask("JobScrapper")

@app.route("/")
def home():
    return "hello world! <a href='/hello'>go to there </a>"

@app.route("/hello")
def hello():
    return render_template("home.html",name="Chanwoo")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = scraping(keyword)
    return render_template("search.html", keyword = keyword ,jobs = jobs)

app.run(debug=True)