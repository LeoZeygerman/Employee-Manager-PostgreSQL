import psycopg2
from models import Worker
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