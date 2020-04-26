def removeSentences(input, split):
    """
    This method removes the longest and the shortest sentences
    :param split: the split characters (. or'\n'). for testing purposes it's '\n'
    :param input: the file with the test
    :return: the left sentences that can be added in the summary
    """
    fin = open(input)
    text = fin.read()
    sentences = text.split(split)
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 30 or len(words) < 5:
            sentences.remove(sentence)
    return sentences
