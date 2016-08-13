import requests

mv_src = 'http://www.omdbapi.com/?s=godfather&page='
mv_src_id = 'http://www.omdbapi.com/?i='
mv_db = 'http://127.0.0.1:8000/movies/'

fields = ["Title", "Plot", "Poster", "Year", "Director", "imdbRating", "Plot"]

for i in range(1, 10):
    result = requests.get(mv_src + str(i + 1)).json()
    if result['Response'] != u'False':
        movies = result["Search"]
        for movie in movies:
            imdb_id = movie["imdbID"]
            movie_full = requests.get(mv_src_id + str(imdb_id)).json()
            movie_for_base = {}
            for n in movie_full:
                if n in fields:
                    movie_for_base[n.lower()] = movie_full[n]

            aaa = requests.post(mv_db, json=movie_for_base)
            print(aaa.json())
