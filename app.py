from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_nerds():
    return "<p>Hello Nerds here I am again!! Auto refresh please please please!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
