from flask import Blueprint, render_template, request, redirect, flash
from repositories.descarte_repository import DescarteRepository
from repositories.usuario_repository import UsuarioRepository
from repositories.ecoponto_repository import EcopontoRepository

descarte_bp = Blueprint(
    "descartes",
    __name__,
    url_prefix="/descartes"
)


@descarte_bp.route("/")
def listar():

    descartes = DescarteRepository.listar()

    return render_template(
        "descartes/listar.html",
        descartes=descartes
    )


@descarte_bp.route("/novo", methods=["GET", "POST"])
def novo():

    usuarios = UsuarioRepository.listar()
    ecopontos = EcopontoRepository.listar()

    if request.method == "POST":

        usuario_id = int(request.form["usuario_id"])
        ecoponto_id = int(request.form["ecoponto_id"])
        material = request.form["material"]
        quantidade = int(request.form["quantidade"])

        DescarteRepository.criar(
            usuario_id,
            ecoponto_id,
            material,
            quantidade
        )

        flash(
            "Descarte registrado com sucesso!",
            "success"
        )

        return redirect("/descartes")

    return render_template(
        "descartes/novo.html",
        usuarios=usuarios,
        ecopontos=ecopontos
    )