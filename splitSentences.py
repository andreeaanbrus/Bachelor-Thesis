from sentence import Sentence
import re


def splitSentences(input, split):
    """
    This method removes the longest and the shortest sentences
    :param split: the split characters (. or'\n'). for testing purposes it's '\n'
    :param input: the input file
    :return: the left sentences that can be added in the summary and their ids
    """
    input.replace('\n', '')
    for char in split:
        input = input.replace(char, '.')
    sentences_text = input.split('.')
    result = []
    for index, sentence in enumerate(sentences_text, start=1):
        result.append(Sentence(index, sentence))
    return result
