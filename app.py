from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def root():
    data = request.get_json()
    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
