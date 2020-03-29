import copy

import numpy as np
from sklearn.cluster import AgglomerativeClustering

from frequentTerms import termFrequency
from removeSentences import removeSentences
from vectorRepresentationOfSentences import vectorRepresentationOfSentences

inputFile = 'input2.txt'
termsFrequencyFile = 'termsFrequency2.txt'
outputFile = 'output2.txt'
sumaryFile = 'summary2.txt'
# the number of clusters should be 30% of the initial text
noClusters = int(len(open(inputFile).read().split('.')) * 0.3)

(no_of_most_frequent_terms, termsFrequency, word_to_lemma) = termFrequency(inputFile, termsFrequencyFile)

# 4. Remove the longest/shortest sentences (sentences over 20 words, under 10 words)
sentences = removeSentences(inputFile, '.')
print(no_of_most_frequent_terms)
print(termsFrequency)
print(word_to_lemma)
mostFrequentTerms = termsFrequency[:no_of_most_frequent_terms]


vectorRepresentation = vectorRepresentationOfSentences(sentences, mostFrequentTerms, no_of_most_frequent_terms, word_to_lemma)
#
# # 5.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}
#
# # TODO handle zero vectors
# # if vector_representation[i] is a zero-vector, it should not be considered in the summary because it does not contain any frequent terms
# # we don't consider them when clustering
# # assign them cluster number -1
# original_vector_representation = copy.deepcopy(vector_representation)
#
# for vector in vector_representation:
#     if zero_vector(vector):
#         vector_representation.remove(vector)
# print(vector_representation)

print(noClusters)
for i in range(len(vectorRepresentation)):
    print(vectorRepresentation[i], sentences[i])
cluster = AgglomerativeClustering(n_clusters=noClusters, linkage="single", affinity="cosine")
cluster.fit_predict(np.array(vectorRepresentation))
print(cluster.labels_)

summary = []
i = 0
j = 0
while j < noClusters:
    while i < len(sentences):
        if cluster.labels_[i] == j:
            # for now, pick the first sentence from the cluster
            # add some wights to the sentences later
            summary.append({i: sentences[i]})
            break
        i += 1
    j += 1
    i = 0
print(summary)

