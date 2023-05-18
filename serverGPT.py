from flask import Flask, request, jsonify
import openai

openai.api_key = 'your-openai-api-key'

app = Flask(__name__)

@app.route('/gpt', methods=['POST'])
def converse_with_gpt():
    prompt = request.json['prompt']
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )
    return jsonify(response['choices'][0]['text'].strip())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

