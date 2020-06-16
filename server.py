from time import sleep
from random import randint

from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/api/lowercase/<string:word>', methods=['GET'])
def get_task(word):
    sleep(randint(1, 3))
    return jsonify({'task': word.lower()})


@app.route('/')
def live():
    return "I'm alive!"

if __name__ == '__main__':
    app.run()