# from flask.templating import render_template
from flask import render_template, request, redirect
from app import app
from models.calendar import events, add_new_event
from models.event import Event
# import datetime

@app.route('/')
def index():
    return render_template("index.html", title="Homepage")

@app.route('/listofevents')
def allevents():
    return render_template("events.html", title="Events", list_of_events = events)

# @app.route('/addevent')
# def show_form():
#     return render_template("addevent.html", title="Add event", list_of_events = events)

@app.route('/listofevents', methods=['POST'])
def create():
    print(request.form)
    event_date = request.form['date']
    # split_date = event_date.split('-')
    # date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    event_name = request.form['name']
    event_guests = request.form['guests']
    event_location = request.form['room']
    event_description = request.form['description']
    # event_recurring = request.form['recurring']

    new_event = Event(event_date, event_name, event_guests, event_location, event_description, True)
    add_new_event(new_event)

    return redirect('/listofevents')