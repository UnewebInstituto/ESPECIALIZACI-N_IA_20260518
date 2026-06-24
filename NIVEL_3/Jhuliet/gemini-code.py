import pandas as pd

# Nombre del archivo a procesar
archivo_entrada = 'operaciones_ventas.txt'
archivo_salida = 'operaciones_ventas_limpio.txt'

try:
    # 1. Cargar el conjunto de datos
    df = pd.read_csv(archivo_entrada)
    
    print(f"Registros iniciales: {len(df)}")
    
    # 2. Eliminar duplicados
    df = df.drop_duplicates()
    
    # 3. Eliminar registros nulos
    df = df.dropna()
    
    print(f"Registros finales: {len(df)}")
    
    # 4. Guardar el archivo limpio (usando coma como separador y sin índice)
    df.to_csv(archivo_salida, index=False)
    print(f"Archivo limpio guardado exitosamente como: {archivo_salida}")

except FileNotFoundError:
    print("Error: El archivo no fue encontrado. Asegúrate de que el nombre sea correcto.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")