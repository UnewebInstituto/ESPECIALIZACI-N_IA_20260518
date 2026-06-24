import pandas as pd
import io

# Cargar los datos desde el contenido del archivo proporcionado
data = """numero_operacion,monto,producto,categoria
OP-1001,47008.55,Inversión,Financiero
OP-1001,47008.55,Inversión,Financiero
OP-1001,47008.55,Inversión,Financiero
OP-1001,47008.55,Inversión,Financiero
OP-1001,47008.55,Inversión,Financiero
OP-1001,47008.55,Inversión,Financiero
OP-1002,45515.55,Tarjeta de Crédito,Inversión
OP-1003,43072.64,Tarjeta de Crédito,Protección
OP-1004,3410.83,Préstamo Personal,Consumo
OP-1005,10780.69,Préstamo Personal,Financiero
OP-1006,45669.71,Cuenta de Ahorros,Inversión
OP-1007,33700.05,Tarjeta de Crédito,Protección
OP-1008,33616.86,Inversión,Consumo
OP-1009,13855.79,Seguro de Vida,Protección
OP-1010,11469.79,Tarjeta de Crédito,Consumo
OP-1011,41902.21,Cuenta de Ahorros,Ahorro
OP-1012,43548.56,Inversión,Ahorro
OP-1013,14908.28,Cuenta de Ahorros,Ahorro
OP-1014,42098.74,Seguro de Vida,Inversión
OP-1015,1217.24,Tarjeta de Crédito,Ahorro
OP-1016,43902.92,Tarjeta de Crédito,Consumo
OP-1017,47095.92,Cuenta de Ahorros,Inversión
OP-1018,17511.57,Préstamo Personal,Consumo
OP-1019,27552.32,Préstamo Personal,Inversión
OP-1020,21577.9,Cuenta de Ahorros,Inversión
OP-1021,20348.32,Cuenta de Ahorros,Financiero
OP-1022,7008.42,Cuenta de Ahorros,Consumo
OP-1023,43190.42,Inversión,Financiero
OP-1024,13670.8,Inversión,Consumo
OP-1025,345.88,Cuenta de Ahorros,Financiero
OP-1026,30141.21,Seguro de Vida,Ahorro
OP-1027,1267.52,Cuenta de Ahorros,Inversión
OP-1028,47344.2,Tarjeta de Crédito,Consumo
OP-1029,25653.93,Préstamo Personal,Inversión
OP-1030,37224.8,Tarjeta de Crédito,Inversión"""

# Convertir el string en un DataFrame
df = pd.read_csv(io.StringIO(data))

# 1. Eliminar registros duplicados
df_limpio = df.drop_duplicates()

# 2. Eliminar filas que contengan valores nulos (NaN)
df_limpio = df_limpio.dropna()

# Mostrar resultados
print("Dimensiones originales:", df.shape)
print("Dimensiones tras la limpieza:", df_limpio.shape)
print("\nPrimeras filas del conjunto limpio:")
print(df_limpio.head())