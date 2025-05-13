import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

api_key=os.getenv('API_KEY')
st.title("Movie Recommendation System")

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies_list
)

def fetch_poster(movie_id):
    try:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movie_id,api_key), timeout=5)  
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Image+Available"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=No+Image+Available"


def recommend_movie(movie):
    movie_index = movies[movies["title"]==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]   
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]]["title"])
        # recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]]["movie_id"]))
    return recommended_movies
# , recommended_movies_poster     
if st.button('Show Recommendations'):
    recommended_movies = recommend_movie(selected_movie_name)
    for i in range(len(recommended_movies)):
        st.write(recommended_movies[i])
    
    #below code is not tested as api was slow & there can be some error for fecting movie_id
    # recommended_movies_poster = []
    # for i in range(len(recommended_movies)):
    #     recommended_movies_poster = fetch_poster(movies.iloc[i[0]]["movie_id"])

    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.image(recommended_movies_poster[0])
    #     st.text(recommended_movies[0]) 
    # with col2:
    #     st.image(recommended_movies_poster[1])
    #     st.text(recommended_movies[1])
    # with col3:
    #     st.image(recommended_movies_poster[2])
    #     st.text(recommended_movies[2])
    # with col4:  
    #     st.image(recommended_movies_poster[3])
    #     st.text(recommended_movies[3])
    # with col5: 
    #     st.image(recommended_movies_poster[4])
    #     st.text(recommended_movies[4])
    