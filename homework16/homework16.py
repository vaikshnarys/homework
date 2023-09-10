import psycopg2
from flask import Flask, request

app = Flask(__name__)
conn = psycopg2.connect(dbname='facebook', user='postgres', password='1111')
USERS = [
    {
        'name': 'Oleg',
        'age': 23,
        'data': "1.02.2023"
    },
    {
        'name': 'Vasya',
        'age': 12,
        'data': "2.03.2023"
    },
    {
        'name': 'Alisa',
        'age': 29,
        'data': "3.04.2023"
    }
]


@app.get("/users")
def get_users():
    age = request.args.get('age')
    if age:
        new_users = list(filter(lambda user: user['age'] > int(age), USERS))
        # new_users = []
        # for user in USERS:
        #     if user['age'] > int(age):
        #         new_users.append(user)
        return new_users
    return USERS


@app.route("/users", methods=['GET'])
def get_users_list():
    filter = request.args.get('filter')
    limit = request.args.get('limit')
    cursor = conn.cursor()
    sql_create_database = f'select * from users where {filter} limit {limit}'
    cursor.execute(sql_create_database)
    rows = cursor.fetchall()
    print(rows)
    return 'print list with filter'


@app.route("/users", methods=['POST'])
def create_users():
    name = request.form.get('name')
    age = request.form.get('age')
    date_create = request.form.get('time')
    cursor = conn.cursor()
    sql_create_base = f'insert into users(name, age, date_create) values(%s, %s, %s)'
    add_user = cursor.execute(sql_create_base)
    conn.commit()
    print(add_user)
    return 'User created'


@app.route("/users/<user_id>", methods=['PUT'])
def update_users(user_id):
    name = request.form.get('name')
    age = request.form.get('age')
    date_create = request.form.get('time')
    cursor = conn.cursor()
    sql_create_base = f'update users set name = %s, age = %s, date_create = %s  where id = %s returning *'
    cursor.execute(sql_create_base, (name, int(age), date_create, int(user_id)))
    conn.commit()
    return 'User update'
