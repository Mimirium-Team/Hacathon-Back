import pandas as pd
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

##
# function append in db
def append_data(department_1, functional_block,department_2,department_3,department_4,post,role,surName, name, number, city, address, mail):
    cursor.execute(f'INSERT INTO users (Подразделение 1 ,Функциональный блок ,Подразделение 2,Подразделение 3,Подразделение 4,Должность,Роль ,Фамилия ,Имя ,Телефон ,Город ,Адрес ,Почта ) VALUES ({department_1}, {functional_block}, {department_2}, {department_3}, {department_4}, {post}, {role}, {surName}, {name}, {number}, {city}, {address}, {mail})')
    conn.commit()
    return conn

q = ''
w = ''
e = ''
r = ''
t = ''
y = 'Back end разработчик'
u = 'defs'
i = 'Тапков'
o = 'Олег'
p = '89826667752'
a = 'Moscow'
s = 'улица мира 32'
d = 'treq@mail.ru'
print(append_data(q,w,e,r,t,y,u,i,o,p,a,s,d))

