import pandas as pd

df=pd.read_csv('https://github.com/prasertcbs/basic-dataset/raw/master/IMDB_Movie_1000_Data.csv', nrows=5)
df.head()

# Create Movie id
df['movie_id'] = df.index
df.head()

## Create genere movie
df_genre = df[['movie_id','Genre',]]

df_genre['glist'] = df_genre.Genre.str.split(',')
df_genre.head()

df_genre.drop('Genre', axis=1,inplace=True)

df_genre = df_genre.explode('glist')

# Create Actor
df_actor = df[['movie_id','Actors']]
df_actor['alist'] = df_actor.Actors.str.split(',')

df_actor.drop('Actors', axis=1, inplace=True)

df_actor = df_actor.explode('alist')



