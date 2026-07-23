class Worker:
    def __init__(self,id,first_name,last_name,bday,post,salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.bday = bday
        self.post = post
        self.salary = salary
        
    def add_worker_models(self):
        print(f'==========\nИмя: {self.first_name}\nФамилия: {self.last_name}\nДата рождение: {self.bday}\nДолжность: {self.post}\nЗарплата: {self.salary}\n==========')
        
    def find_worker_models(self):
        print(f'==========\nID: {self.id}\nИмя: {self.first_name}\nФамилия: {self.last_name}\nДата рождение: {self.bday}\nДолжность: {self.post}\nЗарплата: {self.salary}\n==========')
        
    def show_all_models(self):
        print(f'========================================================================================================\nID: {self.id} | Имя: {self.first_name} | Фамилия: {self.last_name} | Дата рождение: {self.bday} | Должность: {self.post} | Зарплата: {self.salary}\n========================================================================================================')
        
    def delete_worker_models(self):
        print(f'Сотрудник {self.first_name} {self.last_name} удален!')
    
class Salary:
    def __init__(self, worker_id, type, amount, reason):
        self.worker_id = worker_id
        self.type = type
        self.amount = amount
        self.reason = reason
        
    def show_salary(self):
        print(f'===============\nID: {self.worker_id} | Тип: {self.type}\nРазмер: {self.amount}\nПричина: {self.reason}')
        
    def show_salary_all(self):
            print(f'=============================================\nID: {self.worker_id} | Тип: {self.type}\nРазмер: {self.amount}\nПричина: {self.reason}\n=============================================')