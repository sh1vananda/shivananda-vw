from flask import Blueprint, request, render_template, redirect, url_for
from db import db
from models.event import Event
from models.registration import Registration
 
events_bp = Blueprint("events", __name__)
 
 
@events_bp.route("/")
def home():
    events = Event.query.all()
    return render_template("events.html", events=events)
 
@events_bp.route("/events", methods=["POST"])
def create_event():
    name = request.form.get("name")
    total_seats = int(request.form.get("total_seats"))
    event = Event(
        name=name,
        total_seats=total_seats,
        available_seats=total_seats
    )
    db.session.add(event)
    db.session.commit()
    return redirect(url_for("events.home"))
 
@events_bp.route("/register/<int:event_id>", methods=["POST"])
def register(event_id):
    user_name = request.form.get("user_name")
    event = Event.query.get(event_id)
    if event.available_seats == 0:
        return "Event Full"
    reg = Registration(
        user_name=user_name,
        event_id=event_id
    )
    event.available_seats -= 1
    db.session.add(reg)
    db.session.commit()
    return redirect(url_for("events.home"))
 