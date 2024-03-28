import pandas as pd
import numpy as np

# get data
url='https://github.com/prasertcbs/basic-dataset/raw/master/IMDB_Movie_1000_Data.csv'
df=pd.read_csv(url)
df[:5]

# select col split comma and space
sg = df['Genre'].str.split(',\s*')

# convert list concat to str and make to dummies
dd = sg.str.join(',').str.get_dummies(',')

# concat 2 df by axis = 1 is col
df = pd.concat([df,dd], axis=1)


