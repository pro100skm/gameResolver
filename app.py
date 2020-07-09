from flask import Flask, jsonify, request
from forWeb import run_threads

app = Flask(__name__)


@app.route('/')
def hello_world():

    return jsonify(run_threads('ывфапкрвмсыпеаимсваоцывак'))


@app.route('/api/', methods=['POST'])
def solve():
    print(request.data.decode(encoding='utf8'))
    # return jsonify(run_threads('ывфапкрвмсыпеаимсваоцывак')), 200
    res = jsonify(run_threads(request.data.decode(encoding='utf8')))
    return res, 200



if __name__ == '__main__':
    app.run()
