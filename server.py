from datetime import datetime

from flask import Flask, jsonify, json, request
from flask_cors import CORS
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import pairwise_distances

from clustering.myHierarchicalClustering import MyHierarchicalClustering
from clustering.myKMeans import MyKMeans
from clustering.similarity import cosine, customSimilarity, euclidean
from frequentTerms import termFrequency
from myutils import zero_vector
from removeSentences import removeSentences
from vectorRepresentationOfSentences import vectorRepresentationOfSentences

app = Flask(__name__)
CORS(app)


def sim_affinity_cosine(X):
    return pairwise_distances(X, metric=cosine)


def algorithm(input_text, method, compression, summary_file, title):
    noClusters = 3
    if compression == 30:
        noClusters = int(len(input_text.split('.')) * 0.3)
    if compression == 50:
        noClusters = int(len(input_text.split('.')) * 0.5)
    print(noClusters)
    start1 = datetime.now()
    (no_of_most_frequent_terms, termsFrequency, word_to_lemma, title_lemma) = termFrequency(input_text, title)
    stop1 = datetime.now()
    print("Term frequency and lemmatization time: ", stop1 - start1)
    start2 = datetime.now()
    # 4. Remove the longest/shortest sentences (sentences over 20 words, under 10 words)
    sentences = removeSentences(input_text, '.')
    mostFrequentTerms = termsFrequency[:no_of_most_frequent_terms]

    vectorRepresentation, rank = vectorRepresentationOfSentences(sentences, mostFrequentTerms, no_of_most_frequent_terms,
                                                           word_to_lemma, title_lemma)
    stop2 = datetime.now()
    print("Vector representation time: ", stop2 - start2)

    # 5. Remove zero-vectors
    for vector in vectorRepresentation:
        if zero_vector(vector):
            vectorRepresentation.remove(vector)
    # 6.Apply the hierarchical clustering algorithm for T = {S1; … ; Sn}
    labels = None
    if method == 'hierarchical':
        start3 = datetime.now()
        cluster = MyHierarchicalClustering(noClusters=noClusters, similarity=cosine, input=vectorRepresentation)
        labels = cluster.predict()
        stop3 = datetime.now()
        print("Clustering time: ", stop3 - start3)
    if method == 'kmeans':
        start3 = datetime.now()
        cluster = MyKMeans(noClusters=noClusters, input=vectorRepresentation, similarity=euclidean)
        labels, centroids = cluster.predict()
        stop3 = datetime.now()
        print("Clustering time: ", stop3 - start3)
    summary = {}
    i = 0
    j = 0
    while j < noClusters:
        while i < len(sentences):
            if labels[i] == j:
                # for now, pick the first sentence from the cluster
                # todo add some wights to the sentences later
                # TODO THIS IS THE I AFTER REMOVING SENTENCES, the sentences are correct, the indexes are not
                summary[i] = sentences[i]
                break
            i += 1
        j += 1
        i = 0
    summaryResponse = ''
    fout = open(summary_file, "w")  # write summary here
    for index, sentence in summary.items():
        summaryResponse += sentence
        fout.write(sentence)
    fout.close()
    return sentences, summaryResponse


@app.route('/summarize-example/<int:input_id>/<string:method>/<int:compression>')
def summarize_example(input_id, method, compression):
    inputFile = 'testdata/samples/sample' + str(input_id) + '.txt'
    summaryFile = 'testdata/samples/summary-input' + str(input_id) + '.txt'
    with open(inputFile) as f:
        title = next(f)
        print(title)
        input_text = f.read()
        print(input_text)
    sentences, summaryResponse = algorithm(input_text, method, compression, summaryFile, title)
    res = {
        "title": title,
        "input": input_text,
        "summary": summaryResponse
    }
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json',
    )
    return response


@app.route('/summarize/<string:method>/<int:compression>', methods=['POST'])
def summarize(method, compression):
    summaryFile = 'testdata/samples/summary-input' + '.txt'
    print(request.data)
    print(request.get_json())
    title = request.get_json()['title']
    input_text = request.get_json()['input_text']
    sentences, summaryResponse = algorithm(input_text, method, compression, summaryFile, title)
    res = {
        "summary": summaryResponse
    }
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json',
    )
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
