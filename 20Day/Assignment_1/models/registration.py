from db import db
 
class Registration(db.Model):
    __tablename__ = "registrations"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))