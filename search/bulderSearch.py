from functionSearch import search_data
from functionInput import get_user_input
from downloadDB import load_data_from_db

# Загружаем данные из базы данных в DataFrame
df = load_data_from_db()

# Получаем критерии поиска от пользователя
criteria = get_user_input()

# Пример использования функции поиска с введёнными критериями
result = search_data(df, **criteria)

# Печатаем результат
print(result)
