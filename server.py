from flask import Flask, url_for, request

i = 0
app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def prom():
    text = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(text)


@app.route("/image_mars")
def img():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                    </p>Вот такая красивая планета.</p>
                  </body>
                </html>"""

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
