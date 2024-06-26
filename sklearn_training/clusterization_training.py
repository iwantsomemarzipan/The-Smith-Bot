import os
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
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

# Obtaining vectors for each line in lyrics and
# calculating their average
def get_sentence_vector(line):
    words = line.split()
    vectors = [my_model[word] for word in words if word in my_model]
    return np.mean(vectors, axis=0) if vectors else None

# Saving and filtering vectors
sentence_vectors = [get_sentence_vector(line) for line in lines]
valid_sentence_vectors = [vec for vec in sentence_vectors if vec is not None]

os.chdir('..')
os.chdir('./sklearn_training')

# Using elbow method to find optimal number of clusters
distortions = []
cluster_range = range(1, 201)

for k in cluster_range:
    model = KMeans(n_clusters=k)
    model.fit(valid_sentence_vectors)
    distortions.append(model.inertia_)

sns.lineplot(x=cluster_range, y=distortions)
plt.title('Sum of squared distances to the cluster center')
plt.xlabel('Number of clusters')
plt.ylabel('Sum of squared distances')
plt.savefig('elbow.png')

# Training clustering model
# considering that the best number of clusters is 30
kmeans = KMeans(n_clusters=30, random_state=42)
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
