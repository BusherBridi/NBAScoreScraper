import os
from flask import Flask, request, jsonify
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from datetime import date

application = app = Flask(__name__)

# Function to soupify a page
def soupify(url):
@app.route("/")
def index():
    return ("NBA_SCRAPER")
    
@app.route("/score/<string:team>", methods = ["GET"])
def getScores(team):
    today = date.today() # Get today's date
    url_formated_date = today.strftime("%Y%m%d")
    url = "https://www.cbssports.com/nba/gametracker/boxscore/NBA_"+url_formated_date+"_" + team + '/'

    uclient = ureq(url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")
    return page_soup


@app.route("/score/<string:team>", methods = ["GET"])
def getScores(team):
    url = "https://www.cbssports.com/nba/gametracker/boxscore/NBA_20200806_" + team + '/'
    page_soup = soupify(url)
    scores = page_soup.findAll("div",{"class":"score-text"})
    home_score = scores[0].text
    away_score = scores[1].text
    return jsonify({"home_score":home_score,"away_score":away_score})

# @app.route("/schedule", methods = ["GET"])
# def getSchedule():
#     url = "https://www.msn.com/en-us/Sports/nba/schedule"
#     liveGame = "No Live Games"
#     try:
#         page_soup = soupify(url)
#         liveGame = page_soup.find("div",{"id":"live"}).findAll("td",{"class":"teamname"})
#     except:
#         return jsonify({"games":liveGame}), 200
#     numberOfLiveGames = len(liveGame) / 4
#     it = iter(liveGame)
#     onGoingGames = {}
#     gameId = 0
#     for x in it:
#         onGoingGames = {""}
#    # return str(liveGame[0].div.text)
#     return str(liveGame)
