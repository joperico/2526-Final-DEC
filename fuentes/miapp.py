from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import os

app = FastAPI()

# La URL se construye para MariaDB usando pymysql
DATABASE_URL = os.getenv("DATABASE_URL",
                         "mysql+pymysql://user:pass@db:3306/dbname")

engine = create_engine(DATABASE_URL)


@app.get("/status")
def status():
    return {"message": "FastAPI Apellidos-Nombre v.6.0"}


@app.get("/check")
def check_db():
    try:
        # Intentamos una operación mínima
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "Conexión a la base de datos exitosa"}

    except OperationalError:
        return {
            "status": "Error",
            "details": "Error conexión con la base de datos."
        }

    except Exception:
        return {
            "status": "Error",
            "details": "Error interno del servidor."
        }
