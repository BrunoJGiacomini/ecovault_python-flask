from extensions import db
from datetime import datetime


class Descarte(db.Model):
    __tablename__ = "descartes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=False
    )

    ecoponto_id = db.Column(
        db.Integer,
        db.ForeignKey("ecopontos.id"),
        nullable=False
    )

    material = db.Column(
        db.String(100),
        nullable=False
    )

    quantidade = db.Column(
        db.Integer,
        nullable=False
    )

    pontos_gerados = db.Column(
        db.Integer,
        default=0
    )

    data = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )