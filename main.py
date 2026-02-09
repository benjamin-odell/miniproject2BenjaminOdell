# INF601 - Advanced Programming in Python
# Benjamin Odell
# Mini Project 2
import math

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pathlib as path

#all the movie data
data = pd.read_csv('data/imdb_movies.csv')

'''
we need to filter out movies that are not from the US. 
The dataset has all budget in native currency.
This will ensure all budget in USD
We must also remove all movies that have not been release
'''

#only use us movies
data = data[(data['country'] == 'AU') | (data['country'] == 'US')]
data = data[data['orig_lang'] == ' English']
print(data.sort_values('score', ascending=False).head(10))

#only use released movies
data = data[data['status']==' Released']


#get user scores
scores = data['score']

#get budget
budgets = data['budget_x']


#we will split  movies into 5 categories
#masterpiece >85
#great >75
# good >60
# ok >50
#bad <= 50


masterpiece_movies = data[scores > 85]
great_movies = data[(scores >= 75) & (scores < 85)]
good_movies = data[(scores >= 60) & (scores < 75)]
ok_movies = data[(scores >= 50) & (scores < 60)]
bad_movies = data[scores < 50]

print(masterpiece_movies)

#count up each how many in each category
movie_count_arr = [len(masterpiece_movies), len(great_movies), len(good_movies), len(ok_movies), len(bad_movies)]

movie_budget_arr = [masterpiece_movies['budget_x'].mean(),
                    great_movies['budget_x'].mean(),
                    good_movies['budget_x'].mean(),
                    ok_movies['budget_x'].mean(),
                    bad_movies['budget_x'].mean()]

movie_cat_arr = ['Masterpiece', 'Great', 'Good', 'Okay', 'Bad']

cat_color_arr = ['royalblue', 'aqua', 'limegreen', 'sandybrown', 'lightcoral']

#configer ticker
tick_func = ticker.FuncFormatter(lambda x, _: format(int(x), ','))

save_path = path.Path('charts')
#check if charts folder exists, if not create it
if not save_path.exists():
    save_path.mkdir()


#amount of movies
plt.bar_label(plt.bar(movie_cat_arr, movie_count_arr, color=cat_color_arr),fmt='{:,.0f}')
plt.gca().yaxis.set_major_formatter(tick_func)
plt.ylabel('Number of Movies')
plt.title('Number of Movies of Each Ranking')
#plt.show()
plt.savefig(str(save_path / 'movie_count_by_ranking.png'))
plt.close()

#avg budget
plt.figure(figsize=(10,6))
plt.bar_label(plt.bar(movie_cat_arr, movie_budget_arr, color=cat_color_arr),fmt='${:,.0f}')
plt.gca().yaxis.set_major_formatter(tick_func)
plt.ylabel('Budget')
plt.title('Movie Budget by Scores')
plt.savefig(str(save_path / 'avg_movie_budget_by_ranking.png'))
#plt.show()
plt.close()

#sort movies by score
movies = data.sort_values('score', ascending=False)

#get number of movies
count = movies['score'].count()
#divide into ten chunks. Round up to ensure all movies are considered.
chunk = math.ceil(count / 10)
chunks = []

#fill chunks with each group of movies
for i in range(10):
    chunks.append(movies.iloc[i*chunk:(i+1)*chunk])

scores = []

#get avg score
for chunk in chunks:
    scores.append(chunk['score'].mean())

