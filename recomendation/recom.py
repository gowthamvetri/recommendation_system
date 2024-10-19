import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle

movies = pd.read_csv('csv/TMDB_movie_dataset_v11.csv')

# movies = movies.dropna()

# print(movies.Poster.count())

movies = movies[['id','title','poster_path','overview','genres','tagline','keywords']]

# movies = movies[['Movie Name','Description','Poster']]


movies = movies.dropna()
movies = movies.drop_duplicates()

movies = movies.head(20000)

def remno(movie):
    l = ""
    indi = 0
    for i in movies:
        if(indi == 1):
            l.join(i)
        elif(i=='.'):
            indi=1
    return l

def recomend(movie):
    index = final[final['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x: x[1])
    for i in distance[0:5]:
        print(final.iloc[i[0]].title)

def removespace(word):
    l = []
    for i in word:
        l.append(i.replace(" ",""))
    return l

ps = PorterStemmer()
def steams(text):
    l = []
    for i in text:
        l.append(ps.stem(i))
    return "".join(l)

def first(lst):
    temp = lst[0]
    return temp

# print(movies['Poster'] if movies['Movie Name'] == "2. Thunivu" else "movie not avilable")

# movies['Movie Name'] = movies['Movie Name'].apply(remno)

movies['overview'] = movies['overview'].apply(lambda x:x.split())
movies['genres'] = movies['genres'].apply(lambda x:x.split(','))
movies['keywords'] = movies['keywords'].apply(lambda x:x.split(','))
movies['tagline'] = movies['tagline'].apply(lambda x:x.split())
movies['titles'] = movies['title'].apply(lambda x:x.split())

movies['overview'] = movies['overview'].apply(removespace)
movies['genres'] = movies['genres'].apply(removespace)
movies['keywords'] = movies['keywords'].apply(removespace)
movies['tagline'] = movies['tagline'].apply(removespace)
movies['titles'] = movies['titles'].apply(removespace)


movies['tag'] = movies['genres']+movies['keywords']+movies['overview']+movies['tagline']+movies['titles']

movies['genres'] = movies['genres'].apply(first)

final = movies[['id','title','tag','poster_path','genres']]

print(final['genres'].value_counts())
final['tag'] = final['tag'].apply(lambda x: " ".join(x))
final['tag'] = final['tag'].apply(lambda x:x.lower())
final['tag'] = final['tag'].apply(steams)

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(final['tag']).toarray()

similarity = cosine_similarity(vector)

recomend('Spider-Man')

# index = movies[movies['title']==movie].index[0]
# index = final[final['genres']=='Action'].index[0]
# print(index)

# pickle.dump(final,open('csv/movielst.pkl','wb'))
# pickle.dump(similarity,open('csv/similar.pkl','wb'))

# print(final['genres'].unique())
