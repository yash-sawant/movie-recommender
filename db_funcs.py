import pandas as pd
from ast import literal_eval
from functools import lru_cache

# Read the movie data CSV file into a Pandas DataFrame
movies_df = pd.read_csv('dataset/25k IMDb movie Dataset.csv')

l = len(movies_df)
movies_df.dropna(subset=['movie title','Generes', 'Overview'],inplace=True)
print('Dropping {} rows for null values'.format(l-len(movies_df)))

movies_df['Generes'] = movies_df['Generes'].apply(literal_eval)

# Clean the movie titles by removing any extra whitespace and converting to lowercase
movies_df['title_lower'] = movies_df['movie title'].apply(lambda x: x.strip().lower())

GENRES = movies_df['Generes'].explode().unique().tolist()

def get_movies():
    return movies_df['movie title'].unique().tolist()