from flask import Flask, request, render_template
from views.products import product_app


app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")


@app.route("/")
def main_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="localhost",
        port=5000,
        debug=True,
    )
