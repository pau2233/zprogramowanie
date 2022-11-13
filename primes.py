# pip install fastapi
# pip install "uvicorn[standard]"
# uvicorn main:app --reload
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

from typing import Union
from fastapi import FastAPI
from primePy import primes

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "By sprawdzić czy liczba jest pierwsza - http://localhost:8000/prime/10619863"}

@app.get("/prime/{number}")
async isprimenum(number: int):
    if isprimenum(numb

       #     raise Exception ("Give a number above 0")

  #  return {"Is_numer_prime":primes.check(number)}

                  @ app.get("/prime/{nr}")


    def isprimenum(nr: int):
        # if nr<=0:
        #     raise Exception ("Give a number above 0")

        return {"Is_numer_prime": primes.check(nr)}