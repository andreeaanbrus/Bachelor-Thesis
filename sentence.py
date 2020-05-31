class Sentence:
    def __init__(self, index, text):
        self.id = index
        self.text = text
        self.rank = 0
        self.representation = [0]
        self.label = -1

    def __str__(self):
        return "ID: " + str(self.id) + " Sentence: " + self.text + " Rank: " + str(self.rank) + '\n' + 'Representation: ' + str(self.representation) + '\n' + 'Label: ' + str(self.label) + '\n'
