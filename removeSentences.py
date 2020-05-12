def removeSentences(input, split):
    """
    This method removes the longest and the shortest sentences
    :param split: the split characters (. or'\n'). for testing purposes it's '\n'
    :param input: the input file
    :return: the left sentences that can be added in the summary
    """
    sentences = input.split(split)
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 30 or len(words) < 5:
            sentences.remove(sentence)
    return sentences
