from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/inicio")
def read_root():
    return {"Hello": "adioss"}



@app.get("/incremento/{numero}")
def get_incremento(numero:int):
    numero = numero + 1
    return {
        "Resultado" : numero 
    }
    