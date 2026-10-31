from flask import Flask, request

app = Flask(__name__)

TOKEN_VERIFICACION = "mi_token_secreto"


@app.route("/webhook", methods=["GET"])
def verificar():
    if request.args.get("hub.verify_token") == TOKEN_VERIFICACION:
        return request.args.get("hub.challenge")
    return "Token incorrecto", 403


@app.route("/webhook", methods=["POST"])
def recibir():
    datos = request.get_json()
    for entrada in datos.get("entry", []):
        for evento in entrada.get("messaging", []):
            texto = evento.get("message", {}).get("text")
            if texto:
                print("Nuevo mensaje:", texto)
        for cambio in entrada.get("changes", []):
            print("Nueva notificación:", cambio["field"], cambio["value"])
    return "ok", 200


if __name__ == "__main__":
    app.run(port=5000)