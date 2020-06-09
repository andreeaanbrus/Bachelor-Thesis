import string


def vectorRepresentationOfSentences(sentences, most_frequent_terms, no_of_most_frequent_terms, word_to_lemma,
                                    title_lemma):
    """
    4. Represent each sentence Si by m-vectors v[i] = {f(i, t1), f(i, t2), ... f(i, tm)}.
    :param title_lemma:
    :param word_to_lemma:
    :param most_frequent_terms:
    :param no_of_most_frequent_terms:
    :param sentences:
    :return: the vectors
    """
    for sentence in sentences:
        sentence.representation = [0 for _ in range(no_of_most_frequent_terms)]
        if sentence.id == 1:
            sentence.rank += 10  # first sentence is more important
        # 4. Remove the longest/shortest sentences (sentences over 20 words, under 10 words)
        words = [word.strip(string.punctuation) for word in sentence.text.split()]
        words = [x for x in words if x]
        if len(words) < 5 or len(words) > 30:
            sentence.rank -= 2
        for k in range(len(words)):
            if words[k] in word_to_lemma.keys():
                if word_to_lemma[words[k]]['upos'] == 'PROPN':
                    sentence.rank += 1
                if word_to_lemma[words[k]]['upos'] == 'PRON':
                    sentence.rank -= 0.5
                if word_to_lemma[words[k]]['lemma'] in title_lemma:
                    sentence.rank += 5
                for j in range(no_of_most_frequent_terms):
                    if word_to_lemma[words[k]]['lemma'] == most_frequent_terms[j]:
                        sentence.representation[j] += 1
