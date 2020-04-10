import unittest
from random import randrange

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances

from clustering.myClustering import MyClustering
from clustering.similarity import euclidean, cosine


def sim_affinity_euclidean(X):
    return pairwise_distances(X, metric=euclidean)


def sim_affinity_cosine(X):
    return pairwise_distances(X, metric=cosine)


class TestClustering(unittest.TestCase):

    def setUp(self) -> None:
        arrayLength = randrange(20)
        numberOfPoints = randrange(1000)
        self.inputData = []
        for i in range(numberOfPoints):
            self.inputData.append([randrange(100) for _ in range(arrayLength)])
        self.noClusters = 4

    def mapClusters(self, firstResult, secondResult):
        mapping = {x: -1 for x in range(self.noClusters)}
        for label in range(self.noClusters):
            for i in range(len(self.inputData)):
                if firstResult[i] == label:
                    mapping[label] = secondResult[i]
                    break
        return mapping

    def test_clustering_euclidean(self):
        cluster = AgglomerativeClustering(n_clusters=self.noClusters, linkage="single", affinity=sim_affinity_euclidean)
        cluster.fit_predict(self.inputData)
        sklearnLabels = []
        for i in cluster.labels_:
            sklearnLabels.append(i)

        myCluster = MyClustering(noClusters=self.noClusters, similarity=euclidean,
                                 input=self.inputData)
        cluster_labels = myCluster.predict()

        mapping = self.mapClusters(sklearnLabels, cluster_labels)
        for i in range(len(self.inputData)):
            self.assertEqual(mapping[sklearnLabels[i]], cluster_labels[i])

    def test_clustering_cosine(self):
        cluster = AgglomerativeClustering(n_clusters=self.noClusters, linkage="single", affinity=sim_affinity_cosine)
        cluster.fit_predict(self.inputData)
        sklearnLabels = []
        for i in cluster.labels_:
            sklearnLabels.append(i)

        myCluster = MyClustering(noClusters=self.noClusters, similarity=cosine,
                                 input=self.inputData)
        cluster_labels = myCluster.predict()

        mapping = self.mapClusters(sklearnLabels, cluster_labels)
        for i in range(len(self.inputData)):
            self.assertEqual(mapping[sklearnLabels[i]], cluster_labels[i])
