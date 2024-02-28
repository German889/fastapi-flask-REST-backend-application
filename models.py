import sqlite3

def initialize_table():
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Queries (
    id INTEGER PRIMARY KEY,
    cadastral TEXT NOT NULL,
    latitude TEXT NOT NULL,
    longitude TEXT NOT NULL,
    server_answer TEXT NOT NULL
    )
    ''')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()