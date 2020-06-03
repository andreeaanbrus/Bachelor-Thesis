import math
from datetime import datetime

from clustering.myHierarchicalClustering import MyHierarchicalClustering
from clustering.myKMeans import MyKMeans
from clustering.similarity import euclidean, cosine, customSimilarity
from frequentTerms import termFrequency
from myutils import zero_vector, myround
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
        f = open(self.summary_file, 'w+')

        f.write(self.title)
        sentences_to_write = self.input_text.split('\n')
        for i in range(len(sentences_to_write)):
            f.write('S' + str(i + 1) + ': ' + sentences_to_write[i] + '\n')

        noClusters = 3
        if self.compression == 30:
            noClusters = int(myround(len(self.input_text.split('.')) * 0.3))
        if self.compression == 50:
            noClusters = int(myround(len(self.input_text.split('.')) * 0.5))
        start1 = datetime.now()
        (no_of_most_frequent_terms, most_frequent_terms, word_to_lemma, title_lemma) = termFrequency(self.input_text,
                                                                                                     self.title)
        f.write('\n-------------MOST FREQUENT TERMS-------------\n')
        for term in most_frequent_terms:
            f.write(term + ' ')
        f.write('\n')
        stop1 = datetime.now()
        print("Term frequency and lemmatization time: ", stop1 - start1)
        start2 = datetime.now()
        sentences = removeSentences(self.input_text, '.\n')
        mostFrequentTerms = most_frequent_terms[:no_of_most_frequent_terms]

        vectorRepresentationOfSentences(sentences, mostFrequentTerms,
                                        no_of_most_frequent_terms,
                                        word_to_lemma, title_lemma)
        f.write('\n-----------VECTOR REPRESENTATION-------------\n')
        for sentence in sentences:
            f.write('S' + str(sentence.id) + ': ' + str(sentence.representation) + '    with rank ' + str(
                sentence.rank) + '\n')
        stop2 = datetime.now()
        print("Vector representation time: ", stop2 - start2)

        # 5. Remove zero-vectors
        for sentence in sentences:
            if zero_vector(sentence.representation):
                sentences.remove(sentence)

        summary = ''
        summary_positions = []

        # 6.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}
        labels = None
        if self.method == 'hierarchical':
            start3 = datetime.now()
            cluster = MyHierarchicalClustering(noClusters=noClusters, similarity=cosine,
                                               input=[sentence.representation for sentence in sentences])
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
        if self.method == 'kmeans':
            f.write('\n-------CLUSTERS KMEANS--------\n')
        if self.method == 'hierarchical':
            f.write('\n-------CLUSTERS HIERARCHICAL-----\n')
        for i in range(noClusters):
            f.write('c' + str(i) + ' ')
            for sentence in sentences:
                if sentence.label == i:
                    f.write(str(sentence.id) + ', ')
            f.write('\n')

        # 7.Construct the summary
        summary_positions = [-100 for _ in range(noClusters)]
        summary_rank = [-100 for _ in range(noClusters)]
        for sentence in sentences:
            if sentence.rank > summary_rank[sentence.label]:
                summary_positions[sentence.label] = sentence.id
                summary_rank[sentence.label] = sentence.rank
        # sort the summary_positions to assure the chronological order of the sentences
        summary_positions.sort()
        print(summary_positions)  # <- the positions in the initial sentences

        if self.method == 'kmeans':
            f.write('\n-----LABELS---------\n')
            f.write(str(labels) + '\n')
            f.write('\n-----CENTROIDS------\n')
            for centroid in centroids:
                f.write(str(centroid) + '\n')
        for sentence in sentences:
            if sentence.id in summary_positions:
                summary += sentence.text
        f.close()
        # fout = open(self.summary_file, "w")  # write summary here
        # fout.write(summary)
        # fout.close()
        return sentences, summary, summary_positions
