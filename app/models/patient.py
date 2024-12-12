from app import db


class Patient(db.Model):
    id = db.Column(db.String, primary_key=True)
    data = db.Column(db.JSON, nullable=False)

    def __init__(self, id, data):
        self.id = id
        self.data = data