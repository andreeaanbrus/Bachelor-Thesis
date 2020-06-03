from algorithm import Algorithm
from myutils import myround


def testNumberSentences():
    for i in range(1, 16):
        manual_extract_file_m = 'testdata/samples/AVM-summary' + str(i) + '.txt'
        manual_extract_file_t = 'testdata/samples/AIS-summary' + str(i) + '.txt'
        inputFile = 'testdata/samples/sample' + str(i) + '.txt'
        with open(manual_extract_file_m) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_m = [int(number) for number in extract_file.readline().split(' ')]
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_t = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_t = [int(number) for number in extract_file.readline().split(' ')]
        with open(inputFile) as f:
            title = next(f)
            input_text = f.read()
            print(len(input_text.split('.')) - 1)
            noClusters50 = myround((len(input_text.split('.')) - 1) * 0.5)
            noClusters30 = myround((len(input_text.split('.')) - 1) * 0.3)
            print(i)
            # if len(manual_extract_30_m) != noClusters30:
            print("Mami30: ", len(manual_extract_30_m) == noClusters30, " actual: ", noClusters30, "result: ",
                  len(manual_extract_30_m))
            # if len(manual_extract_50_m) != noClusters50:
            print("Mami50: ", len(manual_extract_50_m) == noClusters50, " actual: ", noClusters50, "result: ",
                  len(manual_extract_50_m))
            if len(manual_extract_30_t) != noClusters30:
                print("Tati30: ", len(manual_extract_30_t) == noClusters30, " actual: ", noClusters30, "result: ",
                      len(manual_extract_30_t))
            if len(manual_extract_50_t) != noClusters50:
                print("Tati50: ", len(manual_extract_50_t) == noClusters50, " actual: ", noClusters50, "result: ",
                      len(manual_extract_50_t))

# testNumberSentences()
def evaluate_pers1_vs_pers2_30():
    for i in range(1, 16):
        manual_extract_file_m = 'testdata/samples/AVM-summary' + str(i) + '.txt'
        manual_extract_file_t = 'testdata/samples/AIS-summary' + str(i) + '.txt'
        with open(manual_extract_file_m) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_m = [int(number) for number in extract_file.readline().split(' ')]
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_t = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_t = [int(number) for number in extract_file.readline().split(' ')]
        similar_30 = 0
        for item in manual_extract_30_t:
            if item in manual_extract_30_m:
                similar_30 += 1
        print((similar_30 * 100) / len(manual_extract_30_m))


def evaluate_pers1_vs_pers2_50():
    for i in range(1, 16):
        manual_extract_file_m = 'testdata/samples/AVM-summary' + str(i) + '.txt'
        manual_extract_file_t = 'testdata/samples/AIS-summary' + str(i) + '.txt'
        with open(manual_extract_file_m) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_m = [int(number) for number in extract_file.readline().split(' ')]
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_t = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_t = [int(number) for number in extract_file.readline().split(' ')]
        similar_50 = 0
        for item in manual_extract_50_t:
            if item in manual_extract_50_m:
                similar_50 += 1
        print((similar_50 * 100) / len(manual_extract_50_m))


def evaluate_30_HAC_PERS1():
    for i in range(1, 16):
        manual_extract_file_m = 'testdata/samples/AVM-summary' + str(i) + '.txt'
        input_text_file = 'testdata/samples/sample' + str(i) + '.txt'
        output_HAC_cosine = 'testdata/samples/' + str(i) + '_HAC_cosine_30.txt'
        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_m) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_30_HAC_cosine = Algorithm(input_text, 'hierarchical', 30, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_30 = algorithm_30_HAC_cosine.do()
        same_sentences = 0
        for item in summary_sentences_indexes_30:
            if item in manual_extract_30_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_30_m))


def evaluate_50_HAC_PERS1():
    for i in range(1, 16):
        manual_extract_file_m = 'testdata/samples/AVM-summary' + str(i) + '.txt'
        input_text_file = 'testdata/samples/sample' + str(i) + '.txt'
        output_HAC_cosine = 'testdata/samples/' + str(i) + '_HAC_cosine_50' + '.txt'
        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_m) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_50_HAC_cosine = Algorithm(input_text, 'hierarchical', 50, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_50 = algorithm_50_HAC_cosine.do()
        same_sentences = 0
        print("Automatic Summary ", str(i), summary_sentences_indexes_50)
        for item in summary_sentences_indexes_50:
            if item in manual_extract_50_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_50_m))


def evaluate_30_HAC_PERS2():
    for i in range(1, 16):
        manual_extract_file_t = 'testdata/samples/AIS-summary' + str(i) + '.txt'
        input_text_file = 'testdata/samples/sample' + str(i) + '.txt'
        output_HAC_cosine = 'testdata/samples/summary_HAC_cosine'
        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_30_HAC_cosine = Algorithm(input_text, 'hierarchical', 30, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_30 = algorithm_30_HAC_cosine.do()
        same_sentences = 0
        print("Automatic Summary ", str(i), summary_sentences_indexes_30)
        for item in summary_sentences_indexes_30:
            if item in manual_extract_30_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_30_m))


def evaluate_50_HAC_PERS2():
    for i in range(1, 16):
        manual_extract_file_t = 'testdata/samples/AIS-summary' + str(i) + '.txt'
        input_text_file = 'testdata/samples/sample' + str(i) + '.txt'
        output_HAC_cosine = 'testdata/samples/summary_HAC_cosine'
        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_50_HAC_cosine = Algorithm(input_text, 'hierarchical', 50, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_50 = algorithm_50_HAC_cosine.do()
        print("Automatic Summary ", str(i), summary_sentences_indexes_50)
        same_sentences = 0
        for item in summary_sentences_indexes_50:
            if item in manual_extract_50_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_50_m))


def evaluate_KMEANS_30_PERS1():
    for i in range(1, 16):
        print("Automatic Summary ", str(i))
        manual_extract_file_t = 'testdata/samples/AVM-summary' + str(i) + '.txt'
        input_text_file = 'testdata/samples/sample' + str(i) + '.txt'
        output_HAC_cosine = 'testdata/samples/' + str(i) + '_KMEANS_30.txt'
        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_50_HAC_cosine = Algorithm(input_text, 'kmeans', 30, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_50 = algorithm_50_HAC_cosine.do()
        same_sentences = 0
        for item in summary_sentences_indexes_50:
            if item in manual_extract_30_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_30_m))


def evaluate_KMEANS_30_PERS2():
    for i in range(1, 16):
        print("Automatic Summary ", str(i))
        manual_extract_file_t = 'testdata/samples/AIS-summary' + str(i) + '.txt'
        input_text_file =  'testdata/samples/sample' + '.txt'
        output_HAC_cosine = 'testdata/samples/' + str(i) + '_KMEANS.txt'

        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_50_HAC_cosine = Algorithm(input_text, 'kmeans', 30, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_50 = algorithm_50_HAC_cosine.do()
        same_sentences = 0
        for item in summary_sentences_indexes_50:
            if item in manual_extract_30_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_30_m))


def evaluate_KMEANS_50_PERS1():
    for i in range(7, 16):
        print("Automatic Summary ", str(i))
        manual_extract_file_t = 'testdata/samples/AVM-summary' + str(i) + '.txt'
        input_text_file = 'testdata/samples/sample' + str(i) + '.txt'
        output_HAC_cosine = 'testdata/samples/summary_HAC_cosine'
        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_50_HAC_cosine = Algorithm(input_text, 'kmeans', 50, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_50 = algorithm_50_HAC_cosine.do()
        same_sentences = 0
        for item in summary_sentences_indexes_50:
            if item in manual_extract_50_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_50_m))


def evaluate_KMEANS_50_PERS2():
    for i in range(1, 16):
        print("Automatic Summary ", str(i))
        manual_extract_file_t = 'testdata/samples/AIS-summary' + str(i) + '.txt'
        input_text_file = 'testdata/samples/sample' + str(i) + '.txt'
        output_HAC_cosine = 'testdata/samples/' + str(i) + '_KMEANS_50.txt'
        # read input file
        with open(input_text_file) as f:
            title = next(f)
            input_text = f.read()
        # read manual extract
        with open(manual_extract_file_t) as extract_file:
            manual_extract_30_m = [int(number) for number in extract_file.readline().split(' ')]
            manual_extract_50_m = [int(number) for number in extract_file.readline().split(' ')]
        algorithm_50_HAC_cosine = Algorithm(input_text, 'kmeans', 50, output_HAC_cosine, title)
        sentences, summaryResponse, summary_sentences_indexes_50 = algorithm_50_HAC_cosine.do()
        same_sentences = 0
        for item in summary_sentences_indexes_50:
            if item in manual_extract_50_m:
                same_sentences += 1
        print((same_sentences * 100) / len(manual_extract_50_m))


# evaluate_50_HAC_PERS2()
# evaluate_30_HAC_PERS2()
# evaluate_50_HAC_PERS1()
# evaluate_30_HAC_PERS1()
# while True:
# evaluate_KMEANS_30_PERS1()
# evaluate_KMEANS_30_PERS2()
# evaluate_KMEANS_50_PERS1()
evaluate_KMEANS_50_PERS2()
# pers2_50, pers1_30, pers1_50