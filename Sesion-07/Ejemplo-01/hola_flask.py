from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Soy la página de inicio creada desde Flask</h2>"

@app.route("/pagina")
def pagina():
    return render_template("pagina.html")


if __name__ == "__main__":
    app.run(debug=True)

