n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    name = input("\nMovie Name: ")
    year = int(input("Release Year: "))
    director = input("Director: ")
    cost = float(input("Production Cost: "))
    collection = float(input("Collection Made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

print("\nAll Movie Details:")
for m, d in movies.items():
    print(m, d)

print("\nMovies released before 2015:")
for m, d in movies.items():
    if d["year"] < 2015:
        print(m)

print("\nMovies that made profit:")
for m, d in movies.items():
    if d["collection"] > d["cost"]:
        print(m)

dir_name = input("\nEnter director name to search: ")
print("Movies directed by", dir_name)
for m, d in movies.items():
    if d["director"] == dir_name:
        print(m)
