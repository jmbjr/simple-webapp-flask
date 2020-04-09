import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


board_base = {"LEO":50000, "KRN":45000, "MAY":40000, "KAI":35000, "JUN":30000}

@app.route("/")
def main():
    return jsonify("Johnstein's FancyPants Godot Server!")

@app.route('/reset/')
def reset():
    global board
    board = board_base
    save_leaderboard()
    return('Reset Board OK')

@app.route('/leaderboard/')
def get_leaderboard():
    #global board
    #board = {"LEO":50000, "KRN":45000, "MAY":40000, "KAI":35000, "JUN":30000}
    #print(board)
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


def save_leaderboard():
    print("saving")
    with open('leaderboard.json', 'w') as outfile:
        json.dump(board,outfile)

def load_leaderboard():
    print("loading")
    with open('leaderboard.json') as json_file:
        global board
        board = json.load(json_file)

if __name__ == "__main__":
    reset()
    load_leaderboard()
    app.run()


