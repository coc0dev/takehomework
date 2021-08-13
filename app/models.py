from app import db
from datetime import datetime

class Divvy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.Integer)
    starttime = db.Column(db.DateTime, default=datetime.utcnow)
    stoptime = db.Column(db.DateTime, default=datetime.utcnow)
    bikeid = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String)
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Column(db.String)
    usertype = db.Column(db.String)
    trip_duration = db.Column(db.Float)

    def __repr__(self):
        return f'{self.starttime}, {self.stoptime}, {self.duration}'