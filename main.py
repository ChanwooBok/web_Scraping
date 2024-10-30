from flask import Flask, render_template, request, redirect, send_file
from practice1 import scraping
from file import save_to_file


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
    return render_template("search.html", keyword = keyword ,jobs = jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword is None:
        return redirect("/")
    if keyword not in db:
        print("keyword is not in db")
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run(debug=True)