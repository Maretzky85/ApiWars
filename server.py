from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def mainpage():
    return render_template("main.html")


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
