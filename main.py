from flask import Flask, request, jsonify

app = Flask(__name__)

# Моя небольшая "база данных" приветствий
greetings_list = [
    {"id": 1, "name": "Алина", "text": "Привет! Это мой первый Flask проект"},
    {"id": 2, "name": "Гость", "text": "Добро пожаловать на мой сайт"}
]


@app.route('/')
def home():
    """Главная страница с информацией о API"""
    return jsonify({
        "project": "Flask Greeting Project",
        "author": "Alina Kazieva",
        "routes": {
            "home": "/",
            "greet": "/greet",
            "personal_greet": "/greet/<name>",
            "all_greetings": "/api/greetings"
        }
    })


@app.route('/greet')
def say_hello():
    """Простое приветствие"""
    # TODO: добавить больше вариантов приветствий
    return jsonify({
        "hello": "Привет! Я изучаю Python и Flask",
        "status": "working"
    })


@app.route('/greet/<name>')
def personal_greet(name):
    """Приветствие по имени"""
    return jsonify({
        "message": f"Привет, {name}! Рада знакомству 👋",
        "from": "Flask app by Alina"
    })


@app.route('/api/greetings', methods=['GET'])
def get_all_greetings():
    return jsonify({
        "count": len(greetings_list),
        "data": greetings_list
    })


@app.route('/api/greetings', methods=['POST'])
def create_greeting():
    """Добавить новое приветствие"""
    data = request.get_json()

    # Простая валидация
    if not data:
        return jsonify({"error": "Нет данных"}), 400

    if 'name' not in data:
        return jsonify({"error": "Обязательно укажите имя"}), 400

    new_id = max(item['id'] for item in greetings_list) + 1

    new_greeting = {
        "id": new_id,
        "name": data['name'],
        "text": data.get('text', 'Привет!')  # Если нет текста, ставим дефолтный
    }

    greetings_list.append(new_greeting)

    return jsonify(new_greeting), 201


# Запуск сервера
if __name__ == '__main__':
    print("🚀 Запускаю Flask сервер...")
    print("Открой http://localhost:5001 в браузере")
    app.run(debug=True, port=5001)


    @app.route('/about')
    def about():
        """Обо мне"""
        return jsonify({
            "name": "Alina Kazieva",
            "learning": ["Пайтон", "Фласк", "Алгоритмы", "SQL"],
            "goal": "Стать team leader 😁😁😁 Я буду стараться, очень очень сильно!"
        })