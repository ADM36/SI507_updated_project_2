# Import statements necessary
from flask import Flask, render_template
from movies_tools import Movie
import pandas as pd
import random
from random import randint

# Set up application
app = Flask(__name__)

movies_clean = pd.read_csv('movies_clean.csv')

# Routes

@app.route('/')
def recordings():
    return '<h1> {} movies recorded.</h1>'.format(len(movies_clean.index))

@app.route('/movies/rating')
def ratings():
    movie_list = []
    for i in range(7):
        indx = randint(1,3000)
        flick = Movie(movies_clean.iloc[indx])
        movie_list.append(str(flick))
    return render_template('values.html',word_list = movie_list)


if __name__ == '__main__':
    app.run()
