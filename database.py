import psycopg2
from models import Worker, Salary
con = psycopg2.connect(
    host = 'localhost',
    database = 'employee-manager',
    user = 'postgres',
    password = '1234',
    port = '5432'
)
con.autocommit = True
cur = con.cursor()
cur.execute('''CREATE EXTENSION IF NOT EXISTS pgcrypto''')

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS employee(
        worker_id BIGSERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        bday DATE,
        post VARCHAR(50),
        salary INTEGER)''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS salary(
        worker_id INTEGER,
        type VARCHAR(5),
        amount INTEGER,
        reason VARCHAR(50))''')
    
def add_employee_base(first_name,last_name,bday,post,salary):
    cur.execute('''INSERT INTO employee(first_name,last_name,bday,post,salary) VALUES(%s, %s, %s, %s, %s)''', (first_name, last_name, bday, post, salary))
    worker = Worker(
        None,
        first_name,
        last_name,
        bday,
        post,
        salary
    )
    return worker

def find_by_id(worker_id):
    cur.execute('''SELECT * FROM employee WHERE worker_id = %s''', (worker_id,))
    for row in cur:
        worker = Worker(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        )
        return worker
    
def find_by_name(first_name):
    cur.execute('''SELECT * FROM employee WHERE first_name = %s''', (first_name,))
    workers = []
    for row in cur:
        worker = Worker(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        )
        workers.append(worker)
    return workers

def show_all_base():
    cur.execute('''SELECT * FROM employee''')
    workers = []
    for row in cur:
        worker = Worker(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        )
        workers.append(worker)
    return workers

def delete_worker_base(worker_id):
    cur.execute('''SELECT * FROM employee WHERE worker_id = %s''', (worker_id,))
    for row in cur:
        worker = Worker(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
        )
        cur.execute('''DELETE FROM employee WHERE worker_id = %s''', (worker_id,))
        return worker
    
def add_fine_bonus_base(worker_id, type, amount, reason):
    cur.execute('''INSERT INTO salary VALUES(%s,%s,%s,%s)''', (worker_id, type, amount, reason))
    cur.execute('''SELECT * FROM salary WHERE worker_id = %s''', (worker_id))
    for row in cur:
        sal = Salary(
            row[0],
            row[1],
            row[2],
            row[3]
        )
        return sal
    
def show_history_base(worker_id):
    cur.execute('''SELECT * FROM salary WHERE worker_id = %s''', (worker_id,))
    total = []
    for row in cur:
        sal = Salary(
            row[0],
            row[1],
            row[2],
            row[3]
        )
        total.append(sal)
    return total