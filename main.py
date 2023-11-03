from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def respuesta():
    return{
        "estado": "Si da we "
    }

from routes import clientes

app.include_router(clientes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    

