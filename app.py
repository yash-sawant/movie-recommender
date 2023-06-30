import os
from ast import literal_eval
from flask import Flask, render_template, request, jsonify
from db_funcs import GENRES, get_movies
from datetime import datetime
from recommendation import get_recommendations
import re
app = Flask(__name__)

movies = get_movies()

IMDB_PREFIX = 'https://www.imdb.com/'

@app.route("/")
def home():
    genres = GENRES
    current_year = datetime.now().year
    return render_template('home.html', genres=genres, current_year=current_year)


@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('query')
    results = []
    for movie in movies:
        if query.lower() in movie.lower():
            results.append(movie)
    return jsonify(results)


@app.route('/recommendations', methods=['POST'])
def index():
    movie_title = request.form['movie_search']
    movie_rating = request.form['movie_rating']
    movie_genre = request.form.getlist('movie_genre')
    movie_year = request.form['movie_year']
    rec_movies = get_recommendations(movie_title, movie_rating, movie_genre, movie_year)
    formatted_movies = format_movies_df(rec_movies)

    return render_template('results.html', movies=formatted_movies)


def format_movies_df(df):
    res = []
    pattern = r"\b\d{4}\b"
    for i, row in df.iterrows():
        if type(row['year']) == str:
            year = re.findall(pattern, row['year'])[0]
        else:
            year = 'Unknown'
        genre = row['Generes']
        mov_dict = {'title': row['movie title'],
                    'description': row['Overview'],
                    'year':year,
                    'genre': ', '.join(genre),
                    'link': IMDB_PREFIX + row['path']
                    # 'poster':,
                    }
        res.append(mov_dict)
    return res


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
