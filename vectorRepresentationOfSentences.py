import string


def vectorRepresentationOfSentences(sentences, mostFrequentTerms, no_of_most_frequent_terms, word_to_lemma):
    """
    4. Represent each sentence Si by m-vectors v[i] = {f(i, t1), f(i, t2), ... f(i, tm)}.
    :param mostFrequentTerms:
    :param no_of_most_frequent_terms:
    :param sentences:
    :return: the vectors
    """
    vector_representation = [[0 for _ in range(no_of_most_frequent_terms)] for _ in range(len(sentences))]
    for i in range(len(sentences)):
        words = [word.strip(string.punctuation) for word in sentences[i].split()]
        words = [x for x in words if x]
        print(words)
        # for s in nlp_cube_sentence:
        #     for entry in s:
        #         if entry.upos != 'PUNCT':
        #             nlp_word_to_lemma[entry.word] = entry.lemma
        for j in range(len(words)):
            if words[j] in word_to_lemma.keys():
                print(word_to_lemma[words[j]], words[j])
            else:
                print("Invalid key", words[j])
        for j in range(no_of_most_frequent_terms):
            for k in range(len(words)):
                if words[k] in word_to_lemma.keys():
                    if word_to_lemma[words[k]] == mostFrequentTerms[j]:
                        vector_representation[i][j] += 1
    return vector_representation
