from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI()

# Ruta local del archivo CSV de resultados
CSV_PATH = os.path.join("..", "datos", "salida", "max_temp_mes.csv")

@app.get("/")
def read_root():
    return {"message": "API del Clima - Resultados MapReduce"}

@app.get("/temperaturas-maximas")
def obtener_temperaturas():
    try:
        df = pd.read_csv(CSV_PATH, header=None)
        df.columns = ["mes", "temperatura_maxima"]
        resultados = df.to_dict(orient="records")
        return JSONResponse(content=resultados)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
