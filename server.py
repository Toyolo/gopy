from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from game import Game

app = Flask(__name__)
socketio = SocketIO(app)

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('place_stone')
def handle_place_stone(json):
    x = json['x']
    y = json['y']
    color = json['color']
    game.place_stone(x, y, color)
    emit('update_score', game.end_game(), broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
