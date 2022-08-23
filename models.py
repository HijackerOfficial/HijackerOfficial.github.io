from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

class About_personil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gambar = db.Column(db.String(100), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    Jam = db.Column(db.String(100), nullable=False)

db.create_all()
