class MyClustering:
    def __init__(self, noClusters, input, similarity):
        """

        :type noClusters: the number of resulted clusters
        :param input: the input data represented as vector of vectors
        :param similarity: the similarity measure (eg. cosine, euclidean or a predefined method)
        :param linkage: the linkage function (eg. single, average, complete)
        """
        self.noClusters = noClusters
        self.input = input
        self.similarity = similarity
        self.roots = []
        self.treeDepth = []

    def mergeClustersSingle(self, x, y):
        """
        This method will join 2 clusters by finding the most close 2 clusters and merge them
        :return: the new resulted cluster's label array
        """
        if self.treeDepth[x] > self.treeDepth[y]:
            self.roots[y] = x
        else:
            self.roots[x] = y
            if self.treeDepth[x] == self.treeDepth[y]:
                self.treeDepth[y] += 1

    def getClusterRoot(self, x):
        """
        :param x: index of the current point
        :return: the root of the cluster in which self.input[x] is
        """
        root = x
        while self.roots[root] != root:
            root = self.roots[root]
        while self.roots[x] != x:
            s = self.roots[x]
            self.roots[x] = root
            x = s
        return root

    def normalize(self, x):
        """
        This method will normalize the result obtained in the single link clustering
        :param x: the roots of the clusters ([2, 2, 2, 2, 2, 7, 7, 7, 8, 7])
        :return: An array with the labels of the clusters from 0 to noClusters - 1
        """
        normalizedLabels = [-1 for _ in range(len(x))]
        maping = []
        for i in x:
            if i not in maping:
                maping.append(i)

        for i in range(self.noClusters):
            for j in range(len(x)):
                if x[j] == maping[i]:
                    normalizedLabels[j] = i
        return normalizedLabels

    def predict(self):
        """
        :return: returns the clusters' labels for each value from the data input
        """
        # each data point is a single cluster -> labels are 0, 1, 2, ... n-1
        self.roots = [i for i in range(0, len(self.input))]
        self.treeDepth = [1 for _ in range(0, len(self.input))]
        points = []
        for i in range(len(self.input)):
            for j in range(i + 1, len(self.input)):
                distance = self.similarity(self.input[i], self.input[j])
                points.append((distance, i, j))
        points.sort(key=lambda object: object[0])
        operations = len(self.input) - self.noClusters
        for distance, x, y in points:
            if self.getClusterRoot(x) != self.getClusterRoot(y):
                self.mergeClustersSingle(self.getClusterRoot(x), self.getClusterRoot(y))
                operations -= 1
            if operations == 0:
                break
        notNormalizedResult = []
        for i in range(len(self.input)):
            notNormalizedResult.append(self.getClusterRoot(self.roots[i]))
        normalizedResult = self.normalize(notNormalizedResult)
        return normalizedResult
