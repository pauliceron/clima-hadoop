# Proyecto Final T.E.Telemática

Este proyecto implementa un flujo completo de procesamiento de datos meteorológicos usando **Hadoop** y **MapReduce**, desplegado en Amazon EMR. Incluye la carga de datos a HDFS, su análisis mediante MapReduce en Python (con `mrjob`), y la visualización de resultados a través de una API desarrollada en **FastAPI**.

---

## Objetivo

Analizar las temperaturas mensuales en Medellín durante el año 2024, encontrando la temperatura máxima promedio por mes, usando procesamiento distribuido.

---

## Arquitectura del Proyecto

```plaintext
 +------------------+     +------------------------+     +--------------------+
 | Datos meteorol.  | --> | Carga manual a HDFS    | --> | Análisis con MRJob |
 | en CSV (local)   |     | (/user/admin/entrada)  |     | (MapReduce en Py)  |
 +------------------+     +------------------------+     +--------------------+
                                                            |
                                                            v
                                      +-----------------------------+
                                      | Resultados guardados en CSV |
                                      | y subidos a HDFS (/salida)  |
                                      +-----------------------------+
                                                            |
                                                            v
                                           +--------------------+
                                           | API FastAPI       |
                                           | Consulta resultados|
                                           +--------------------+
```

---

## Estructura del repositorio

```bash
clima-hadoop/
├── datos/
│   ├── entrada/                # CSV original con datos del clima
│   └── salida/                 # CSV de salida generado por MapReduce
├── mapReduce/
│   ├── max_temp_mes.py        # Script MapReduce con mrjob
│   ├── run_job.py             # Ejecuta el job y guarda CSV
├── api/
│   └── main.py                # API FastAPI para consultar resultados
├── requirements.txt           # Librerías necesarias
├── README.md                  # Este archivo
```

---

## Datos utilizados

Se usaron datos simulados del clima de Medellín para el año 2024, obtenidos de la api [weatherapi](https://www.weatherapi.com/) y estructurados en un archivo CSV con las siguientes columnas:

* `fecha`: en formato `YYYY-MM-DD`
* `temperatura_max`: temperatura máxima registrada ese día
* `temperatura_min`: temperatura máxima registrada ese día
* `precipitacion_mm`: precipitación medida en milímetros
* `condicion`: descripción generalizada del clima

---

## Ejecución del Job MapReduce

1. Instalar las dependencias necesearias desde el entorno virtual:

```bash
pip install -r requirements.txt
```

2. Ejecutar el procesamiento:

```bash
cd mapReduce
python run_job.py
```

3. El resultado es guardado en `datos/salida/max_temp_mes.csv`. Para fines de este proyecto, fue cargado manualmente a HDFS.

---

## Subida a HDFS

Desde Hue o consola Hadoop:

```bash
hdfs dfs -put datos/salida/max_temp_mes.csv /user/admin/salida/
```

---

## Ejecutar la API

```bash
cd api
uvicorn main:app --reload
```

Luego, se accede a `http://localhost:8000` para ver los endpoints disponibles.

---

## Video de sustentación

En el video se explica:

* Los datos usados y su origen
* El proceso de carga al sistema HDFS
* Cómo funciona el script de MapReduce en Python (usando `mrjob`)
* Los resultados obtenidos por mes
* La arquitectura general y cómo consultar resultados mediante la API
El video puede visualizarse [aqui](https://www.canva.com/design/DAGpGF2MLng/rt8eDs0YAKpPxP_qSrtE6A/edit?utm_content=DAGpGF2MLng&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
---

## Tecnologías usadas

* Hadoop (Amazon EMR)
* HDFS
* Python + MRJob
* FastAPI
* Hue
* Git + GitHub

---

## Autora

Paula Cerón
Proyecto final - Procesamiento Distribuido
Junio 2025
