from flask import Flask,jsonify,request
from flask_basicauth import BasicAuth
app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] ='username'
app.config['BASIC_AUTH_PASSWORD'] ='password'
basic_auth = BasicAuth(app)


books = [
    {"id" :1 , "title" : "Book 1" , "author" :"Author 1"},
    {"id" :2 , "title" : "Book 2" , "author" :"Author 2"},
    {"id" :3 , "title" : "Book 3" , "author" :"Author 3"}
]
@app.route("/")
def Greet():
    return "<p>Welcome to Book Management System</p>"

@app.route("/books",methods = ["GET"])
@basic_auth.required
def get_all_book():
    return jsonify({"books":books})

@app.route("/books/<int:book_id>",methods = ["GET"])
@basic_auth.required
def get_id_book(book_id):
    book = next( (b for b in books if b["id"] == book_id),None)
    
    # obj_book = jsonify(book) if book else jsonify({"error":"Book not found"}),404
    # return obj_book

    if book:
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}),404
    
@app.route("/books/",methods = ["POST"])
@basic_auth.required
def create_book():
    data = request.get_json()
    new_book={
        "id":len(books)+1,
        "title":data["title"],
        "author":data["author"]
    }
    books.append(new_book)
    return jsonify(new_book),201

@app.route("/books/<int:book_id>",methods = ["PUT"])
@basic_auth.required
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id),None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error":"Book not found"}),404
    
@app.route("/books/<int:book_id>",methods =["DELETE"])
@basic_auth.required
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message":"Books deleted successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
