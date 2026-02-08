# INF601 - Advanced Programming in Python
# Benjamin Odell
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#all the movie data
data = pd.read_csv('data/imdb_movies.csv')

print(data.head())

#get user scores
scores = data['score']

#get budget
budgets = data['budget_x']

#prints scores and budgets
print(scores)
print(budgets)


#we will split  movies into 5 categories
#masterpiece >90
#great >80
# good >70
# ok >50
#bad <= 50

masterpiece_movies = data[scores > 90]
great_movies = data[(scores >= 80) & (scores < 90)]
good_movies = data[(scores >= 70) & (scores < 80)]
ok_movies = data[(scores >= 50) & (scores < 70)]
bad_movies = data[scores < 50]

#count up each how many in each category
movie_count_arr = [len(masterpiece_movies), len(great_movies), len(good_movies), len(ok_movies), len(bad_movies)]

movie_budget_arr = [masterpiece_movies['budget_x'].mean(),
                    great_movies['budget_x'].mean(),
                    good_movies['budget_x'].mean(),
                    ok_movies['budget_x'].mean(),
                    bad_movies['budget_x'].mean()]

movie_cat_arr = ['Masterpiece', 'Great', 'Good', 'Okay', 'Bad']

#configer ticker
tick_func = ticker.FuncFormatter(lambda x, _: format(int(x), ','))


#amount of movies
plt.bar_label(plt.bar(movie_cat_arr, movie_count_arr),fmt='{:,.0f}')
plt.gca().yaxis.set_major_formatter(tick_func)
plt.ylabel('Number of Movies')
plt.title('Number of Movies of Each Ranking')
plt.show()
plt.close()

#avg budget
plt.figure(figsize=(10,6))
plt.bar_label(plt.bar(movie_cat_arr, movie_budget_arr),fmt='${:,.0f}')
plt.gca().yaxis.set_major_formatter(tick_func)
plt.ylabel('Budget')
plt.title('Movie Budget by Scores')
plt.show()