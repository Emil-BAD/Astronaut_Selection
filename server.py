from flask import Flask, url_for, request

res_checkbox = list()
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


@app.route('/promotion_image')
def prom_img():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img width="700px" height="700px" src="{url_for('static', filename='img/mars.png')}"
                    alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-secondary" role="alert">
                          Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                          Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-light" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                    </html>'''


def check_box(value):
    global res_checkbox
    if len(res_checkbox) > 0:
        res_checkbox.clear()
    for i in value.split(', '):
        res_checkbox.append(f'''<div><input type="checkbox" name="prof" value="{i}">
        <label for="{i}">{str(i)}</label></div>''')
    return "".join(res_checkbox)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астонавтов</title>
                          </head>
                          <body>
                            <h2 align="center">Анкета прентендента</h2>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию"
                                    name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя"
                                    name="name">
                                    <p><p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                    placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="education" name="edu">
                                          <option>начальное</option>
                                          <option>основное</option>
                                          <option>среднее</option>
                                          <option>профессиональное</option>
                                          <option>среднее профессиональное</option>
                                          <option>бакалавриат</option>
                                          <option>специалитет</option>
                                          <option>подготовка кадров высшей квалификации</option>
                                        </select>
                                     </div>
                                     <p><p>
                                     <p>Какие у Вас есть профессии?<p>
                                     {check_box("инженер-исследователь, пилот, строитель, экзобиолог, врач,"
                                                "инженер по терраформированию, климатолог,"
                                                "специалист по радиационной защите, астрогеолог, гляциолог,"
                                                "инженер жизнеобеспечения, метеоролог, оператор марсохода,"
                                                "киберинженер, штурман, пилот дронов")}
                                     <p><p>
                                    <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                        <p></p>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="mission"></textarea>
                                    </div>
                                    <p></p>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                    <p></p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <p></p>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </div>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form['prof'])
        print(request.form['sex'])
        print(request.form['mission'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')