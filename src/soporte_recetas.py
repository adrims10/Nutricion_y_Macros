import requests
import pandas as pd
import json
import os
import dotenv 
dotenv.load_dotenv()
key = os.getenv("key")

def recetas(data):
    """ 
    Convierte los datos de recetas en un DataFrame de pandas.

    Args:
        data (list): Lista de diccionarios que contienen los datos de las recetas.

    Returns:
        DataFrame: Un DataFrame de pandas que contiene las recetas y sus campos.

    La función recibe una lista de diccionarios con los datos de las recetas.
    Luego, extrae los campos de interés para crear un DataFrame.
    Finalmente, guarda el DataFrame en un archivo CSV y lo devuelve.
    """
    data_list = []
    for result in data:
        compilations = result.get('compilations', [])
        for comp in compilations:
            data_list.append({
                'recipe_id': result.get('canonical_id'),
                'approved_at': result.get('approved_at'),
                'aspect_ratio': result.get('aspect_ratio'),
                'beauty_url': result.get('beauty_url'),
                'brand': result.get('brand'),
                'brand_id': result.get('brand_id'),
                'buzz_id': result.get('buzz_id'),
                'compilation_id': comp.get('id'),
                'compilation_name': comp.get('name'),
                'compilation_description': comp.get('description'),
                'created_at': comp.get('created_at'),
                'language': result.get('language'),
                'name': result.get('name'),
                'slug': result.get('slug'),
                'thumbnail_url': result.get('thumbnail_url'),
                'video_url': result.get('video_url'),
                'yields': result.get('yields')
            })
    
    # Crear un DataFrame con los datos
    df = pd.DataFrame(data_list)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv('../datos/recetas_data.csv', index=False)
    print("Datos guardados en 'datos/recetas_data.csv'")
    return df