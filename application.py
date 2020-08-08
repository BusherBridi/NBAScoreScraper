import os
from flask import Flask, request, jsonify
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from datetime import date

application = app = Flask(__name__)
# Function to soupify a page
def soupify(url):
    uclient = ureq(url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup
@app.route("/")
def index():
    return ("NBA_SCRAPER")
    
@app.route("/score/<string:team>", methods = ["GET"])
def getScores(team):
    today = date.today() # Get date now
    url_formated_date = str(today.strftime("%Y%m%d"))
    url = str("https://www.cbssports.com/nba/gametracker/boxscore/NBA_"+url_formated_date+"_" + team + '/')
    page_soup = soupify(url)
    scores = page_soup.findAll("div",{"class":"score-text"})
    home_score = scores[0].text
    away_score = scores[1].text
    return jsonify({"home_score":home_score,"away_score":away_score})


