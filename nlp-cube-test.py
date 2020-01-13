from cube.api import Cube

cube = Cube(verbose=True)

cube.load("ro")

fin = open('input.txt')
text = fin.read()
sentences = cube(text)
words = [{} for _ in range(0, len(sentences))]  # 1.calculating the frequency of the terms in each sentence f(i, t)
for i in range(0, len(sentences)):
    for entry in sentences[i]:
        print(entry)
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
        else:
            overAllFrequency[word] += words[i][word]

# 3. calculate the m most frequent terms
sortedTerms = {k: v for k, v in sorted(overAllFrequency.items(), key=lambda item: item[1], reverse=True)}
fout = open("output.txt", "w")
for key in sortedTerms.keys():
    fout.write(key + " " + str(sortedTerms[key]) + "\n")

fout.close()
