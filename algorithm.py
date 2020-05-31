import math
from datetime import datetime

from clustering.myHierarchicalClustering import MyHierarchicalClustering
from clustering.myKMeans import MyKMeans
from clustering.similarity import euclidean, cosine
from frequentTerms import termFrequency
from myutils import zero_vector
from removeSentences import removeSentences
from vectorRepresentationOfSentences import vectorRepresentationOfSentences


class Algorithm:
    def __init__(self, input_text, method, compression, summary_file, title):
        self.input_text = input_text
        self.method = method
        self.compression = compression
        self.summary_file = summary_file
        self.title = title

    def do(self):
        noClusters = 3
        if self.compression == 30:
            noClusters = math.ceil(len(self.input_text.split('\n')) * 0.3)
            print(noClusters, len(self.input_text.split('\n')))
        if self.compression == 50:
            noClusters = math.floor(len(self.input_text.split('\n')) * 0.5)
            print(noClusters, len(self.input_text.split('\n')))
        start1 = datetime.now()
        (no_of_most_frequent_terms, termsFrequency, word_to_lemma, title_lemma) = termFrequency(self.input_text,
                                                                                                self.title)
        stop1 = datetime.now()
        print("Term frequency and lemmatization time: ", stop1 - start1)
        start2 = datetime.now()
        # 4. Remove the longest/shortest sentences (sentences over 20 words, under 10 words)
        sentences = removeSentences(self.input_text, '.')
        mostFrequentTerms = termsFrequency[:no_of_most_frequent_terms]

        vectorRepresentation, rank = vectorRepresentationOfSentences(sentences, mostFrequentTerms,
                                                                     no_of_most_frequent_terms,
                                                                     word_to_lemma, title_lemma)
        stop2 = datetime.now()
        print("Vector representation time: ", stop2 - start2)

        # 5. Remove zero-vectors
        for i in range(len(vectorRepresentation)):
            if zero_vector(vectorRepresentation[i]):
                vectorRepresentation.remove(vectorRepresentation[i])
                rank.__delitem__(i)

        # 6.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}
        labels = None
        if self.method == 'hierarchical':
            start3 = datetime.now()
            cluster = MyHierarchicalClustering(noClusters=noClusters, similarity=cosine, input=vectorRepresentation)
            labels = cluster.predict()
            stop3 = datetime.now()
            print("Clustering time: ", stop3 - start3)
        if self.method == 'kmeans':
            start3 = datetime.now()
            cluster = MyKMeans(noClusters=noClusters, input=vectorRepresentation, similarity=euclidean)
            labels, centroids = cluster.predict()
            stop3 = datetime.now()
            print("Clustering time: ", stop3 - start3)
        summary = {}
        summary_positions = [-100 for _ in range(noClusters)]
        summary_rank = [-100 for _ in range(noClusters)]
        print(len(summary_rank), len(rank), len(labels))
        print(summary_rank, rank, labels, len(vectorRepresentation))
        for i in range(len(vectorRepresentation)):
            print(i, rank[i], labels[i])
            if rank[i] > summary_rank[labels[i]]:
                summary_positions[labels[i]] = i
                summary_rank[labels[i]] = rank[i]

        # sort the summary_positions to assure the cronological order of the sentences

        summary_positions.sort()
        for pos in summary_positions:
            summary[pos] = sentences[pos]
        summaryResponse = ''
        fout = open(self.summary_file, "w")  # write summary here
        for index, sentence in summary.items():
            print(index, sentence)
            summaryResponse += sentence
            fout.write(sentence)
        fout.close()
        return sentences, summaryResponse
