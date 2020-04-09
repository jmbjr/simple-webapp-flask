import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def main():
    return jsonify("Johnstein's FancyPants Godot Server!")

@app.route('/leaderboard/')
def get_leaderboard():
    global board
    board = {"LEO":50000, "KRN":45000, "MAY":40000, "KAI":35000, "JUN":30000}
    print(board)
    return jsonify(board)


@app.route('/update', methods = ["POST",])
def update_leaderboard():
    global board
    content = request.json
    new_stuff = content['scores']
    print(new_stuff)
    for d in new_stuff:
        board[d] = new_stuff[d]
    return ("Update OK")

if __name__ == "__main__":
    app.run()


