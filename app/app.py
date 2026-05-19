from flask import Flask, request, jsonify
import mysql.connector
import time

app = Flask(__name__)

def get_db():
    # tenta conectar até o mysql subir
    for _ in range(10):
        try:
            return mysql.connector.connect(
                host="mysql-cp3",
                user="root",
                password="123456",
                database="dimdim"
            )
        except:
            time.sleep(2)
    raise Exception("Erro ao conectar no MySQL")

@app.route("/")
def home():
    return "API CP3 rodando!"

# CREATE
@app.route("/produtos", methods=["POST"])
def create():
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO produtos (nome, preco) VALUES (%s, %s)",
        (data["nome"], data["preco"])
    )
    db.commit()

    return jsonify({"msg": "Produto criado"})

# READ
@app.route("/produtos", methods=["GET"])
def read():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM produtos")
    result = cursor.fetchall()

    return jsonify(result)

# UPDATE
@app.route("/produtos/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE produtos SET nome=%s, preco=%s WHERE id=%s",
        (data["nome"], data["preco"], id)
    )
    db.commit()

    return jsonify({"msg": "Produto atualizado"})

# DELETE
@app.route("/produtos/<int:id>", methods=["DELETE"])
def delete(id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM produtos WHERE id=%s", (id,))
    db.commit()

    return jsonify({"msg": "Produto deletado"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)