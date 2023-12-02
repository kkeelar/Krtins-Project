from flask import Flask, request, jsonify
from flask_cors import CORS
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.stemmers import Stemmer
from nltk.corpus import stopwords
import traceback

from sumy.summarizers.lsa import LsaSummarizer

app = Flask(__name__)
CORS(app)

@app.route('/summarize', methods=['POST'])
def summarize_text():
    try:
        if not request.json or 'text' not in request.json:
            return jsonify({'error': 'No text provided'}), 400

        text_to_summarize = request.json['text']

        parser = PlaintextParser.from_string(text_to_summarize, Tokenizer('english'))
        stemmer = Stemmer('english')
        summarizer = LsaSummarizer(stemmer)
        summary = summarizer(parser.document, 4)

        summarized_text = ' '.join([str(sentence) for sentence in summary])
        
        return jsonify({'summary': summarized_text})

    except Exception as e:
        traceback_str = traceback.format_exc()
        app.logger.error(traceback_str)
        return jsonify({'error': 'Internal Server Error', 'trace': traceback_str}), 500

if __name__ == '__main__':
    app.run(debug=True)
