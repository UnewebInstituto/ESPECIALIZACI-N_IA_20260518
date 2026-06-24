import pandas as pd

def limpiar_dataset(archivo_entrada, archivo_salida):
    # 1. Cargar el dataset
    try:
        df = pd.read_csv(archivo_entrada)
        print(f"Dataset cargado. Registros iniciales: {len(df)}")
        
        # 2. Eliminar duplicados
        df_limpio = df.drop_duplicates()
        print(f"Registros después de eliminar duplicados: {len(df_limpio)}")
        
        # 3. Eliminar registros nulos
        # Si una fila tiene al menos un valor nulo, se elimina
        df_limpio = df_limpio.dropna()
        print(f"Registros después de eliminar nulos: {len(df_limpio)}")
        
        # 4. Guardar el archivo limpio
        df_limpio.to_csv(archivo_salida, index=False)
        print(f"Archivo limpio guardado exitosamente como: {archivo_salida}")
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecutar la función
limpiar_dataset('ventas_30_registros.txt', 'ventas_limpio.csv')