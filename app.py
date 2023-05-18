from flask import Flask, request, jsonify
import openai
import os  # добавляем модуль os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_KEY")  # заменяем ваш API ключ на переменную окружения

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    message = data['message']

    response = openai.Completion.create(engine="text-davinci-002", prompt=message, max_tokens=60)
    
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)



