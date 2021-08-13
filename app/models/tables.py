from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Interger, primary_key=True)
    date_log = db.Column(db.DateTime)
    origin = db.Column(db.String)
    destination = db.Column(db.String)
    distance = db.Column(db.String)
    gmaps = db.Column(db.String)
    request_distance = db.Column(db.Text)

    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
