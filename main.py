from fastapi import FastAPI
import aiohttp
import asyncio
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
import sqlite3
import models

app = FastAPI()

models.initialize_table()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.post("/query/")
async def query(cadastral_number:str, latitude:str, longitude:str):
    answer = 'no_answer'
    try:
        response = requests.post('http://localhost:12344/check', params={
            'cadastral_number': cadastral_number,
            'latitude': latitude,
            'longitude': longitude
        }, timeout=60)
        response.raise_for_status()  # Вызовет исключение, если статус ответа 4xx или 5xx

        if response.status_code == 200:
            if 'true' in response.json():
                answer = 'TRUE'
            else:
                answer = 'FALSE'
            print("server connected", cadastral_number)

        add_coordinates(cadastral_number, latitude, longitude, answer)

    except requests.exceptions.ConnectionError:
        # Обработка ошибки соединения
        print("Не удалось установить соединение с сервером.")
        add_coordinates(cadastral_number, latitude, longitude, answer)
    except requests.exceptions.Timeout:
        # Обработка ошибки таймаута
        print("Время ожидания соединения истекло.")
        add_coordinates(cadastral_number, latitude, longitude, answer)
    except requests.exceptions.HTTPError as err:
        # Обработка других HTTP ошибок
        print(f"HTTP ошибка: {err}")
        add_coordinates(cadastral_number, latitude, longitude, answer)

    return {'message':answer,'cadastral': cadastral_number, 'latitude': latitude, 'longitude': longitude}

@app.get("/result/")
async def result(cadastral_number:str):
    connection = sqlite3.connect('instance/my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT server_answer, latitude, longitude FROM Queries WHERE cadastral = ?',(cadastral_number,))
    result = cursor.fetchall()
    return result

@app.get("/ping/")
async def ping():
    url = 'http://localhost:12344/ping'
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=61) as response:
                if response.status == 200:
                    return {"status": "available"}
                else:
                    return {"status": "unavailable"}
        except aiohttp.ClientError:
            return response.text
            # return {"status": "unavailable"}

@app.get("/history/")
async def history():
    connection = sqlite3.connect('instance/my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Queries')
    result = cursor.fetchall()
    return result

async def fetch(session, url):
    async with session.get(url) as responce:
        return await responce.json()
    
def add_coordinates(cadastral_number, latitude, longitude, answer):
    connection = sqlite3.connect('instance/my_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Queries (cadastral, latitude, longitude, server_answer) VALUES (?, ?, ?, ?)', (cadastral_number, latitude, longitude, answer))
    connection.commit()
    connection.close()