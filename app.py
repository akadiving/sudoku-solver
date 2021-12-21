from flask import Flask, jsonify, request
from tasks import solve_puzzle

app = Flask(__name__)

@app.route('/', methods=['POST'])
def solve_sudoku():
    result = request.get_json()
    task = solve_puzzle.apply_async(result['grid'])
    return jsonify(task.id)

@app.route('/status/<task_id>', methods=['GET'])
def taskstatus(task_id):
    task = solve_puzzle.AsyncResult(task_id)
    return jsonify(task.state)

if __name__ == '__main__':
    app.run(debug = True)