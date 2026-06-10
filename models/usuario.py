from extensions import db

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True
    )

    pontos = db.Column(
        db.Integer,
        default=0
    )

    descartes = db.relationship(
        "Descarte",
        backref="usuario",
        lazy=True
    )

    def __repr__(self):
        return f"<Usuario {self.nome}>"