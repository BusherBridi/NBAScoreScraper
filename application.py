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



@app.route("/schedule", methods = ["GET"])
def getSchedule():
    gameInfo = {}
    url = "https://www.msn.com/en-us/Sports/nba/schedule"
    liveGame = "No Live Games"
    try:
        page_soup = soupify(url)
        liveGame = page_soup.find("div",{"id":"live"}).findAll("td",{"class":"teamname"})
    except:
        number_of_live_games = 0
        gameInfo = {'number_of_live_games':number_of_live_games}
        return gameInfo
    numberOfLiveGames = len(liveGame) / 4
    games = [liveGame[x:x+4] for x in range(0, len(liveGame), 4)]
    i = 0
    for game in games:
        gameInfo[f'game_{i}'] = {'away_team':game[0].text.replace('\n',' '), 'away_abv':game[1].text.replace('\n',' '), 'home_team':game[2].text.replace('\n',' '), 'home_abv':game[3].text.replace('\n',' ')}
        i = i+1
    return jsonify(gameInfo)

