from flask import Flask, jsonify, request
from model.mysql import DB

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route("/")
def index():
    return jsonify({"message": "hello"})

@app.route("/book/new", methods=["POST"])
def new_book():
    params = request.json
    print(params)
    db = DB()
    db.add(params)
    return jsonify(params)

@app.route("/books")
def books():
    db = DB()
    books = db.findAll()
    return jsonify(books)


if __name__ == "__main__":
    app.run(port=5000)