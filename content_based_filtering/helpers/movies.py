def get_movie_id(movies, title, year=None):
    res = movies[movies['title'] == title]
    if year:
        res = res[res['year'] == year]

    if len(res) > 1:
        print("Ambiguous: found")
        print(f"{res['title']} {res['year']}")
    elif len(res) == 0:
        print('not found')
    else:
        return res.index[0]

def get_movie_name(movies, index):
    return movies.iloc[index].title

def get_movie_year(movies, index):
    return movies.iloc[index].year
