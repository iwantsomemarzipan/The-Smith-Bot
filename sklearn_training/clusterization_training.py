import os
import numpy as np
import joblib
from sklearn.cluster import KMeans

os.chdir('./sklearn_training')

# Загружаем преобразованный (за кадром) bin файл модели
my_model = joblib.load('the_smiths_word2vec_model.pkl')

os.chdir('..')
os.chdir('./data')

txt_file = 'lyrics_only.txt'

with open(txt_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.lower()

# Функция для получения векторов для каждого слова 
# и подсчёта их среднего для получения вектора предложения
def get_sentence_vector(line):
    words = line.split()
    vectors = [my_model[word] for word in words if word in my_model]
    return np.mean(vectors, axis=0) if vectors else None

# Сохраняем и фильтруем векторы
sentence_vectors = [get_sentence_vector(line) for line in lines]
valid_sentence_vectors = [vec for vec in sentence_vectors if vec is not None]

os.chdir('..')
os.chdir('./sklearn_training')

# Тренируем модель кластеризации
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(valid_sentence_vectors)
cluster_labels_c = kmeans.labels_

joblib.dump(kmeans, 'the_smiths_kmeans_model.pkl')

line_clusters = {}

# Присваиваем каждую строку песен тому или иному кластеру на основе
# предсказаний модели кластеризации, сохраняем кластеры и их строки в словарь
for i, line in enumerate(lines):
    if i < len(cluster_labels_c) and sentence_vectors[i] is not None:
        cluster_id = cluster_labels_c[i]
        if cluster_id not in line_clusters:
            line_clusters[cluster_id] = []
        line_clusters[cluster_id].append(line)
