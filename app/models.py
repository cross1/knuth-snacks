from app import db

class Snacks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    snackname = db.Column(db.String(64))


    def __init__(self, name):
        self.snackname = name
