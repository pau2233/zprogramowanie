from fastapi import FastAPI, Depends
from primePy import primes
import cv2
from datetime import datetime

from fastapi.security import HTTPBasic, HTTPBasicCredentials
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "By sprawdzić czy liczba jest pierwsza - http://localhost:8000/prime/10619863 lub https://zprogramowanie-grzanka.herokuapp.com/prime/10619863 " +
            " By odwrócić kolory obrazka  - http://127.0.0.1:8000/picture/invert/image.jpg"
            }

@app.get("/prime/{number}")
async def is_prime_number(number: int):
    if primes.check(number):  return {"message": f"Liczba {number} jest pierwsza"}
    else:
        return {"message": f"Liczba {number} nie jest pierwsza"}

image=cv2.imread('image.jpg')

@app.get("/picture/invert")
async def inverse_picture():

    newimage = ~image
    cv2.imwrite("img_inverted.jpg", newimage)
    return {"message": "Obrazek jest teraz nawiedzony"}




@app.get("/login")
async def user(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    time = datetime.now().strftime("%H:%M:%S")
    return {"message": f"Czas teraz {time} "}
