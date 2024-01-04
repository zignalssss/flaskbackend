from flask import Flask,jsonify

app = Flask(__name__)
books = [
    {"id" :1 , "title" : "Book 1" , "author" :"Author 1"},
    {"id" :2 , "title" : "Book 2" , "author" :"Author 2"},
    {"id" :3 , "title" : "Book 3" , "author" :"Author 3"}
]
@app.route("/")
def Greet():
    return "<p>Welcome to Book Management System</p>"

@app.route("/books",methods = ["GET"])
def get_all_book():
    return jsonify({"books":books})

@app.route("/books/<int:book_id>",methods = ["GET"])
def get_id_book(book_id):
    book = next( (b for b in books if b["id"] == book_id),None)
    obj_book = jsonify(book) if book else jsonify({"error":"Book not found"}),404
    return obj_book

    # if(book):
    #     return jsonify(book)
    # else:
    #     return jsonify({"error":"Book not found"}),404

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)