import pandas as pd
from ast import literal_eval
from functools import lru_cache

# Read the movie data CSV file into a Pandas DataFrame
movies_df = pd.read_csv('dataset/25k IMDb movie Dataset.csv')

# Clean the movie titles by removing any extra whitespace and converting to lowercase
movies_df['title_lower'] = movies_df['movie title'].apply(lambda x: x.strip().lower())


@lru_cache()
def get_genres():
    return movies_df['Generes'].apply(literal_eval).explode().unique().tolist()

def get_movies():
    return movies_df['movie title'].unique().tolist()