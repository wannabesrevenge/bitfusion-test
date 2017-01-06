import flask

app = flask.Flask(__name__)
hello_res = {"response":"hello world"}

@app.route("/hello")
def hello():
    return flask.jsonify(**hello_res)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8888)
