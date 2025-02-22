"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    import pandas as pd
    import os

    # Definir ruta de archivos
    input_file = "files/input/solicitudes_de_credito.csv"
    output_file = "files/output/solicitudes_de_credito.csv"

    # Eliminar archivo de salida si existe
    if os.path.exists(output_file):
        os.remove(output_file)

    # Cargar el archivo CSV
    df = pd.read_csv(input_file, sep=";", index_col=0, encoding="utf-8")

    # Definir columnas a limpiar
    columnas = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]

    # Normalizar texto en columnas clave
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].str.lower().str.strip().str.replace("_", " ").str.replace("-", " ").str.replace(",", "").str.replace("$", "").str.replace(".00", "").str.strip()

    # Limpiar idea_negocio
    df['idea_negocio'] = df['idea_negocio'].str.replace(' ', '_').str.replace('-', '_').str.strip('_')

    # Convertir estrato a entero
    df['estrato'] = df['estrato'].astype(int)

    # Normalizar barrio
    df['barrio'] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")

    # Convertir monto_del_credito a numérico
    df['monto_del_credito'] = pd.to_numeric(df["monto_del_credito"], errors="coerce")

    # Convertir comuna_ciudadano a entero
    df['comuna_ciudadano'] = pd.to_numeric(df["comuna_ciudadano"], errors="coerce", downcast="integer")

    # Convertir fecha_de_beneficio a formato datetime
    df['fecha_de_beneficio'] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    # Eliminar duplicados y valores nulos
    df = df.drop_duplicates()
    df = df.dropna()

    # Crear directorio de salida si no existe
    os.makedirs("files/output", exist_ok=True)

    # Guardar el archivo limpio
    df.to_csv(output_file, sep=';', index=False, encoding='utf-8')


pregunta_01()