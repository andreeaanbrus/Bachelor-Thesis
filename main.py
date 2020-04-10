from frequentTerms import termFrequency
from clustering.myClustering import MyClustering
from removeSentences import removeSentences
from clustering.similarity import cosine
from vectorRepresentationOfSentences import vectorRepresentationOfSentences
from myutils import zero_vector

inputFile = 'testdata/input4.txt'
termsFrequencyFile = 'testdata/termsFrequency-input4.txt'
summaryFile = 'testdata/summary-input4.txt'
vectorsFile = 'testdata/vectors-input4.txt'
clustersFile = 'testdata/clusters-input4.txt'

# the number of clusters should be 30% of the initial text
noClusters = int(len(open(inputFile).read().split('.')) * 0.3)

(no_of_most_frequent_terms, termsFrequency, word_to_lemma) = termFrequency(inputFile, termsFrequencyFile)

# 4. Remove the longest/shortest sentences (sentences over 20 words, under 10 words)
sentences = removeSentences(inputFile, '.')
print(no_of_most_frequent_terms)
print(termsFrequency)
print(word_to_lemma)
mostFrequentTerms = termsFrequency[:no_of_most_frequent_terms]

vectorRepresentation = vectorRepresentationOfSentences(sentences, mostFrequentTerms, no_of_most_frequent_terms,
                                                       word_to_lemma)

# 5. Remove zero-vectors
for vector in vectorRepresentation:
    if zero_vector(vector):
        vectorRepresentation.remove(vector)

# 6.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}
for i in range(len(vectorRepresentation)):
    print(vectorRepresentation[i], sentences[i])
cluster = MyClustering(noClusters=noClusters, similarity=cosine, input=vectorRepresentation)
labels = cluster.predict()
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
