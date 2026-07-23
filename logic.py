from models import Worker
from database import add_employee_base, find_by_id, find_by_name, show_all_base, delete_worker_base, add_fine_bonus_base, show_history_base

def add_employee():
    print('===Добавление сотрудника===')
    first_name = input('Введите имя сотрудника: ')
    last_name = input('Введите фамилию сотрудника: ')
    bday = input('Введите дату рождения в формате ГГГГ-ММ-ДД: ')
    post = input('Введите должность: ')
    salary = int(input('Введите зарплату сотрудника: '))
    worker = add_employee_base(first_name, last_name, bday, post, salary)
    worker.add_worker_models()
    
def find_worker():
    print('1.Найти работника по ID')
    print('2.Найти работника(ов) по имени')
    choice = int(input('Ваш выбор: '))
    
    if choice == 1:
        worker_id = int(input('Введите ID пользователя: '))
        worker = find_by_id(worker_id)
        worker.find_worker_models()
    elif choice == 2:
        worker_name = input('Введите имя работника(ов), которого(ых) хотите найти: ')
        workers = find_by_name(worker_name)
        for work in workers:
            work.find_worker_models()

def show_all():
    worker = show_all_base()
    for workers in worker:
        workers.show_all_models()

def delete_worker():
    worker_id = int(input('Введите ID пользователя, которого хотите удалить: '))
    worker = delete_worker_base(worker_id)
    worker.delete_worker_models()
    
def add_fine_bonus():
    worker_id = int(input('Введите ID сотрудника: '))
    print('1.Добавить штраф.')
    print('2.Добавить бонус.')
    print('3.Посмотреть историю штрафов/бонусов.')
    choice = int(input('Ваш выбор: '))

    if choice == 1:
        type = 'Штраф'
        amount = int(input('Введите размер штрафа: '))
        reason = input('Причина штрафа: ')
        salary = add_fine_bonus_base(worker_id, type, amount, reason)
        salary.show_salary()
    
    elif choice == 2:
        type = 'Бонус'
        amount = int(input('Введите размер бонуса: '))
        reason = input('Причина бонуса: ')
        salary = add_fine_bonus_base(worker_id, type, amount, reason)
        salary.show_salary()
    
    elif choice == 3:
        result = show_history_base()
        for total in result:
            total.show_salary_all()