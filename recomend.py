import pickle
import streamlit as st
import pandas as ps
import math
import matplotlib.pyplot as plt
import random

st.header("Movie recomendation using machine Learning")
movies = pickle.load(open('files/movielst.pkl','rb'))
similar = pickle.load(open('files/similar.pkl','rb'))

def recomend(movie):
    index = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similar[index])),reverse=True,key=lambda x: x[1])
    rec_movies = []
    rec_poster = []
    for i in distance[0:5]:
        rec_movies.append(movies.iloc[i[0]].title)
        rec_poster.append("http://image.tmdb.org/t/p/w500/" + movies.iloc[i[0]].poster_path)
    return rec_movies,rec_poster

def particular(genre):
    index = movies[movies['genres']==genre].index[0]
    distance = sorted(list(enumerate(similar[index])),reverse=True,key=lambda x:x[1])
    mov = []
    for i in distance[0:150]:
        mov.append("http://image.tmdb.org/t/p/w500/" + movies.iloc[i[0]].poster_path)
    return mov

movie_lst = movies['title'].values

selected_movie = st.selectbox(
    'Type or Enter a Movie to give Recomendation',movie_lst
)

recmovie = []


if st.button('Show Recommnedation'):
    recmovie.append(selected_movie)
    rec_movie_name,rec_movie_poster = recomend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(rec_movie_name[0])
        st.image(rec_movie_poster[0])
    
    with col2:
        st.text(rec_movie_name[1])
        st.image(rec_movie_poster[1])

    with col3:
        st.text(rec_movie_name[2])
        st.image(rec_movie_poster[2])

    with col4:
        st.text(rec_movie_name[3])
        st.image(rec_movie_poster[3])
    
    with col5:
        st.text(rec_movie_name[4])
        st.image(rec_movie_poster[4])

st.divider()
    
st.header('Action')
mov = particular('Action')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(mov[num])
with col2:
    st.image(mov[num+1])
with col3:
    st.image(mov[num+2])
with col4:
    st.image(mov[num+3])
with col5:
    st.image(mov[num+4])
st.button("More",key=1)

st.divider()
     
st.header('Adventure')
adv = particular('Adventure')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(adv[0+num])
with col2:
    st.image(adv[1+num])
with col3:
    st.image(adv[2+num])
with col4:
    st.image(adv[3+num])
with col5:
    st.image(adv[4+num])
st.button("More",key=2)

st.divider()

st.header('Animation')
Animation = particular('Animation')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(Animation[0+num])
with col2:
    st.image(Animation[1+num])
with col3:
    st.image(Animation[2+num])
with col4:
    st.image(Animation[3+num])
with col5:
    st.image(Animation[4+num])
st.button("More",key=3)

st.divider()

st.header('Drama')
Drama = particular('Drama')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=1150
with col1:
    st.image(Drama[0+num])
with col2:
    st.image(Drama[1+num])
with col3:
    st.image(Drama[2+num])
with col4:
    st.image(Drama[3+num])
with col5:
    st.image(Drama[4+num])
st.button("More",key=5)
st.divider()

st.header('ScienceFiction')
ScienceFiction = particular('ScienceFiction')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(ScienceFiction[0+num])
with col2:
    st.image(ScienceFiction[1+num])
with col3:
    st.image(ScienceFiction[2+num])
with col4:
    st.image(ScienceFiction[3+num])
with col5:
    st.image(ScienceFiction[4+num])
st.button("More",key=6)
st.divider()

st.header('Horror')
Horror = particular('Horror')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(Horror[0+num])
with col2:
    st.image(Horror[1+num])
with col3:
    st.image(Horror[2+num])
with col4:
    st.image(Horror[3+num])
with col5:
    st.image(Horror[4+num])
st.button("More",key=7)
st.divider()

st.header('Thriller')
Thriller = particular('Thriller')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(Thriller[0+num])
with col2:
    st.image(Thriller[1+num])
with col3:
    st.image(Thriller[2+num])
with col4:
    st.image(Thriller[3+num])
with col5:
    st.image(Thriller[4+num])
st.button("More",key=8)
st.divider()

st.header('Crime')
Crime = particular('Crime')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(Crime[0+num])
with col2:
    st.image(Crime[1+num])
with col3:
    st.image(Crime[2+num])
with col4:
    st.image(Crime[3+num])
with col5:
    st.image(Crime[4+num])
st.button("More",key=9)
st.divider()

st.header('Family & Kids')
Family = particular('Family')
col1,col2,col3,col4,col5 = st.columns(5)
num = math.floor(random.random()*150)
if num+4 >=149:
    num//=150
with col1:
    st.image(Family[0+num])
with col2:
    st.image(Family[1+num])
with col3:
    st.image(Family[2+num])
with col4:
    st.image(Family[3+num])
with col5:
    st.image(Family[4+num])
st.button("More",key=10)