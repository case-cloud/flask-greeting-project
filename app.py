from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    hour = now.hour
    
    if 6 <= hour <= 12:
        greeting = "Доброе утро"
    elif 13 <= hour <= 17:
        greeting = "Добрый день"
    elif 18 <= hour <= 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"
    
    user = "Гость"
    
    return render_template('index.html', greeting=greeting, user=user)

if __name__ == '__main__':
    app.run(debug=True)