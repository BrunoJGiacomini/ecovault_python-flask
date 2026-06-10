from models.ecoponto import Ecoponto
from extensions import db


class EcopontoRepository:

    @staticmethod
    def listar():
        return Ecoponto.query.all()

    @staticmethod
    def buscar_por_id(id):
        return Ecoponto.query.get(id)

    @staticmethod
    def criar(nome, cidade, endereco, tipo_material):
        ecoponto = Ecoponto(
            nome=nome,
            cidade=cidade,
            endereco=endereco,
            tipo_material=tipo_material
        )

        db.session.add(ecoponto)
        db.session.commit()

        return ecoponto

    @staticmethod
    def atualizar(id, nome, cidade, endereco, tipo_material):
        ecoponto = Ecoponto.query.get(id)

        if ecoponto:
            ecoponto.nome = nome
            ecoponto.cidade = cidade
            ecoponto.endereco = endereco
            ecoponto.tipo_material = tipo_material

            db.session.commit()

        return ecoponto

    @staticmethod
    def excluir(id):
        ecoponto = Ecoponto.query.get(id)

        if ecoponto:
            db.session.delete(ecoponto)
            db.session.commit()

        return ecoponto

    @staticmethod
    def buscar_por_cidade(cidade):
        return Ecoponto.query.filter(
            Ecoponto.cidade.contains(cidade)
        ).all()

    @staticmethod
    def total():
        return Ecoponto.query.count()