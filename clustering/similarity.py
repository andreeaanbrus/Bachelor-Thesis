import math

import numpy as np
from sklearn.metrics import pairwise_distances


def customSimilarity(a, b):
    numerator = 0
    denominator = 0
    # len(a) == len(b)
    for i in range(len(a)):
        numerator += min(a[i], b[i])
        denominator += max(a[i], b[i])
        print(numerator, denominator, i)
    return numerator / denominator


def cosine(v1, v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y
    return sumxy / (math.sqrt(sumxx) * math.sqrt(sumyy))


def euclidean(x, y):
    res = 0
    for i in range(0, len(x)):
        res += (x[i] - y[i]) ** 2
    res = np.sqrt(res)
    return res
