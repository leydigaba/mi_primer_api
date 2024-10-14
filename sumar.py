from fastapi import FastAPI

app = FastAPI()

@app.get("/sumar")
async def suma(num1: float, num2: float):
    resultado = num1 + num2
    return {
        "resultado": resultado
    }


