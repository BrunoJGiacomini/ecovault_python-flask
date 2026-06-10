from flask import Blueprint, render_template, request, redirect, flash
from repositories.usuario_repository import UsuarioRepository

usuario_bp = Blueprint(
    "usuarios",
    __name__,
    url_prefix="/usuarios"
)


@usuario_bp.route("/")
def listar():
    usuarios = UsuarioRepository.listar()
    return render_template("usuarios/listar.html", usuarios=usuarios)


@usuario_bp.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        UsuarioRepository.criar(nome, email)

        flash("Usuário cadastrado com sucesso!", "success")
        return redirect("/usuarios")

    return render_template("usuarios/novo.html")


@usuario_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    usuario = UsuarioRepository.buscar_por_id(id)

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        UsuarioRepository.atualizar(id, nome, email)

        flash("Usuário atualizado com sucesso!", "success")
        return redirect("/usuarios")

    return render_template("usuarios/editar.html", usuario=usuario)


@usuario_bp.route("/excluir/<int:id>")
def excluir(id):
    UsuarioRepository.excluir(id)

    flash("Usuário excluído com sucesso!", "success")
    return redirect("/usuarios")

@usuario_bp.route("/ranking")
def ranking():

    usuarios = UsuarioRepository.ranking()

    return render_template(
        "usuarios/ranking.html",
        usuarios=usuarios
    )