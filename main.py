import pandas as pd
from sklearn.neighbors import NearestNeighbors

# load in the data file
df = pd.read_csv("/Users/rachelprempeh/PycharmProjects/DSAGroup/final_data_with_titles.csv")

# knn can't handle any NaN values, so just ensure no entries have null features and to improve accuracy, cleanse data from missing genres
df.dropna(inplace=True)
df = df[df['Genres'] != "(no genres listed)"]

# preprocess for 19 possible genres that will each be their own feature
genres = ['Film-Noir', 'War', 'Western', 'Musical', 'Crime', 'Adventure', 'Mystery', 'Thriller', 'IMAX', 'Romance', 'Sci-Fi', 'Fantasy', 'Comedy', 'Children', 'Action', 'Horror', 'Documentary', 'Drama', 'Animation']
for genre in genres:
    df[genre] = df['Genres'].apply(lambda x: 1 if genre in x else 0)

# define our features and labels
X = df[['Duration', 'Year'] + genres]
y = df['Avg Rating']


def recommend_movies(user_input, k=7):
    # find neighbors based on euclidean distance and then fit the algorithm
    knn = NearestNeighbors(n_neighbors=k, metric='euclidean')
    knn.fit(X)
    distances, indices = knn.kneighbors([user_input])

    # return a list of the recommended movies by printing their title and average rating
    recommended_movies = df.iloc[indices[0]][['Title', 'Avg Rating']]
    recommended_movies_unique = recommended_movies.drop_duplicates(subset=['Title'])

    # found 7 neighbors, but only returning 5
    return recommended_movies_unique[['Title', 'Avg Rating']].head(5)


# get user input for up to 3 genres, length of the movie, and year it was released
print("Please select up to 3 genres from the following options:")
print(genres)
selected_genres = input("Enter your chosen genres separated by commas: ").split(',')[:3]
duration = int(input("Enter your preferred movie duration (in minutes): "))
year = int(input("Enter your preferred movie release year: "))

# store the user's selections for each category
user_input = [duration, year] + [1 if genre in selected_genres else 0 for genre in genres]

# use the KNN algorithm to find movie suggestions and print them
recommended_movies = recommend_movies(user_input)
# recommended_movies_unique = recommended_movies.drop_duplicates(subset=['Title'])

print("Recommended Movies:")
print(recommended_movies.to_string(index=False))
# print(recommended_movies_unique.to_string(index=False))
