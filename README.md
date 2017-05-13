# Mitt's Movie Trailer Site

This repository displays a webpage of movie posters and plays their trailers
when you click each movie.

It takes a list of movies, which are described in "entertainment_center.py",
and uses a constructor in Media.py to build an instance of each movie. This
list of movie objects in stored in a "movies" variable, which is created in the
"entertainment_center.py" file. Finally, by running "entertainment_center.py"
you call the method open_movies_page(), which is located in
"fresh_tomatoes.py", and takes a list of movies as a parameter.

The file "fresh_tomatoes.py" constructs the webpage. It takes a list of movies,
the ones previously defined in "entertainment_center.py", and constructs a
content variable that contains all the information needed by the HTML cards
for each movie. Finally, it launches builds the HTML file
"fresh_tomatoes.html", and launches the page in a local browser.

You can run all code by running the script in "entertainment_center.py" file.
This has a aforementioned open_movies_page() method, which takes care of all
the work for you. You can do this by

--

Further work would create the list of movies from an external API, instead of
defining each movie by hand, which would enable a much larger collection of
movies.
