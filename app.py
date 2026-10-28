"""F1 Race Intelligence - Flask app that embeds the Tableau Public dashboard and story.

Run:  pip install -r requirements.txt
      python app.py          then open http://127.0.0.1:5000
Paste your real Tableau Public URLs into config below (leave "" until published).
"""
from flask import Flask, render_template

app = Flask(__name__)

# ---- CONFIG: fill these in after publishing to Tableau Public ----
# Use the view URL WITHOUT "?:..." parameters, e.g.
# https://public.tableau.com/views/YourWorkbook/YourDashboard
DASHBOARD_URL = "https://public.tableau.com/views/F1_Race_Intelligence_17931663228480/F1Dashboard"
STORY_URL = "https://public.tableau.com/views/F1_Race_Intelligence_17931663228480/F1Story"

# ---- ONE project-level link each (shown in the footer and README) ----
DEMO_LINK = ""     # add your demo link
GITHUB_LINK = ""   # add your GitHub link


@app.context_processor
def inject_links():
    return dict(demo_link=DEMO_LINK, github_link=GITHUB_LINK)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", viz_url=DASHBOARD_URL, title="Dashboard")


@app.route("/story")
def story():
    return render_template("story.html", viz_url=STORY_URL, title="Story")


if __name__ == "__main__":
    app.run(debug=True)
