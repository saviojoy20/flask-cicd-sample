from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<center><h1>Flaskyuu Adrgrpplication Version1.6uiyu66666666666/h1></center>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
