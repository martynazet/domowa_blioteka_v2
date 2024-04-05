# -*- coding: utf-8 -*
from flask import Flask, jsonify, abort, make_response, request
from models_biblioteka import library

app = Flask(__name__)
app.config["SECRET_KEY"] = "hatemondays"

@app.route("/api/v1/library/", methods=["GET"])
def library_list_api():
    return jsonify(library.all())

@app.route("/api/v1/library/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = library.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book": book})

@app.route("/api/v1/library/", methods=["POST"])
def create_book():
    if not request.json or not "title" in request.json:
        abort(400)
    book = {
        "id": library.all()[-1]["id"] + 1,
        "title": request.json["title"],
        "author": request.json["author"],
        "genre": request.json["genre"],
        "pages": request.json["pages"],
        "read": False
    }
    library.create(book)
    return jsonify({"book": book}), 201

@app.route("/api/v1/library/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = library.get(book_id)
    result = library.delete(book_id)
    if result:
        return jsonify({"result": f"Usunięto {book["title"]}"})
    else:
        abort(404)
    
@app.route("/api/v1/library/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = library.get(book_id)
    if not book:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        "title" in data and not isinstance(data.get("title"), str),
        "author" in data and not isinstance(data.get("author"), str),
        "genre" in data and not isinstance(data.get("genre"), str),
        "pages" in data and not isinstance(data.get("pages"), int),
        "read" in data and not isinstance(data.get("read"), bool)
    ]):
        abort(400)
    book = {
        "title": data.get("title", book["title"]),
        "author": data.get("author", book["author"]),
        "genre": data.get("genre", book["genre"]),
        "pages": data.get("pages", book["pages"]),
        "read": data.get("read", book["read"])
    }
    library.update(book_id, book)
    return jsonify({"book": book})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "status_code": 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request", "status_code": 400}), 400)



if __name__ == "__main__":
    app.run(debug=True)