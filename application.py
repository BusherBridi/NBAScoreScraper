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
    return(url) 
    # page_soup = soupify(url)
    # scores = page_soup.findAll("div",{"class":"score-text"})
    # home_score = scores[0].text
    # away_score = scores[1].text
    # return jsonify({"home_score":home_score,"away_score":away_score})

@app.route("/standings/<string:standings>", methods = ["GET"])
def getStandings(standings):
    url = "https://www.cbssports.com/nba/standings/"
    page_soup = soupify(url)
    standings = page_soup.findAll("div", {"class": "TableBase-1"})
    


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
