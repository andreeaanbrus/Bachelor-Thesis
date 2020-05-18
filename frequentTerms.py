from cube.api import Cube

cube = Cube(verbose=True)

cube.load("ro")


def termFrequency(input, title):
    titleForLemma = cube(title)
    title_lemma = []
    # sentence number is 1, but this is the nlp-cube documentation for lemmatization
    for sentence in titleForLemma:
        for entry in sentence:
            if entry.upos == "VERB" or entry.upos == "NOUN" or entry.upos == "PROPN":
                title_lemma.append(entry.lemma)
    sentences = cube(input)
    no_of_all_terms = 0
    nlp_word_to_lemma = dict()
    words = [{} for _ in range(0, len(sentences))]
    # 1.calculating the frequency of the terms in each sentence f(i, t)
    for i in range(0, len(sentences)):
        for entry in sentences[i]:
            if entry.upos != 'PUNCT':
                nlp_word_to_lemma[entry.word] = {'lemma': entry.lemma, 'upos': entry.upos}
            if entry.upos == "VERB" or entry.upos == "NOUN" or entry.upos == "PROPN":
                # only calculate the frequency of verbs and nouns and proper nouns
                if entry.lemma not in words[i]:
                    words[i][entry.lemma] = 1
                else:
                    words[i][entry.lemma] += 1
    # 2. calculate the sum of the frequencies of all terms computed at 1
    # sum(f(i, t), i = 1, n)
    overAllFrequency = {}
    for i in range(0, len(words)):
        for word in words[i].keys():
            if word not in overAllFrequency:
                overAllFrequency[word] = 1
                no_of_all_terms += 1
            else:
                overAllFrequency[word] += words[i][word]

    # 3. calculate the m most frequent terms
    # take the terms with frequency > 2
    most_frequent_terms_dict = {k: v for k, v in overAllFrequency.items() if v >= 2}
    # sort the terms
    sortedTerms = {k: v for k, v in sorted(most_frequent_terms_dict.items(), key=lambda item: item[1], reverse=True)}
    fout = open('termsFrequency.txt', "w")  # here are the frequencies of the terms
    for key in sortedTerms.keys():
        fout.write(key + " " + str(sortedTerms[key]) + "\n")
    most_frequent_terms = list(sortedTerms.keys())
    no_of_most_frequent_terms = len(most_frequent_terms)  # m
    fout.close()
    print(nlp_word_to_lemma)
    return no_of_most_frequent_terms, most_frequent_terms, nlp_word_to_lemma, title_lemma
