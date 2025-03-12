# Movie Recommendation System
# Description: Build a simple movie recommendation system that stores movies as keys and lists of attributes (genre, director, year) as values. Users can input preferences, and the system suggests movies based on matching attributes.
# Dictionary Use: Store movies and their attributes for easy lookup and comparison.

disney_movies = {
    "The Lion King": ["Adventure", "Drama"],
    "Frozen": ["Adventure", "Comedy"],
    "Beauty and the Beast": ["Family", "Fantasy"],
    "Aladdin": ["Adventure", "Comedy"],
    "Toy Story": ["Adventure", "Comedy"],
    "Mulan": ["Adventure", "Family"],
    "Finding Nemo": ["Adventure", "Comedy"],
    "The Little Mermaid": ["Family", "Fantasy"],
    "Cinderella": ["Family", "Fantasy"],
    "Zootopia": ["Adventure", "Comedy"],
    "Moana": ["Adventure", "Comedy"],
    "Wreck-It Ralph": ["Adventure", "Comedy"],
    "The Incredibles": ["Action", "Adventure"],
    "Big Hero 6": ["Action", "Adventure"],
    "Sleeping Beauty": ["Family", "Fantasy"],
    "Hercules": ["Adventure", "Comedy"],
    "Tangled": ["Adventure", "Comedy"],
    "Pocahontas": ["Adventure", "Drama"],
    "Snow White and the Seven Dwarfs": ["Family", "Fantasy"],
    "Dumbo": ["Family", "Fantasy"]
}

def searchDict(dict, value):
    keys = list(dict.keys())
    moviesFound = []
    for i in range(len(keys)):
        genres = dict[keys[i]]
        for j in range(len(genres)):
            if genres[j] == value:
                moviesFound.append(keys[i])
    return moviesFound

genres = ["Action", "Adventure","Comedy", "Drama", "Family", "Fantasy"]
for i in range(len(genres)):
    print(i, genres[i])

choice = input("Which genre do you want recommendations for? ")
movies = searchDict(disney_movies, choice)
print(movies)