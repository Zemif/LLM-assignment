# main.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy Llama2 and Mistral classes for demonstration
class Llama2:
    def ask(self, query, context):
        # Implement Llama2 logic here
        return {'model': 'Llama2', 'query': query, 'response': 'Answer from Llama2'}

class Mistral:
    def ask(self, query, context):
        # Implement Mistral logic here
        return {'model': 'Mistral', 'query': query, 'response': 'Answer from Mistral'}

models = {
    'llama2': Llama2(),
    'mistral': Mistral()
}
context = {}

@app.route('/query', methods=['POST'])
def query():
    model_name = request.json.get('model')
    query_text = request.json.get('query')

    if model_name in models:
        response = models[model_name].ask(query_text, context.get(model_name))
        context[model_name] = response['response']  # Update context for next interaction
        return jsonify(response)
    else:
        return jsonify({'error': 'Model not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
