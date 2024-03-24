from sklearn_training.clusterization_training import line_clusters, my_model

import joblib
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

kmeans = joblib.load('the_smiths_kmeans_model.pkl')

# Функции для получения векторов для каждого слова из инпута пользователя 
# и подсчёта их среднего для получения вектора предложения
def get_sentence_vector(user_input):
    words = re.sub(r'[^a-zA-Z\s]', '', user_input)
    words = words.lower()
    words = words.split()
    vectors = [my_model[word] for word in words if word in my_model]
    return np.mean(vectors, axis=0) if vectors else None

def get_similar_response(user_input):
    user_vector = get_sentence_vector(user_input)
    if user_vector is not None:
        # Вычисляем сходство с каждым центроидом кластера
        similarities = []
        for centroid in kmeans.cluster_centers_:
            similarity = cosine_similarity([user_vector], [centroid])[0][0]
            similarities.append(similarity)

        # Находим кластер с наибольшим сходством
        max_similarity_index = np.argmax(similarities)
        response_cluster = line_clusters[max_similarity_index]

        # Выбираем случайную строку из выбранного кластера
        response = np.random.choice(response_cluster)

    elif user_vector is None:
        return "Apologies, I couldn't decipher your input this time :("

    return response
