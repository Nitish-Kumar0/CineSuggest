import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=aaf72e4965fb691f4185b549bc169961&language=en-US'
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:9]:
        movie_id = movies.iloc[i[0]].movie_id
        poster_path = fetch_poster(movie_id)
        title = movies.iloc[i[0]].title
        overview = movies_orig.iloc[i[0]].overview
        recommended_movies.append({'poster_path': poster_path, 'title': title, 'overview': overview})

    return recommended_movies

st.header('CineSuggest')
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_orig = pickle.load(open('movie_orig.pkl', 'rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movies = recommend(selected_movie)

    st.subheader('Selected Movie:')
    selected_movie_index = movies[movies['title'] == selected_movie].index[0]
    col1, col2 = st.columns([1, 3])
    col1.image(fetch_poster(movies.iloc[selected_movie_index]['movie_id']))
    col2.write(movies_orig.iloc[selected_movie_index]['overview'])

    st.subheader('Similar Movies:')
    for movie in recommended_movies:
        col1, col2 = st.columns([1, 3])
        col1.image(movie['poster_path'])
        col2.write(f"**{movie['title']}**")
        col2.write(f"**Description:** {movie['overview']}")
