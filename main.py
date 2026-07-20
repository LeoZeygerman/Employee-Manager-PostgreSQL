from database import create_table
while True:
    try:
        print('===Employee-Manager===')
        print('1.Добавить сотрудника.')
        print('2.Найти сотруднкиа.')
        print('3.Показать всех сотрудников.')
        print('4.Добавить штраф/бонус.')
        print('5.Удалить сотрудника.')
        print('6.Выйти.')
    except ValueError:
        print('Ошибка при вводе!')