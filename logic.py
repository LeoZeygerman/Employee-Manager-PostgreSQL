from models import Worker
from database import add_employee_base, find_by_id

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
    print('2.Найти работника/ов по имени')
    choice = int(input('Ваш выбор: '))
    
    if choice == 1:
        worker_id = int(input('Введите ID пользователя: '))
        worker = find_by_id(worker_id)
        worker.find_worker_models()