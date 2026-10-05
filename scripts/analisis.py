# Análisis de la Práctica Individual N° 2
# Estudiante: MolinaCristhofer

import csv
import statistics
import os

# Obtener la carpeta principal del proyecto automáticamente.
# Así funciona correctamente aunque se ejecute desde VS Code/Debug.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARCHIVO = os.path.join(BASE_DIR, "datos", "datos.csv")

with open(ARCHIVO, newline="", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    datos = [float(fila["tiempo_servicio_min"]) for fila in lector]

n = len(datos)

media = statistics.mean(datos)
mediana = statistics.median(datos)
moda = statistics.multimode(datos)
desv_muestral = statistics.stdev(datos)
desv_poblacional = statistics.pstdev(datos)

minimo = min(datos)
maximo = max(datos)
rango = maximo - minimo

q1, _, q3 = statistics.quantiles(
    datos,
    n=4,
    method="inclusive"
)

print("=" * 50)
print("PRÁCTICA INDIVIDUAL N° 2")
print("Estudiante: MolinaCristhofer")
print("Análisis del tiempo de servicio en una farmacia")
print("=" * 50)

print("\nESTADÍSTICOS DESCRIPTIVOS")
print(f"Número de observaciones: {n}")
print(f"Media: {media:.2f} min")
print(f"Mediana: {mediana:.2f} min")
print(f"Moda: {moda}")
print(f"Desviación estándar muestral: {desv_muestral:.2f} min")
print(f"Desviación estándar poblacional: {desv_poblacional:.2f} min")
print(f"Mínimo: {minimo:.2f} min")
print(f"Máximo: {maximo:.2f} min")
print(f"Rango: {rango:.2f} min")
print(f"Q1: {q1:.2f} min")
print(f"Q3: {q3:.2f} min")

print("\nVALORES ATÍPICOS CON Z-SCORE")
print("Criterio: |Z| > 3")

for i, valor in enumerate(datos, start=1):
    z = (valor - media) / desv_poblacional

    if abs(z) > 3:
        print(
            f"Cliente {i}: {valor:.2f} min "
            f"| Z-Score = {z:.2f} <-- OUTLIER"
        )
    else:
        print(
            f"Cliente {i}: {valor:.2f} min "
            f"| Z-Score = {z:.2f}"
        )

print("\nCONCLUSIÓN")
print(
    "El tiempo de servicio habitual se encuentra alrededor de "
    f"{mediana:.2f} minutos."
)
print(
    "Se detectó un valor atípico que incrementa la media y "
    "la dispersión de los datos."
)
