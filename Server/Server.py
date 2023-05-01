from flask import Flask, render_template


app = Flask(__name__, template_folder='../templates')


@app.route("/")
@app.route("/home")
@app.route("/Home")
def home():
    return render_template('Home.html')


@app.route("/test")
def test():
    return render_template('Test.html')


if __name__ == "__main__":
    app.run(debug=True)
