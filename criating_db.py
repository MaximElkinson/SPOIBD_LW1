from SQLTable import *

with open('cites.txt') as file:
    cites = file.read().split('\n')


db_config = {
    'user': 'j1007852',
    'password': 'el|N#2}-F8',
    'host': 'srv201-h-st.jino.ru',
    'database': 'j1007852_13423'
}

f = SQLTable(db_config, 'cites')
f.create_table({'name': 'text'})
for i in cites:
    f.insert_row({'name': f'{i}'})