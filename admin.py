from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)
admin = Admin(app, name='Админ-панель', template_mode='bootstrap3')

class Queries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cadastral = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Text, nullable=False)
    longitude = db.Column(db.Text, nullable=False)
    server_answer = db.Column(db.Text, nullable=False)


admin.add_view(ModelView(Queries, db.session))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных
    app.run(debug=True)