import string


def vectorRepresentationOfSentences(sentences, most_frequent_terms, no_of_most_frequent_terms, word_to_lemma, title_lemma):
    """
    4. Represent each sentence Si by m-vectors v[i] = {f(i, t1), f(i, t2), ... f(i, tm)}.
    :param title_lemma:
    :param word_to_lemma:
    :param most_frequent_terms:
    :param no_of_most_frequent_terms:
    :param sentences:
    :return: the vectors
    """
    rank = [0 for _ in range(len(sentences))]
    vector_representation = [[0 for _ in range(no_of_most_frequent_terms)] for _ in range(len(sentences))]
    for i in range(len(sentences)):
        words = [word.strip(string.punctuation) for word in sentences[i].split()]
        words = [x for x in words if x]
        for k in range(len(words)):
            if words[k] in word_to_lemma.keys():
                if word_to_lemma[words[k]]['upos'] == 'PROPN':
                    rank[i] += 1
                if word_to_lemma[words[k]]['upos'] == 'PRON':
                    rank[i] -= 0.5
                if word_to_lemma[words[k]]['lemma'] in title_lemma:
                    rank[i] += 5
                for j in range(no_of_most_frequent_terms):
                    if word_to_lemma[words[k]]['lemma'] == most_frequent_terms[j]:
                        vector_representation[i][j] += 1
    return vector_representation, rank

