from random import sample

import numpy as np


def isIn(element, list):
    for list_element in list:
        if np.array_equal(element, list_element):
            return True
    return False


class MyKMeans:
    def __init__(self, noClusters, input, similarity):
        self.noClusters = noClusters
        self.input = input
        self.similarity = similarity
        self.labels = [None for _ in self.input]

    def initializeCentroids(self):
        """
        Randomly choose  initial clusters
        :return: The list of randomly chosen centroids
        """
        random_centroids = []
        random_positions = sample([i for i in range(len(self.input))], self.noClusters)
        for random_position in random_positions:
            random_centroids.append(self.input[random_position])
        return random_centroids

    def assignPointsToClusters(self):
        """
        Assigns all points to some cluster
        :return: the list of labels
        """
        for i in range(len(self.input)):
            self.assignPointToCluster(i, self.centroids)
        return self.labels

    def assignPointToCluster(self, point_i, centroids):
        """
        Assigns a point to a cluster
        :param point_i: the position of the point
        :param centroids: the list of possible centroids to be assigned to
        :return: -
        """
        min_i = -1
        min_dis = 1000000000
        for centroid in centroids:
            if self.similarity(self.input[point_i], centroid) < min_dis:
                min_dis = self.similarity(self.input[point_i], centroid)
                min_i = centroid
        self.labels[point_i] = min_i

    def meanOfClusters(self, centroids):
        """
        todo fix this method -> mean based on the computed clusters
        calculate the mean (centroid) of each cluster
        :return: the mean point of the cluster
        """
        means = []
        for centroid in centroids:
            pointsInCluster = []
            for i in range(len(self.labels)):
                if np.array_equal(self.labels[i], centroid):
                    pointsInCluster.append(self.input[i])
            means.append(np.mean(pointsInCluster, axis=0, dtype=int))
        return means

    def predict(self):
        """
        The method that performs the clustering algorithm
        :return: the list of labels and the centroids of the clusters
        """
        self.centroids = self.initializeCentroids()
        for i in range(200):
            old_centroids = self.centroids
            self.assignPointsToClusters()
            self.centroids = self.meanOfClusters(self.centroids)
            self.assignPointsToClusters()
            if np.array_equal(old_centroids, self.centroids):
                break
        normalized_labels = self.normalizeLabels(self.labels)
        return normalized_labels, self.centroids

    def normalizeLabels(self, labels):
        """
        The labels are represented by a point (of form [x1, x2, ... xn])
        :param labels: the list of labels
        :return: The normalized clusters (a value in the normalized vector is a natural number form 0 to noClusters)
        """
        normalizedLabels = [-1 for _ in range(len(labels))]
        maping = []
        for i in labels:
            if not isIn(i, maping):
                maping.append(i)
        for x in range(self.noClusters):
            for j in range(len(labels)):
                if np.array_equal(labels[j], maping[x]):
                    normalizedLabels[j] = x
        return normalizedLabels
