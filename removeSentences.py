from sentence import Sentence


def removeSentences(input, split):
    """
    This method removes the longest and the shortest sentences
    :param split: the split characters (. or'\n'). for testing purposes it's '\n'
    :param input: the input file
    :return: the left sentences that can be added in the summary and their ids
    """
    sentences_text = input.split(split)
    result = []
    for index, sentence in enumerate(sentences_text, start=1):
        words = sentence.split()
        if 30 > len(words) > 5:
            result.append(Sentence(index, sentence))
    return result
