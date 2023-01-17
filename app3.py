from flask import Flask, request, jsonify
app = Flask(__name__)


@app.post('/post_num')
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    return jsonify({'result': a + b})


if __name__ == '__main__':
    app.run(debug=True)

