import psycopg2
from psycopg2 import OperationalError, errorcodes, errors 
import numpy as np

import psycopg2
from psycopg2 import OperationalError, errorcodes

def conexion(nombre):
    """
    Establece una conexión con la base de datos PostgreSQL.

    Args:
        nombre (str): El nombre de la base de datos a la que se desea conectar.

    Returns:
        conexion (psycopg2.extensions.connection): Objeto de conexión a la base de datos PostgreSQL.

    La función intenta establecer una conexión con la base de datos PostgreSQL utilizando los parámetros proporcionados.
    Si se produce un error, se captura y se muestra un mensaje correspondiente dependiendo del tipo de error.
    """
    try:  
        conexion = psycopg2.connect(
            database=nombre,
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("La contraseña es erronea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexion")
        else:
            print(f"Ocurrió el error {e}")

    return conexion



def crear_tablas(conexion):
    """
    Crea las tablas necesarias en la base de datos proporcionada.

    Args:
        conexion (psycopg2.extensions.connection): Objeto de conexión a la base de datos PostgreSQL.
    
    La función crea las tablas 'ejercicios', 'productos_fit', 'productos_fresh', y 'recetas' en la base de datos.
    Las tablas 'productos_fit', 'productos_fresh', y 'recetas' están relacionadas mediante claves foráneas.
    """
    cursor = conexion.cursor()
    
    # Crear tabla ejercicios sin producto_id
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS ejercicios (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(300) NOT NULL,
        tipo VARCHAR(300),
        musculo VARCHAR(300),
        equipo VARCHAR(300),
        dificultad VARCHAR(300),
        instrucciones TEXT
    );
    ''')
    
    # Crear tabla productos_fit con referencia a ejercicios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos_fit (
        producto_id SERIAL PRIMARY KEY,
        tipo_producto VARCHAR(50) NOT NULL,
        Nombre VARCHAR(300) NOT NULL,
        Precio FLOAT,
        cantidad_reseñas FLOAT,
        descripcion TEXT,
        rating FLOAT,
        Peso FLOAT,
        Unidad VARCHAR(300),
        ejercicio_id INT REFERENCES ejercicios(id) ON DELETE CASCADE
    );
    ''')
    
    # Crear tabla productos_fresh
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos_fresh (
        id SERIAL PRIMARY KEY,
        producto_id INT NOT NULL REFERENCES productos_fit(producto_id) ON DELETE CASCADE,
        Nombre_y_peso VARCHAR(300) NOT NULL,
        Descuentos FLOAT,
        precio_actual FLOAT,
        precio_sin_descuento FLOAT
    );
    ''')
    
    # Crear tabla recetas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recetas (
        id SERIAL PRIMARY KEY,
        producto_id INT NOT NULL REFERENCES productos_fit(producto_id) ON DELETE CASCADE,
        nombre_compilacion VARCHAR(300),
        descripcion_compilacion TEXT,
        idioma VARCHAR(300),
        nombre VARCHAR(300) NOT NULL,
        slug VARCHAR(300),
        url_miniatura VARCHAR(600),
        url_video VARCHAR(600),
        rinde VARCHAR(300),
        numero_de_receta INTEGER
    );
    ''')
    
    # Confirmar los cambios y cerrar el cursor
    conexion.commit()
    cursor.close()
    print("Tablas creadas correctamente.")


def insertar_datos(df_productos_fit, df_productos_precios, df_recetas, df_ejercicios, conexion):
    """ Inserta datos en las tablas correspondientes en la base de datos PostgreSQL. 
    
    Args: df_productos_fit (DataFrame): DataFrame con los datos de la tabla productos_fit. 
df_productos_precios (DataFrame): DataFrame con los datos de la tabla productos_fresh. 
df_recetas (DataFrame): DataFrame con los datos de la tabla recetas. 
df_ejercicios (DataFrame): DataFrame con los datos de la tabla ejercicios. 
conexion (psycopg2.extensions.connection): Objeto de conexión a la base de datos PostgreSQL. 
La función inserta datos en las tablas 'ejercicios', 'productos_fit', 'productos_fresh' y 'recetas' en la base de datos. 
Se asegura de que los datos estén relacionados adecuadamente utilizando claves foráneas. """
    cursor = conexion.cursor()
    
    # 1. Inserción en ejercicios
    query_insercion_ejercicios = '''
    INSERT INTO ejercicios (nombre, tipo, musculo, equipo, dificultad, instrucciones)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
    '''
    id_ejercicios = []  # Lista para almacenar los ids de ejercicios insertados
    
    for fila in df_ejercicios[['nombre', 'tipo', 'musculo', 'equipo', 'dificultad', 'instrucciones']].values:
        cursor.execute(query_insercion_ejercicios, tuple(fila))
        id_ejercicio = cursor.fetchone()[0]  # Obtener el id del ejercicio insertado
        id_ejercicios.append(id_ejercicio)
    
    conexion.commit()
    
    # 2. Inserción en productos_fit
    query_insercion_productos = '''
    INSERT INTO productos_fit (tipo_producto, Nombre, Precio, cantidad_reseñas, descripcion, rating, Peso, Unidad, ejercicio_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING producto_id;
    '''
    
    producto_ids = []  # Lista para almacenar los ids de productos insertados
    
    for index, fila in df_productos_fit[['tipo_producto', 'Nombre', 'Precio', 'cantidad de reseñas', 'decripcion', 'rating', 'Peso', 'Unidad']].iterrows():
        if index < len(id_ejercicios):  # Asegurarse que hay un ejercicio_id correspondiente
            cursor.execute(query_insercion_productos, (*tuple(fila), id_ejercicios[index]))  # Asociar el ejercicio_id
            producto_id = cursor.fetchone()[0]  # Obtener el id del producto insertado
            producto_ids.append(producto_id)
    
    conexion.commit()
    
    # 3. Inserción en productos_fresh
    query_insercion_productos_precios = '''
    INSERT INTO productos_fresh (producto_id, Nombre_y_peso, Descuentos, precio_actual, precio_sin_descuento)
    VALUES (%s, %s, %s, %s, %s);
    '''
    
    for index, fila in df_productos_precios.iterrows():
        if index < len(producto_ids):  # Asegurarse que hay un producto_id correspondiente
            cursor.execute(query_insercion_productos_precios, (producto_ids[index], fila['Nombre y peso'], fila['Descuentos'], fila['precio_actual'], fila['precio_sin_descuento']))
    conexion.commit()
    
    # 4. Inserción en recetas
    query_insercion_recetas = '''
    INSERT INTO recetas (producto_id, nombre_compilacion, descripcion_compilacion, idioma, nombre, slug, url_miniatura, url_video, rinde, numero_de_receta)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    
    for index, fila in df_recetas.iterrows():
        if index < len(producto_ids):  # Asegurarse que hay un producto_id correspondiente
            cursor.execute(query_insercion_recetas, (producto_ids[index], fila['nombre_compilacion'], fila['descripcion_compilacion'], fila['idioma'], fila['nombre'], fila['slug'], fila['url_miniatura'], fila['url_video'], fila['rinde'], fila['numero_de_receta']))
    conexion.commit()
    
    cursor.close()
    print("Datos insertados en las tablas correspondientes.")