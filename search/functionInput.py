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