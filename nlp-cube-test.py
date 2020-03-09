import copy

import numpy as np
from cube.api import Cube
from sklearn.cluster import AgglomerativeClustering

from utils import zero_vector

cube = Cube(verbose=True)

cube.load("ro")

fin = open('input.txt')
text = fin.read()
sentences = cube(text)
no_of_all_terms = 0
words = [{} for _ in range(0, len(sentences))]  # 1.calculating the frequency of the terms in each sentence f(i, t)
for i in range(0, len(sentences)):
    for entry in sentences[i]:
        if entry.upos == "VERB" or entry.upos == "NOUN" or entry.upos == "PROPN":
            # only calculate the frequency of verbs and nouns and proper nouns
            if entry.lemma not in words[i]:
                words[i][entry.lemma] = 1
            else:
                words[i][entry.lemma] += 1
# 2. calculate the sum of the frequencies of all terms computed at 1
# sum(f(i, t), i = 1, n)
overAllFrequency = {}
for i in range(0, len(words)):
    for word in words[i].keys():
        no_of_all_terms += 1
        if word not in overAllFrequency:
            overAllFrequency[word] = 1
        else:
            overAllFrequency[word] += words[i][word]

# 3. calculate the m most frequent terms
sortedTerms = {k: v for k, v in sorted(overAllFrequency.items(), key=lambda item: item[1], reverse=True)}
fout = open("output.txt", "w")
for key in sortedTerms.keys():
    fout.write(key + " " + str(sortedTerms[key]) + "\n")
no_of_most_frequent_terms = int(no_of_all_terms * 0.3)  # m
most_frequent_terms = list(sortedTerms.keys())
# print(no_of_all_terms, no_of_most_frequent_terms)
fout.close()

# 4. Represent each sentence Si by m-vectors v[i] = {f(i, t1), f(i, t2), ... f(i, tm)}.
vector_representation = [[0 for _ in range(no_of_most_frequent_terms)] for _ in range(len(sentences))]
for i in range(len(sentences)):
    for j in range(no_of_most_frequent_terms):
        # print(sentences[i], most_frequent_terms[j])
        for entry in sentences[i]:
            if most_frequent_terms[j] == entry.lemma:
                vector_representation[i][j] += 1
for i in range(len(vector_representation)):
    print(vector_representation[i])

# 5.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}

# TODO handle zero vectors
# if vector_representation[i] is a zero-vector, it should not be considered in the summary because it does not contain any frequent terms
# we don't consider them when clustering
# assign them cluster number -1
original_vector_representation = copy.deepcopy(vector_representation)

for vector in vector_representation:
    if zero_vector(vector):
        vector_representation.remove(vector)
print(vector_representation)
cluster = AgglomerativeClustering(n_clusters=3, linkage="single", affinity="cosine")
cluster.fit_predict(np.array(vector_representation))
print(cluster.labels_)
# plt.scatter(vector_representation[:,0],vector_representation[:,1], c=cluster.labels_, cmap='rainbow')


