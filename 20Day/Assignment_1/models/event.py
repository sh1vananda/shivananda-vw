from db import db
 
class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    total_seats = db.Column(db.Integer)
    available_seats = db.Column(db.Integer)
