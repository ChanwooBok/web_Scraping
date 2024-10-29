from flask import Flask, render_template, request
from practice1 import scraping



app = Flask("JobScrapper")


db = {}


@app.route("/")
def home():
    return "hello world! <a href='/hello'>go to there </a>"

@app.route("/hello")
def hello():
    return render_template("home.html",name="Chanwoo")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
        print("this keyword is already in the db")
    else:
        jobs = scraping(keyword)
        db[keyword] = jobs
        print("db is updated and db is ",db)
    return render_template("search.html", keyword = keyword ,jobs = jobs)

app.run(debug=True)