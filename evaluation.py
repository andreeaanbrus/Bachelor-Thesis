import math

from algorithm import Algorithm


def myround(x):
    decimal, integer = math.modf(x)
    if decimal >= 0.5:
        return integer + 1
    return integer


def testNumberSentences():
    for i in range(1, 13):
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
            if len(manual_extract_30_m) != noClusters30:
                print("Mami30: ", len(manual_extract_30_m) == noClusters30, " actual: ", noClusters30, "result: ",
                      len(manual_extract_30_m))
            if len(manual_extract_50_m) != noClusters50:
                print("Mami50: ", len(manual_extract_50_m) == noClusters50, " actual: ", noClusters50, "result: ",
                      len(manual_extract_50_m))
            if len(manual_extract_30_t) != noClusters30:
                print("Tati30: ", len(manual_extract_30_t) == noClusters30, " actual: ", noClusters30, "result: ",
                      len(manual_extract_30_t))
            if len(manual_extract_50_t) != noClusters50:
                print("Tati50: ", len(manual_extract_50_t) == noClusters50, " actual: ", noClusters50, "result: ",
                      len(manual_extract_50_t))


def main():
    sampleNo = '2'
    method = 'hierarchical'
    compression = 50
    inputFile = 'testdata/samples/sample' + sampleNo + '.txt'
    summaryFile = 'testdata/samples/summary-input' + sampleNo + '.txt'
    with open(inputFile) as f:
        title = next(f)
        input_text = f.read()
    algorithm = Algorithm(input_text, method, compression, summaryFile, title)
    sentences_algo, summaryResponse = algorithm.do()

    manual_extract_file = 'testdata/samples/AIS-summary' + sampleNo + '.txt'
    with open(manual_extract_file) as extract_file:
        manual_extract_30 = [int(number) for number in extract_file.readline().split(' ')]
        manual_extract_50 = [int(number) for number in extract_file.readline().split(' ')]
    print(manual_extract_30)
    print(manual_extract_50)

    sentences = input_text.split('.')
    manual_extract_sentences = [sentences[i - 1] for i in manual_extract_50]  # array starts from 0
    with open(summaryFile) as summaryFile:
        automatic_summary = summaryFile.read().split('.')
        print(automatic_summary)

    for s in manual_extract_sentences:
        print(s, s in automatic_summary)

    return

main()
