from models import Worker
from database import add_employee_base

def add_employee():
    print('===Добавление сотрудника===')
    first_name = input('Введите имя сотрудника: ')
    last_name = input('Введите фамилию сотрудника: ')
    bday = input('Введите дату рождения в формате ГГГГ-ММ-ДД: ')
    post = input('Введите должность: ')
    salary = int(input('Введите зарплату сотрудника: '))
    worker = add_employee_base(first_name, last_name, bday, post, salary)
    worker.add_worker_models()
    