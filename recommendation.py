import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item interaction data
data = {
    'User': ['User1', 'User2', 'User1', 'User3', 'User2', 'User3'],
    'Movie': ['Movie1', 'Movie1', 'Movie2', 'Movie2', 'Movie3', 'Movie3'],
    'Rating': [5, 4, 3, 2, 4, 5]
}

df = pd.DataFrame(data)

# user-item matrix
user_item_matrix = df.pivot_table(index='User', columns='Movie', values='Rating', fill_value=0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix)

# user-movie recommendation function
def recommend_movies(user, user_item_matrix, user_similarity):
    similar_users = user_similarity[user]
    similar_users_indexes = similar_users.argsort()[::-1]
    
    recommendations = []
    for index in similar_users_indexes:
        if similar_users[index] > 0 and user_item_matrix.iloc[index].sum() > 0:
            for movie in user_item_matrix.columns:
                if user_item_matrix.at[user, movie] == 0 and user_item_matrix.at[index, movie] > 0:
                    recommendations.append((movie, user_item_matrix.at[index, movie]))
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations

# Get movie recommendations for User1
user_to_recommend = 'User1'
movie_recommendations = recommend_movies(user_to_recommend, user_item_matrix, user_similarity)

print(f"Recommended movies for {user_to_recommend}:")
for movie, rating in movie_recommendations:
    print(f"{movie} (Rating: {rating})")
