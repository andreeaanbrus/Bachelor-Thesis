# Automatic Text Summarization in Romanian

## Summarization using clustering

### Input
A text that can be summarize in romanian. The length of the text should be at least 10-15 sentences.   

### Output
The summarized text

### Tools USED  
[NPL-CUBE](https://github.com/adobe/NLP-Cube)

### Run the app
1. create a virtual environment - venv
2. activate the environment
3. pip install -r requirements.txt
4. run the app

## Algorithm
###Steps
1. Calculate the frequency of the terms f(i, t).
2. Calculate the total frequency of the term T for all sentences.
3. Choose the first m most frequent terms (nouns and verbs).
4. Represent each sentence Si by m-vectors ```v[i] = {f(i, t1), f(i, t2), ... f(i, tm)}```.
5. Apply hierarchical clustering algorithm.
6. Build the summary: select from each cluster the sentence with minimal index, which does not belong to the summary and re-traverse the clusters applying the same selection rule until length L.

### Hierarchical Clustering Algorithm
 