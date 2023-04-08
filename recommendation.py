import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from db_funcs import movies_df


def get_recommendations(title, rating, genre, year):
    return get_random_movies()


def get_random_movies():
    return movies_df.sample(30)


# Define a function to get a movie's index based on its title
def get_movie_index(title):
    return movies_df[movies_df['movie title'] == title.strip().lower()].index.values[0]


# Define a function to get similar movies based on a movie title
def get_similar_movies(title):
    # Get the index of the movie
    movie_index = get_movie_index(title)

    # Create a CountVectorizer object to transform the movie titles into vectors
    count_vectorizer = CountVectorizer()
    count_matrix = count_vectorizer.fit_transform(movies_df['movie title'])

    # Calculate the cosine similarity between the movie and all other movies
    cosine_similarities = cosine_similarity(count_matrix, count_matrix[movie_index])

    # Get the indices of the 10 most similar movies
    similar_movie_indices = cosine_similarities.argsort(axis=0)[-11:-1][::-1]

    # Get the titles of the similar movies
    similar_movie_titles = [movies_df.iloc[index]['movie title'] for index in similar_movie_indices]

    return similar_movie_titles


if __name__ == '__main__':
    # Get similar movies based on a movie title
    similar_movies = get_similar_movies('The Godfather')

    # Print the similar movies
    print(similar_movies)
