import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=e023ce971a32e6f2244ddd9c592939be&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f9f9f9, #eaeaea);
        font-family: 'Segoe UI', sans-serif;
        padding: 20px;
        color: #333;
    }

    h1 {
        font-size: 3em;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 40px;
    }

    .card {
        background-color: #fffbea;
        padding: 10px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .card:hover {
        transform: scale(1.03);
        box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    }

    .badge {
        display: block;
        text-align: center;
        background-color: #F5C518;
        color: #000000;
        border-radius: 999px;
        padding: 6px 16px;
        margin-top: 12px;
        font-weight: 600;
        font-size: 14px;
        width: fit-content;
        margin-left: auto;
        margin-right: auto;
    }

    ::-webkit-scrollbar {
        width: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #eaeaea;
    }

    ::-webkit-scrollbar-thumb {
        background: #FF4B4B;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎬 App Title
st.markdown("<h1>🎥 Movie Recommender System</h1>", unsafe_allow_html=True)

# 🎯 Movie selection
option = st.selectbox("🎯 Select a movie you like:", movies_list)

# 🚀 Recommend button
if st.button("🔍 Recommend"):
    names, posters = recommend(option)

    st.markdown("### 🍿 Top 5 Similar Movies:")
    st.markdown("---")

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.image(posters[i], use_container_width=True)
            st.markdown(f"<div class='badge'>{names[i]}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
