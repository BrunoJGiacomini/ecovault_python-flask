from extensions import db



class Ecoponto(db.Model):
    __tablename__ = "ecopontos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    cidade = db.Column(
        db.String(100),
        nullable=False
    )

    endereco = db.Column(
        db.String(200),
        nullable=False
    )

    tipo_material = db.Column(
        db.String(100),
        nullable=False
    )

    descartes = db.relationship(
        "Descarte",
        backref="ecoponto",
        lazy=True
    )

    def __repr__(self):
        return f"<Ecoponto {self.nome}>"