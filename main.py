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