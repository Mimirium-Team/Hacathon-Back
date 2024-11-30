import pandas as pd
import sqlite3

# Чтение данных из Excel-файла
df = pd.read_excel('data.xlsx')

# Подключение к базе данных SQLite
conn = sqlite3.connect('example.db')

df.to_sql('people', conn, if_exists='replace', index=False)

# Запрос данных из таблицы
query = "SELECT * FROM people"
result = pd.read_sql_query(query, conn)

conn.close()
print(result)