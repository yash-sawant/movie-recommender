from db_funcs import movies_df as DF, GENRES
import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import re

# Genre Preprocessing
genre_series = DF['Generes'].apply(' '.join)
genre_vectorizer = CountVectorizer()
genre_vectorizer.fit(GENRES)
transformed_genres = genre_vectorizer.transform(genre_series)

# Title Preprocessing
title_vectorizer = CountVectorizer(analyzer="char")
title_vectorizer.fit(DF['movie title'])
transformed_titles = genre_vectorizer.transform(genre_series)


# year processing
def year_func(inp):
    pattern = r"\b\d{4}\b"
    if type(inp) == str:
        y = re.findall(pattern, inp)
        if len(y) > 0:
            return y[0]
    return '0000'


years = DF['year'].apply(year_func)
ignore_year = years == '0000'

# load spacy model
print('Loading spacy...')
# nlp = spacy.load('en_core_web_trf', disable=["tok2vec", "lemmatizer", "tagger", "parser", "ner"])
nlp = spacy.load('en_core_web_md', disable=["lemmatizer", "tagger", "parser", "ner"])
ENCODED_OVERVIEW_PATH = 'dataset/encoded_overview_md.pkl'
with open(ENCODED_OVERVIEW_PATH, "rb") as f:
    transformed_overview = pickle.load(f)
print('spacy data loaded')


# if os.path.exists(ENCODED_OVERVIEW_PATH):
#     with open(ENCODED_OVERVIEW_PATH, "rb") as f:
#         transformed_overview = pickle.load(f)
# if transformed_overview.shape[0] != len(DF):
#     transformed_overview = DF['Overview'].apply(lambda p:nlp(p).vector)
#     with open(ENCODED_OVERVIEW_PATH, "wb") as f:
#         pickle.dump(transformed_overview, f)


def get_recommendations(title, rating, genre, year, top_res=10):
    g_rec_score = genre_similarity(genre)
    o_rec_score = get_overview_recommendation(title)
    t_rec_score = title_similarity(title)
    y_rec_score = year_similarity(year)
    summed_rec_score = 0.23 * o_rec_score + \
                       0.33 * t_rec_score + \
                       0.33 * g_rec_score + \
                       0.1 * y_rec_score


    rec_idx = np.argsort(summed_rec_score)[-top_res:][::-1]
    return DF.iloc[rec_idx, :]


def year_similarity(year):
    global years, ignore_year
    score = years == year
    score = score.astype(int)
    score[ignore_year] = 0
    return score


def get_overview_recommendation(title):
    global transformed_overview, nlp
    movie_idx = get_movie_index(title)
    input_overview = DF.loc[movie_idx, 'Overview']
    transformed_input = nlp(input_overview).vector.reshape((1, -1))
    similarity_scores = cosine_similarity(transformed_input, transformed_overview).reshape((-1))
    similarity_scores[movie_idx] = 0
    return similarity_scores


def title_similarity(title):
    global transformed_titles, DF
    input_arr = genre_vectorizer.transform([title])
    similarity_scores = cosine_similarity(input_arr, transformed_titles).reshape((-1))
    return similarity_scores


def genre_similarity(input_list):
    global transformed_genres, DF
    input_arr = genre_vectorizer.transform([' '.join(input_list)])
    similarity_scores = cosine_similarity(input_arr, transformed_genres).reshape((-1))

    return similarity_scores


def get_random_movies():
    return DF.sample(30)


# Define a function to get a movie's index based on its title
def get_movie_index(title):
    return DF[DF['title_lower'] == title.strip().lower()].index.values[0]


if __name__ == '__main__':
    title = 'The Godfather'
    rating = None
    genre = ['Adult', 'Action']
    year = 2022

    similar_movies = get_recommendations(title, rating, genre, year)

    # Print the similar movies
    print(similar_movies)
