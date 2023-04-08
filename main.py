import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)


@app.route('/recommendations', methods=['POST'])
def index():
    if request.method == 'POST':
        movie_rating = request.form['movie_rating']
        movie_genre = request.form['movie_genre']
        movie_year = request.form['movie_year']
        # Do something with the form data, like query a database or API for movie recommendations
        return render_template('movie_results.html')
    else:
        genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Romance', 'Thriller']
        current_year = 2023
        return render_template('results.html', genres=genres, current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))