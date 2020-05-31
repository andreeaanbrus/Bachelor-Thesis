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
        sentences = removeSentences(self.input_text, '.')
        mostFrequentTerms = termsFrequency[:no_of_most_frequent_terms]

        vectorRepresentationOfSentences(sentences, mostFrequentTerms,
                                        no_of_most_frequent_terms,
                                        word_to_lemma, title_lemma)
        stop2 = datetime.now()
        print("Vector representation time: ", stop2 - start2)

        # 5. Remove zero-vectors
        for sentence in sentences:
            if zero_vector(sentence.representation):
                sentences.remove(sentence)

        # # 6.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}
        labels = None
        if self.method == 'hierarchical':
            start3 = datetime.now()
            cluster = MyHierarchicalClustering(noClusters=noClusters, similarity=cosine, input=[sentence.representation for sentence in sentences])
            labels = cluster.predict()
            stop3 = datetime.now()
            print("Clustering time: ", stop3 - start3)
        if self.method == 'kmeans':
            start3 = datetime.now()
            cluster = MyKMeans(noClusters=noClusters, input=[sentence.representation for sentence in sentences], similarity=euclidean)
            labels, centroids = cluster.predict()
            stop3 = datetime.now()
            print("Clustering time: ", stop3 - start3)
        for i in range(len(labels)):
            sentences[i].label = labels[i]
        for sentence in sentences:
            print(sentence)
        summary = ''
        summary_positions = [-100 for _ in range(noClusters)]
        summary_rank = [-100 for _ in range(noClusters)]
        for sentence in sentences:
            if sentence.rank > summary_rank[sentence.label]:
                summary_positions[sentence.label] = sentence.id
                summary_rank[sentence.label] = sentence.rank
        # sort the summary_positions to assure the chronological order of the sentences
        summary_positions.sort()
        print(summary_positions)  # <- the positions in the initial sentences
        for sentence in sentences:
            if sentence.id in summary_positions:
                summary += sentence.text
        fout = open(self.summary_file, "w")  # write summary here
        fout.write(summary)
        fout.close()
        return sentences, summary, summary_positions
