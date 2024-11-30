import sqlite3
import pandas as pd


# Функция для подключения к базе данных
def get_connection(db_name="example.db"):
    return sqlite3.connect(db_name)


# Функция для поиска по базе данных с несколькими критериями
def search_data(df, name=None, department_1=None, role=None, city=None, department_2=None, department_3=None,
                department_4=None, \
                functional_block=None, surName=None, number=None, address=None, post=None):
    # Стартуем с DataFrame
    filtered_df = df

    # Применяем фильтрацию по имени
    if name:
        filtered_df = filtered_df[filtered_df['Имя '].str.contains(name, case=False, na=False)]
    if surName:
        filtered_df = filtered_df[filtered_df['Фамилия '].str.contains(surName, case=False, na=False)]

    # Применяем фильтрацию по подразделению
    if department_1:
        filtered_df = filtered_df[filtered_df['Подразделение 1 '].str.contains(department_1, case=False, na=False)]
    if department_2:
        filtered_df = filtered_df[filtered_df['Подразделение 2'].str.contains(department_2, case=False, na=False)]
    if department_3:
        filtered_df = filtered_df[filtered_df['Подразделение 3'].str.contains(department_3, case=False, na=False)]
    if department_4:
        filtered_df = filtered_df[filtered_df['Подразделение 4'].str.contains(department_4, case=False, na=False)]

    # Применяем фильтрацию по городу
    if city:
        filtered_df = filtered_df[filtered_df['Город '].str.contains(city, case=False, na=False)]

    # Применяем фильтрацию по роли
    if role:
        filtered_df = filtered_df[filtered_df['Роль '].str.contains(role, case=False, na=False)]
    if post:
        filtered_df = filtered_df[filtered_df['Должность'].str.contains(post, case=False, na=False)]

    if functional_block:
        filtered_df = filtered_df[
            filtered_df['Функциональный блок '].str.contains(functional_block, case=False, na=False)]

    if number:
        filtered_df = filtered_df[filtered_df['Телефон '].str.contains(number, case=False, na=False)]

    if address:
        filtered_df = filtered_df[filtered_df['Адрес '].str.contains(address, case=False, na=False)]
    return filtered_df


# Функция для загрузки данных из базы данных SQLite в DataFrame
def load_data_from_db(db_name="example.db"):
    conn = get_connection(db_name)
    query = "SELECT * FROM people"  # Убедитесь, что такая таблица существует
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


# Функция для получения ввода от пользователя
def get_user_input():
    print("Введите критерии поиска (оставьте пустым для пропуска):")
    name = input("Имя: ")
    surName = input("Фамилия: ")
    department_1 = input("Подразделение 1: ")
    department_2 = input("Подразделение 2: ")
    department_3 = input("Подразделение 3: ")
    department_4 = input("Подразделение 4: ")
    city = input("Город: ")
    role = input("Роль: ")
    post = input("Должность: ")
    functional_block = input("Функциональный блок: ")
    number = input("Телефон: ")
    address = input("Адрес: ")

    return {
        'name': name or None,
        'surName': surName or None,
        'department_1': department_1 or None,
        'department_2': department_2 or None,
        'department_3': department_3 or None,
        'department_4': department_4 or None,
        'city': city or None,
        'role': role or None,
        'post': post or None,
        'functional_block': functional_block or None,
        'number': number or None,
        'address': address or None
    }


# Загружаем данные из базы данных в DataFrame
df = load_data_from_db()

# Получаем критерии поиска от пользователя
criteria = get_user_input()

# Пример использования функции поиска с введёнными критериями
result = search_data(df, **criteria)

# Печатаем результат
print(result)
