### INF601 - Advanced Programming in Python
### Benjamin Odell
# Mini Project 2


## Description
 
Does budget effect how good a move is?
This seeks to answer this question.

This program creates two sets of charts. The first set is based on ranking movie scores based on a threshold.
* Masterpiece: 100 - 85
* Great: 85 - 75
* Good: 75 - 60 
* Okay: 60 - 50
* Bad: 50 - 0

The next set of charts is based on the percentile of the movie's score. Each section consist of 10% of the movies.
<br>
90% means the movie is ranked better than 90% of movies in the dataset.

 
## Getting Started


### Dependencies
```
pip install -r requirements.txt
```
### Installing

* Download files and place in its own folder
* You can change the stock tickers in stock_tickers.py if you want to look at different stocks

### Data
Download the dataset [here](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset).
<br>
Place the dataset into a folder called data in the folder where the project is stored.
 
### Executing program
 
* Run the main.py file
* Charts will be saved in a folder called charts
 
## Authors
 
Benjamin Odell

## Acknowledgments
 
Inspiration, code snippets, etc.
* [Dataset Used: ](https://www.kaggle.com/datasets/ashpalsingh1525/imdb-movies-dataset)
* [Y Axis Formatting help](https://queirozf.com/entries/matplotlib-examples-number-formatting-for-axes-labels)
* [Thousands Comma Tick Labels](https://stackoverflow.com/questions/38152356/dollar-sign-with-thousands-comma-tick-labels)
* [Matplotlib Documentation](https://matplotlib.org/stable/tutorials/pyplot.html)
* [Pandas Documentation](https://pandas.pydata.org/docs/)