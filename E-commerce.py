import pandas as pd
import json

# Lee el archivo Excel; header=1 utiliza la segunda fila como encabezados
df = pd.read_excel("Lista ecommerce.xlsx", header=1)

# Convierte el DataFrame a una lista de diccionarios
json_data = df.to_dict(orient="records")

# Guarda el JSON en un archivo, con indentación para legibilidad
with open("ecommerce.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Archivo JSON generado: ecommerce.json")
