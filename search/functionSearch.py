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