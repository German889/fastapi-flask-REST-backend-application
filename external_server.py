from fastapi import FastAPI
import random
import time
app = FastAPI()


@app.post("/check/")
async def check(cadastral_number:str, latitude:str, longitude:str):
    answer_time = random.randint(1,60)
    time.sleep(answer_time)
    answer_type = random.randint(1,2)
    answer = 'false'
    if answer_type == 1:
        'true'
    return {"answer": answer}

@app.get("/ping/")
async def ping():
    # answer_time = random.randint(1,5)
    # time.sleep(answer_time)
    return {'status':'is_active'}