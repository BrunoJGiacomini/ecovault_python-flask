from models.descarte import Descarte
from models.usuario import Usuario
from extensions import db


class DescarteRepository:

    @staticmethod
    def listar():
        return Descarte.query.all()

    @staticmethod
    def criar(
        usuario_id,
        ecoponto_id,
        material,
        quantidade
    ):

        pontos = quantidade * 10

        descarte = Descarte(
            usuario_id=usuario_id,
            ecoponto_id=ecoponto_id,
            material=material,
            quantidade=quantidade,
            pontos_gerados=pontos
        )

        db.session.add(descarte)

        usuario = Usuario.query.get(usuario_id)

        usuario.pontos += pontos

        db.session.commit()

        return descarte

    @staticmethod
    def total():
        return Descarte.query.count()

    @staticmethod
    def total_pontos():
        descartes = Descarte.query.all()

        total = 0

        for descarte in descartes:
            total += descarte.pontos_gerados

        return total