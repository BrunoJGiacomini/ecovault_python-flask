from models.usuario import Usuario
from extensions import db


class UsuarioRepository:

    @staticmethod
    def listar():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(id):
        return Usuario.query.get(id)

    @staticmethod
    def criar(nome, email):
        usuario = Usuario(nome=nome, email=email)
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def atualizar(id, nome, email):
        usuario = Usuario.query.get(id)

        if usuario:
            usuario.nome = nome
            usuario.email = email
            db.session.commit()

        return usuario

    @staticmethod
    def excluir(id):
        usuario = Usuario.query.get(id)

        if usuario:
            db.session.delete(usuario)
            db.session.commit()

        return usuario

    @staticmethod
    def ranking():
        return Usuario.query.order_by(
            Usuario.pontos.desc()
        ).all()

    @staticmethod
    def total():
        return Usuario.query.count()