from database import create_table
from logic import add_employee
while True:
    try:
        create_table()
        print('===Employee-Manager===')
        print('1.Добавить сотрудника.')
        print('2.Найти сотруднкиа.')
        print('3.Показать всех сотрудников.')
        print('4.Добавить штраф/бонус.')
        print('5.Удалить сотрудника.')
        print('6.Выйти.')
        choice = int(input('Ваш выбор: '))
        
        if choice == 1:
            add_employee()
    except ValueError:
        print('Ошибка при вводе!')