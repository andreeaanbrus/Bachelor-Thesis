# Automatic Text Summarization in Romanian

## Summarization using clustering

### Input
A text that can be summarize in romanian. The length of the text should be at least 10-15 sentences.   

### Output
The summarized text

### Tools USED  
* [NPL-CUBE](https://github.com/adobe/NLP-Cube)
* [scikt-learn](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)

### Run the app
1. create a virtual environment - venv
2. activate the environment
3. pip install -r requirements.txt
4. run the app
5. Some test examples can be found in the `testdata` folder (`inputX.txt` is the input file, `summary-inputX.txt` is the final summary, `clusters-inputX.txt` is the list of the resulted cluster labels, `vectors-inputX.txt` is the list of vectors corresponding to the sentences)
## Algorithm
###Steps
1. Calculate the frequency of the terms f(i, t).
2. Calculate the total frequency of the term T for all sentences.
3. Choose the first m most frequent terms (nouns and verbs).
4. Remove the longest/shortest sentences.
5. Remove the sentences with 0 vector representation (they don't have common words and should not be in the summary)
6. Represent each sentence Si by m-vectors ```v[i] = {f(i, t1), f(i, t2), ... f(i, tm)}```.
7. Apply hierarchical clustering algorithm.
8. Build the summary: select from each cluster the sentence with minimal index, which does not belong to the summary and re-traverse the clusters applying the same selection rule until length L.

### Hierarchical Clustering Algorithm
 