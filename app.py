from flask import Flask, render_template, request
from SQLTable import *

app = Flask(__name__)

db_config = {
    'user': 'j1007852',
    'password': 'el|N#2}-F8',
    'host': 'srv201-h-st.jino.ru',
    'database': 'j1007852_13423'
}

f = SQLTable(db_config, 'cites')

@app.route('/', methods=['GET', 'POST'])
def editor():
    if request.method == 'POST':
        content = request.form.get('content')
        if content in list(f.select_rows_by_column_value('name', f'{content}')['name']):
            massage = 'Город с таким названием уже есть в базе'
        else:
            f.insert_row({'name': f'{content}'})
            massage = 'Город добавлен'

        # Здесь вы можете сохранить содержимое, если нужно
        return render_template('index.html', content=massage)
    return render_template('index.html', content='Введите город')


if __name__ == '__main__':
    app.run(debug=True)