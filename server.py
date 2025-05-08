from datetime import datetime
import json
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    if len(club) == 0:
        flash('Email not found')
    else:
        club = club[0]
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    foundClub = [c for c in clubs if c['name'] == club][0]
    dateFoundCompettion = datetime.strptime(foundCompetition['date'], '%Y-%m-%d %H:%M:%S')
    if dateFoundCompettion < datetime.now():
        flash('The competition is already finished')
    else:
        if foundClub and foundCompetition:
            return render_template('booking.html', club=foundClub, competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
    return render_template('welcome.html', club=foundClub, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired > 12:
        flash("You can't take more than 12 places")
    else:
        if placesRequired <= int(club['points']):
            club['points'] = int(club['points']) - placesRequired
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            flash('Great-booking complete!')
        else:
            flash("You don't have enough point")
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/scoreboard')
def scoreboard():
    return render_template('scoreboard.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
