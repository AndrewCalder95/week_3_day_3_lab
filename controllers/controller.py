from flask.templating import render_template
from flask import render_template, request, redirect
from app import app
from models.calendar import events
from models.event import Event
#from models.calendar import METHOD

@app.route('/')
def index():
    return render_template("index.html", title="Homepage")

@app.route('/listofevents')
def allevents():
    return render_template("events.html", title="Events", list_of_events = events)

# @app.route('/addevent')
# def add_event():
#     return "Add event"