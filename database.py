import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    database = 'employee-manager',
    user = 'postgres',
    password = '1234',
    port = '5432'
)
cur = con.cursor()