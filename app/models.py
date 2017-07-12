from app import db

class Snacks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    snackname = db.Column(db.String(64))
    out = db.Column(db.Boolean)
    location = db.Column(db.String(64))
    bumps = db.Column(db.Integer)


    def __init__(self, name):
        self.snackname = name
        self.bumps = 0
        self.out = True
        self.location = "Other"
