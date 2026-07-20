import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    database = 'employee-manager',
    user = 'postgres',
    password = '1234',
    port = '5432'
)
cur = con.cursor()

def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS employee(
        id BIGSERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        bday DATE,
        post VARVHAR(50),
        salary INTEGER)''')