import os
from flask import Flask, request, jsonify
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

application = app = Flask(__name__)
@app.route("/")
def index():
    return ("NBA_SCRAPER")
    
@app.route("/<string:team>", methods = ["GET"])
def getScores(team):
    url = "https://www.cbssports.com/nba/gametracker/boxscore/NBA_20200806_" + team + '/'
    uclient = ureq(url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    scores = page_soup.findAll("div",{"class":"score-text"})
    home_score = scores[0].text
    away_score = scores[1].text
    return jsonify({"home_score":home_score,"away_score":away_score})
    