# Movie Recommendation System

This is a movie recommendation system built using Flask and Bootstrap and deployed on a Google Cloud Run. The system allows users to input their movie preferences and receive recommendations based on similar movies.

[![Check it out live][run_img]][run_link]

[run_img]: https://storage.googleapis.com/cloudrun/button.svg
[run_link]: https://movie-recommender-pssahwnxxa-pd.a.run.app

The project uses an ensemble of 3 methods to generate weighted scores for similarity to other movies based on user preferences. 
Method 1 applies cosine similarity on BERT-encoded text for 'Overview' with 'Plot Keywords' columns appended, resulting in dense vectors that represent the movies' overviews. 
Method 2 uses CountVectorizer to extract features from the concatenated genre string for each movie, resulting in genre vectors that represent the frequency of genre labels. 
Method 3 uses a character-level CountVectorizer to match input titles with a database of titles, resulting in vector representations that are used to calculate similarity scores. The ensemble of these methods generates weighted scores that can be used to rank movies based on their similarity to the user's preferences. 

## Getting Started

To run the recommendation system, you will need to install Python and the required Python packages. You can do this using `pip` by running the following command:

````
pip install -r requirements.txt
````

Next, you will need to start the Flask server by running the following command:

````
python main.py
````

This will start the server on `http://localhost:5000/`, where you can access the movie recommendation system.

## To deploy this app on Google Cloud
````
gcloud run deploy
````

## Usage

To use the movie recommendation system, enter your movie preferences in the input fields provided. You can rate movies on a scale of 1 to 10 using a slider, select genres from a dropdown list, and enter a release year.

When you submit your preferences, the system will use a machine learning algorithm to recommend similar movies. The results will be displayed in a grid of Bootstrap cards, with each card showing the movie title, runtime, rating, and other relevant details.

You can click on a card to view more information about the recommended movie, including the plot summary, cast and crew, and IMDb link.

## Contributing

If you would like to contribute to the movie recommendation system, please fork the repository and submit a pull request with your changes. We welcome bug reports, feature requests, and code contributions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
