from clustering.myKMeans import MyKMeans
from frequentTerms import termFrequency
from clustering.myHierarchicalClustering import MyHierarchicalClustering
from removeSentences import removeSentences
from clustering.similarity import cosine, customSimilarity, euclidean
from vectorRepresentationOfSentences import vectorRepresentationOfSentences
from myutils import zero_vector

inputFile = 'testdata/input3.txt'
termsFrequencyFile = 'termsFrequency.txt'
summaryFile = 'summary-input2.txt'
vectorsFile = 'vectors.txt'
clustersFile = 'clusters.txt'

# the number of clusters should be 30% of the initial text
noClusters = int(len(open(inputFile).read().split('.')) * 0.3)

(no_of_most_frequent_terms, termsFrequency, word_to_lemma) = termFrequency(inputFile, termsFrequencyFile)

# 4. Remove the longest/shortest sentences (sentences over 20 words, under 10 words)
sentences = removeSentences(inputFile, '.')
mostFrequentTerms = termsFrequency[:no_of_most_frequent_terms]

vectorRepresentation = vectorRepresentationOfSentences(sentences, mostFrequentTerms, no_of_most_frequent_terms,
                                                       word_to_lemma)

# 5. Remove zero-vectors
for vector in vectorRepresentation:
    if zero_vector(vector):
        vectorRepresentation.remove(vector)

# 6.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}
cluster = MyHierarchicalClustering(noClusters=noClusters, similarity=cosine, input=vectorRepresentation)
labels = cluster.predict()
print(labels)

# 6. Apply KMEANS clustering
cluster = MyKMeans(noClusters=noClusters, similarity=euclidean, input=vectorRepresentation)
(labels, centroids) = cluster.predict()
print(labels)

summary = []
i = 0
j = 0
while j < noClusters:
    while i < len(sentences):
        if labels[i] == j:
            # for now, pick the first sentence from the cluster
            # add some wights to the sentences later
            summary.append((i, sentences[i]))
            break
        i += 1
    j += 1
    i = 0

fout = open(summaryFile, "w")  # write summary here
for i in summary:
    fout.write(i[1] + "\n")
fout.close()

fout = open(clustersFile, "w")
fout.write(str(labels))
fout.close()

fout = open(vectorsFile, "w")
for i in range(len(vectorRepresentation)):
    fout.write(str(vectorRepresentation[i]) + '\n' + sentences[i] + '\n')
fout.close()
