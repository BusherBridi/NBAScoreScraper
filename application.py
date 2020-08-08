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
    now = date.now() # Get date now
    url_formated_date = str(now.strftime("%Y%m%d"))
    url = str("https://www.cbssports.com/nba/gametracker/boxscore/NBA_"+url_formated_date+"_" + team + '/')
    page_soup = soupify(url)
    scores = page_soup.findAll("div",{"class":"score-text"})
    home_score = scores[0].text
    away_score = scores[1].text
    return jsonify({"home_score":home_score,"away_score":away_score})

# @app.route("/standings/<string:standings>", methods = ["GET"])
# def getStandings(standings):
#     url = "https://www.cbssports.com/nba/standings/"
#     page_soup = soupify(url)
#     standings = page_soup.findAll("div", {"class": "TableBase-1"})
    


@app.route("/schedule", methods = ["GET"])
def getSchedule():
    url = "https://www.msn.com/en-us/Sports/nba/schedule"
    liveGame = "No Live Games"
    try:
        page_soup = soupify(url)
        liveGame = page_soup.find("div",{"id":"live"}).findAll("td",{"class":"teamname"})
    except:
        return jsonify({"games":liveGame}), 200
    numberOfLiveGames = len(liveGame) / 4
    games = [liveGame[x:x+4] for x in range(0, len(liveGame), 4)]
    gameInfo = {}
    i = 0
    for game in games:
        gameInfo[i]['away_team']['name'] = game[0]
        # gameInfo[f'game_{i}']['away_team']['abv'] = game[1]
        # gameInfo[f'game_{i}']['home_team']['name'] = game[2]
        # gameInfo[f'game_{i}']['home_team']['abv'] = game[3]
        i = i+1
    return str(gameInfo)
