from app import app


@app.route("/pitorrillo")
def index():
    return "pitorrillo!!!1111"


@app.route("/esteban")
def decir_holo():
    return "Holo ejej"
