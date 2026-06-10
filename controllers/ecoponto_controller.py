from flask import Blueprint, render_template, request, redirect, flash
from repositories.ecoponto_repository import EcopontoRepository

ecoponto_bp = Blueprint(
    "ecopontos",
    __name__,
    url_prefix="/ecopontos"
)


@ecoponto_bp.route("/")
def listar():

    cidade = request.args.get("cidade")

    if cidade:
        ecopontos = EcopontoRepository.buscar_por_cidade(cidade)
    else:
        ecopontos = EcopontoRepository.listar()

    return render_template(
        "ecopontos/listar.html",
        ecopontos=ecopontos
    )


@ecoponto_bp.route("/novo", methods=["GET", "POST"])
def novo():

    if request.method == "POST":

        nome = request.form["nome"]
        cidade = request.form["cidade"]
        endereco = request.form["endereco"]
        tipo_material = request.form["tipo_material"]

        EcopontoRepository.criar(
            nome,
            cidade,
            endereco,
            tipo_material
        )

        flash("Ecoponto cadastrado com sucesso!", "success")

        return redirect("/ecopontos")

    return render_template(
        "ecopontos/novo.html"
    )

@ecoponto_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    ecoponto = EcopontoRepository.buscar_por_id(id)

    if request.method == "POST":

        nome = request.form["nome"]
        cidade = request.form["cidade"]
        endereco = request.form["endereco"]
        tipo_material = request.form["tipo_material"]

        EcopontoRepository.atualizar(
            id,
            nome,
            cidade,
            endereco,
            tipo_material
        )

        flash(
            "Ecoponto atualizado com sucesso!",
            "success"
        )

        return redirect("/ecopontos")

    return render_template(
        "ecopontos/editar.html",
        ecoponto=ecoponto
    )

@ecoponto_bp.route("/excluir/<int:id>")
def excluir(id):

    EcopontoRepository.excluir(id)

    flash(
        "Ecoponto excluído com sucesso!",
        "success"
    )

    return redirect("/ecopontos")