import requests
import csv
from datetime import datetime, timedelta

# Configuración de API
API_KEY = "007330b1b3b64bc1b8540600252805"
CIUDAD = "Medellín"
FECHA_INICIO = datetime(2024, 1, 1)
FECHA_FIN = datetime(2024, 12, 31)

# Creación de archivo CSV
with open('datos_clima_medellin_2024.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(["fecha", "temp_max", "temp_min", "precipitacion_mm", "condicion"])

    fecha_actual = FECHA_INICIO
    while fecha_actual <= FECHA_FIN:
        fecha_str = fecha_actual.strftime('%Y-%m-%d')
        print(f"Descargando datos de {fecha_str}...")

        url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={CIUDAD}&dt={fecha_str}"

        try:
            respuesta = requests.get(url)
            data = respuesta.json()

            # Extraer datos del día
            dia = data["forecast"]["forecastday"][0]["day"]
            condicion = dia["condition"]["text"]

            writer.writerow([
                fecha_str,
                dia["maxtemp_c"],
                dia["mintemp_c"],
                dia["totalprecip_mm"],
                condicion
            ])
        except Exception as e:
            print(f"Error en {fecha_str}: {e}")

        # Avanzar un día
        fecha_actual += timedelta(days=1)

print("Datos descargados y guardados en datos_clima_medellin_2024.csv")
