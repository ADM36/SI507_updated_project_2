
class Movie:
    def __init__(self, flick):
        self.title = flick['Title']
        self.imdb = flick['IMDB Rating']
        self.release = flick['Release Date']
        self.genre = flick['Major Genre']
        self.mpaa = flick['MPAA Rating']
        self.director = flick['Director']
        self.tomatoes = flick['Rotten Tomatoes Rating']
        self.us_gross = flick['US Gross']
        self.world_gross = flick['Worldwide Gross']

    def __str__(self):
        return "{} | {}".format(self.title,self.imdb)

#test = Movie(movies_clean.iloc[2])
#print(test.title)
#print(len(movies_clean.index))
