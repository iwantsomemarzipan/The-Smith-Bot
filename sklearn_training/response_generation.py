from sklearn_training.clusterization_training import line_clusters, my_model

import joblib
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

kmeans = joblib.load('the_smiths_kmeans_model.pkl')

# Searching for words and their embeddings in user's input that are
# familiar to word2vec model and calculating vectors' average
def get_sentence_vector(user_input):
    words = re.sub(r'[^a-zA-Z\s]', '', user_input)
    words = words.lower()
    words = words.split()
    vectors = [my_model[word] for word in words if word in my_model]
    return np.mean(vectors, axis=0) if vectors else None

def get_similar_response(user_input):
    user_vector = get_sentence_vector(user_input)
    if user_vector is not None:
        # Calculating the similarity with each cluster centroid
        # with cosine similarity
        similarities = []
        for centroid in kmeans.cluster_centers_:
            similarity = cosine_similarity([user_vector], [centroid])[0][0]
            similarities.append(similarity)

        # Detecting the cluster with the greatest similarity
        max_similarity_index = np.argmax(similarities)
        response_cluster = line_clusters[max_similarity_index]

        # Choosing a random line from the target cluster
        response = np.random.choice(response_cluster)

    elif user_vector is None:
        return "Apologies, I couldn't decipher your input this time :("

    return response
