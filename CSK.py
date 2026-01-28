from flask import Flask, request, render_template_string

app = Flask(__name__)

цсл_словарь = {
    "выбор": "Избери дѣло:",
    "сложить": "сложити",
    "вычесть": "вычѧсти",
    "умножить": "умножити",
    "разделить": "раздѣлити",
    "результат": "исходъ",
    "ошибка": "грѣхъ въ вводѣ"
}

HTML = '''
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Калѯлаторъ</title></head>
<body>
    <h2>{{цсл_словарь['выбор']}}</h2>
    <form method="post">
        <input type="radio" name="action" value="1"> {{цсл_словарь['сложить']}}<br>
        <input type="radio" name="action" value="2"> {{цсл_словарь['вычесть']}}<br>
        <input type="number" step="any" name="a" placeholder="Число а" required><br>
        <input type="number" step="any" name="b" placeholder="Число в" required><br>
        <button type="submit">Испънити</button>
    </form>
    {% if result %}
        <h3>{{цсл_словарь['результат']}}: {{ result }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def главная():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            action = request.form.get('action')
            if action == '1':
                result = a + b
            elif action == '2':
                result = a - b
            else:
                result = цсл_словарь['ошибка']
        except:
            result = цсл_словарь['ошибка']
    return render_template_string(HTML, цсл_словарь=цсл_словарь, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
