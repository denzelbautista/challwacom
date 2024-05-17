import os

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/shop")
def shop():
    return render_template('shop.html')

@app.route("/vender")
def sell():
    return render_template('product-details.html')

@app.route("/peces")
def fishes():
    return render_template('product-details.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


def main():
    app.run(port=int(os.environ.get('PORT', 3000)), debug=True)

if __name__ == "__main__":
    main()
