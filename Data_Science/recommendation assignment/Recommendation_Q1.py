# import os
import pandas as pd

# import Dataset 
game = pd.read_csv("C:\\Data Science\\360\\Recommendation Engine\\Assignment\\game.csv", encoding = 'utf8')
game.shape # shape
game.columns
game.game # genre columns

from sklearn.feature_extraction.text import TfidfVectorizer #term frequencey- inverse document frequncy is a numerical statistic that is intended to reflect how important a word is to document in a collecion or corpus

# Creating a Tfidf Vectorizer to remove all stop words
tfidf = TfidfVectorizer(stop_words = "english")    # taking stop words from tfid vectorizer 

# replacing the NaN values in overview column with empty string
game["game"].isnull().sum() 
game["game"] = game["game"].fillna(" ")

# Preparing the Tfidf matrix by fitting and transforming
tfidf_matrix = tfidf.fit_transform(game.game)   #Transform a count matrix to a normalized tf or tf-idf representation
tfidf_matrix.shape 

# with the above matrix we need to find the similarity score
# There are several metrics for this such as the euclidean, 
# the Pearson and the cosine similarity scores

# For now we will be using cosine similarity matrix
# A numeric quantity to represent the similarity between 2 movies 
# Cosine similarity - metric is independent of magnitude and easy to calculate 

# cosine(x,y)= (x.y⊺)/(||x||.||y||)

from sklearn.metrics.pairwise import linear_kernel

# Computing the cosine similarity on Tfidf matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

# creating a mapping of anime name to index number 
game_index = pd.Series(game.index, index = game['game']).drop_duplicates()
game_id = game_index["SoulCalibur"]
game_id

def get_recommendations(Name, topN):    
    # topN = 10
    # Getting the movie index using its title 
    game_id = game_index[Name]
    
    # Getting the pair wise similarity score for all the games's with that 
    # game
    cosine_scores = list(enumerate(cosine_sim_matrix[game_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)
    
    # Get the scores of top N most similar game 
    cosine_scores_N = cosine_scores[0: topN + 1] 
    
    # Getting the game index 
    game_idx  =  [i[0] for i in cosine_scores_N]
    game_scores =  [i[1] for i in cosine_scores_N]
    
    # Similar game and scores
    game_similar_show = pd.DataFrame(columns=["game", "Score"])
    game_similar_show["game"] = game.loc[game_idx, "game"]
    game_similar_show["Score"] = game_scores
    game_similar_show.reset_index(inplace = True)
    # anime_similar_show.drop(["index"], axis=1, inplace=True)
    print (game_similar_show)
    # return (game_similar_show)

    
# Enter your game and number of game's to be recommended 
get_recommendations(6, topN = 10)
game_index["SoulCalibur"]

