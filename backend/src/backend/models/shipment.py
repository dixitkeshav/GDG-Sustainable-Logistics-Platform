from backend.app import db

class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(200), nullable=False)
    destination = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default="Pending")

    def __repr__(self):
        return f"<Shipment {self.id} - {self.status}>"
