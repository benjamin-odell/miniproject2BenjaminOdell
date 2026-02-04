# INF601 - Advanced Programming in Python
# Benjamin Odell
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt

#all the movie data
data = pd.read_csv('data/Cleaned_DataSet.csv')

#get user scores
scores = data['imdb_score']

#get budget
budgets = data['budget']

#prints scores and budgets
print(scores)
print(budgets)

print(data['imdb_score'].describe())


#we will split  movies into 5 categories
#masterpiece >9
#great >8
# good >7
# ok >5
#bad <= 5

#imdb scores in the csv are from 0-1
#multiply all scores by ten to get scores from 0-10
data['imdb_score'] = data['imdb_score'].apply(lambda x: x * 10)

masterpiece_movies = data[data['imdb_score'] >= 9]
great_movies = data[(data['imdb_score'] >= 8) & (data['imdb_score'] < 9)]
good_movies = data[(data['imdb_score'] >= 7) & (data['imdb_score'] < 8)]
ok_movies = data[(data['imdb_score'] >= 5) & (data['imdb_score'] < 7)]
bad_movies = data[data['imdb_score'] < 5]