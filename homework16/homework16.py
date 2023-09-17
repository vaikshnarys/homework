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
@app.route("/users/<user_id>", methods=['DELETE'])
def delete_users(user_id):
    cursor = conn.cursor()
    sql_create_base = f'delete from users where id = {user_id}'
    cursor.execute(sql_create_base, (int(user_id)))
    conn.commit()
    return 'Delete user'


@app.route("/alter_table", methods=['POST'])
def alter_table():
    cursor = conn.cursor()
    sql_create_base = f'alter table post add column post_id SERIAL;'
    cursor.execute(sql_create_base)
    conn.commit()
    return "Create column post_id"
@app.route("/update_post", methods=['PUT'])
def update_post_id():
    user_id = request.form.get('user_id')
    name = request.form.get('name')
    cursor = conn.cursor()
    sql_create_base = f"update post set name = '{name}', user_id = {user_id} where id = 1"
    cursor.execute(sql_create_base)
    conn.commit()
    return 'Update post_id'

@app.route("/alter_foreign_key", methods=['POST'])
def alter_table_post_id():
    cursor = conn.cursor()
    sql_create_base = f'alter table post add foreign key (user_id) references users(id)'
    cursor.execute(sql_create_base)
    conn.commit()
    return "Create constraint"
