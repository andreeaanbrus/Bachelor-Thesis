from flask import Flask, json, request
from flask_cors import CORS

from algorithm import Algorithm

app = Flask(__name__)
CORS(app)


@app.route('/summarize-example/<int:input_id>/<string:method>/<int:compression>')
def summarize_example(input_id, method, compression):
    inputFile = 'testdata/samples/sample' + str(input_id) + '.txt'
    summaryFile = 'testdata/samples/summary-input' + str(input_id) + '.txt'
    with open(inputFile) as f:
        title = next(f)
        print(title)
        input_text = f.read()
        print(input_text)
    algorithm = Algorithm(input_text, method, compression, summaryFile, title)
    sentences, summaryResponse, summary_sentences_indexes = algorithm.do()
    res = {
        "title": title,
        "input": input_text,
        "summary": summaryResponse
    }
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json',
    )
    return response


@app.route('/summarize/<string:method>/<int:compression>', methods=['POST'])
def summarize(method, compression):
    summaryFile = 'testdata/samples/summary-input' + '.txt'
    print(request.data)
    print(request.get_json())
    title = request.get_json()['title']
    input_text = request.get_json()['input_text']
    algorithm = Algorithm(input_text, method, compression, summaryFile, title)
    sentences, summaryResponse, summary_sentences_indexes = algorithm.do()
    res = {
        "summary": summaryResponse
    }
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json',
    )
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
