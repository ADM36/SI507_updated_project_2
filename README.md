When run, the project_two program will run a flask application that will allow a user to provide text to a web URL and find the number of movies in a csv data file (movies_clean.csv) and also retrieve seven random movie titles with their appropriate MPAA rating (ex: PG).

The program utilizes four different files:

- SI507_project2.py
  This is the program's controller code, which provides controls for python.

- movies_tools.py
  This is code which is imported into the SI507SI507_project2.py code. This file contains code which defines a class definition Movie, which represents one movie with variables important to its class, including the movie title and its MPAA rating.

- values.html
  Inside the templates folder, values.html acts as a special template file which controls some of the "view" of the program (what a human can view/see). This code, also imported into the SI507SI507_project2.py file, interacts with the code in our other files to make the functions viewable to humans on a computer.

- movies_clean.csv
  This file is our csv data file which contains information on over 3,000 movies. Our SI507SI507_project2.py code will download data from the csv file and interact with it to provide us information from the data.

When a user runs this program on a computer (by going to terminal or bash and routing to the folder containing all of these documents, and then typing in "python SI507SI507_project2.py") they should receive a message back that looks similair to the below:

* Serving Flask app "SI507_project2" (lazy loading)
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

If this happens, the user should copy http://127.0.0.1:5000/ and paste it into their web application search bar. Once the user does this, they should see a message printed on the web application that shows the number of movies recorded in the movies_clean.csv file.

This happens because of the following route code:

@app.route('/')
def recordings():
    return '<h1> {} movies recorded.</h1>'.format(len(movies_clean.index))

Next, the user may interact with the flask application and retrieve a list of seven random movies from the movies_clean.csv database, specifically printing the name of those movies with their MPAA rating to the user's web application. To do this, the user must add "/movies/rating" in the search bar after the rest of the text already in the search bar.

This happens because of the following route code:

@app.route('/movies/rating')
def ratings():
    movie_list = []
    for i in range(7):
        indx = randint(1,3000)
        flick = Movie(movies_clean.iloc[indx])
        movie_list.append(str(flick))
    return render_template('values.html',word_list = movie_list)

In this code, you will see we utilize the class Movie, which is defined in the movie_tools.py file, and imported. You will also see we interact with our template file values.html and use the function render_template to print our function return values to our web application in an appropriate html format (seen in the value.html code).
