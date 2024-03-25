import os
import numpy as np
import joblib
from sklearn.cluster import KMeans

os.chdir('./sklearn_training')

# Loading .pkl converted w2v model file
my_model = joblib.load('the_smiths_word2vec_model.pkl')

os.chdir('..')
os.chdir('./data')

txt_file = 'lyrics_only.txt'

with open(txt_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.lower()

# Obtaining vectors for each word and calculating
# their average to get sentence vectors
def get_sentence_vector(line):
    words = line.split()
    vectors = [my_model[word] for word in words if word in my_model]
    return np.mean(vectors, axis=0) if vectors else None

# Saving and filtering vectors
sentence_vectors = [get_sentence_vector(line) for line in lines]
valid_sentence_vectors = [vec for vec in sentence_vectors if vec is not None]

os.chdir('..')
os.chdir('./sklearn_training')

# Training clustering model
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(valid_sentence_vectors)
cluster_labels = kmeans.labels_

joblib.dump(kmeans, 'the_smiths_kmeans_model.pkl')

line_clusters = {}

# Assigning each line of songs to a cluster based on the predictions
# of the clustering model, save the clusters and
# their corresponding lines in a dictionary
for i, line in enumerate(lines):
    if i < len(cluster_labels) and sentence_vectors[i] is not None:
        cluster_id = cluster_labels[i]
        if cluster_id not in line_clusters:
            line_clusters[cluster_id] = []
        line_clusters[cluster_id].append(line)
