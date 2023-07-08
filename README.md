# CineSuggest

CineSuggest is a movie recommendation project that suggests similar movies based on user input. It uses a combination of natural language processing and cosine similarity to determine movie recommendations.

## Overview

The CineSuggest project is designed to provide movie recommendations to users based on a selected movie. It utilizes a dataset containing information about thousands of movies, including their titles, overviews, genres, keywords, cast, and crew. By analyzing these attributes, the project generates a list of similar movies that users may enjoy.

The project consists of two main files:

1. **CineSuggest.py**: This file contains the main code for processing and analyzing the movie dataset. It performs tasks such as data cleaning, feature extraction, cosine similarity calculation, and movie recommendation generation. The processed movie data is saved using the pickle module for later use.

2. **app.py**: This file serves as the user interface for the CineSuggest application. It utilizes the Streamlit library to create a web-based interface where users can select a movie from a dropdown list and view the recommended movies. The movie recommendations are fetched using the processed data from the CineSuggest.py file, and additional information about the movies is retrieved using the TMDB API.

## Dataset

To run the CineSuggest project, you'll need to download the movie dataset files from [TMDB Movie Metadata](https://www.kaggle.com/tmdb/tmdb-movie-metadata) on Kaggle. Please download the following files:

- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

Place these files in the same directory as the project files.

## Libraries Used

The CineSuggest project relies on the following libraries:

- **numpy**: A library for numerical computing in Python.
- **pandas**: A data manipulation library used for handling the movie dataset.
- **ast**: A library for safely evaluating and converting strings containing Python literals.
- **scikit-learn**: A machine learning library that provides various tools for data analysis and modeling. It is used for feature extraction and cosine similarity calculation.
- **nltk**: The Natural Language Toolkit library used for text processing tasks such as stemming.
- **streamlit**: A library for building web applications with Python. It is used to create the user interface for the CineSuggest application.
- **requests**: A library for making HTTP requests. It is used to fetch movie information from the TMDB API.

## Instructions

To use the CineSuggest application, follow these steps:

1. Clone the GitHub repository containing the project files.

2. Make sure you have the required libraries installed. You can use the following command to install them:  `pip install numpy pandas scikit-learn nltk streamlit requests`

3. Run the `CineSuggest.py` file to process the movie dataset and generate the necessary data files (`movie_orig.pkl`, `movie_list.pkl`, and `similarity.pkl`).

4. After the data files are generated, run the `app.py` file to launch the CineSuggest application using Streamlit. The application will be accessible through a web browser.

5. In the web interface, select a movie from the dropdown list or type its name in the input field.

6. Click the "Show Suggestions" button to view the recommended movies. The interface will display the selected movie along with its poster and overview, followed by a list of similar movies with their posters and descriptions.

7. Explore different movies and discover new recommendations!

Please note that the CineSuggest application requires an internet connection to fetch movie information from the TMDB API.




---

With CineSuggest, you can easily find movies similar to your favorites and discover new films that match your interests. Enjoy exploring the world of cinema!
