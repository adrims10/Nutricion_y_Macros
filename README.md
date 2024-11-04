# Proyecto4-Nutricion y Macros

![image](https://github.com/user-attachments/assets/8d0cb5a0-99b8-42df-a7a3-59b992f1da6e)

Bienvenidos! 

# *Es un placer recibirlos*


# 📝 En que consiste:

Hemos imaginado personas que necesitan un analisis de precios y rutinas diarias para empezar a estar en forma. Por lo que vamos a ofrecer 4 herramientas sencillas para que estas puedan inciarse en la nutricion y en el ejercicio siempre partiendo desde una base baja.

# Objetivos del proyecto:

Scraping de datos: Extraemos producto en la pagina de suplementos deportivos para optimizar el rendimiento deportivo y nuticional.
                   Extaer productos frescos de la pagina web de Ahorra Mas. 

Extracions de datos de la Api: Obtencion de datos de rutinas y recetas fitnes de las Apis.

Creacion de base de datos en Dbeaver llamada Salud.

Analisis de precios, reseñas de los productos, descuentos y creacion de rutinas y recetas personalizadas.

# Análisis de Datos:


## 🗂️ Estructura del Proyecto
Hemos creado un entorno llamado Webscraping para el siguiente proyecto.

        ├── notebooks/           # Notebooks de Jupyter donde se encontraran la limpieza de los datos y la visualizacion
                                  archivo de conclusiones y visualizacion : 6.Exploracion datos es el archivo de conclusiones y graficas
        ├── src/                 # Doportes de funciones
        ├─  Datos                # Datos obtenidos durante el estudio, csv y json
        ├── README.md            # Descripción del proyecto
        ├── README_English version.md   # Descripción del proyecto en ingles
      
## 🛠️ Instalación y Requisitos
        Este proyecto usa Python 3.12.6.
        **requests** - [Documentación de Requests](https://docs.python-requests.org/en/master/)
        **json** - [Documentación de JSON](https://docs.python.org/3/library/json.html)
        **pandas** - [Documentación de Pandas](https://pandas.pydata.org/pandas-docs/stable/)
        **sys** - [Documentación de sys](https://docs.python.org/3/library/sys.html)
        **os** - [Documentación de os](https://docs.python.org/3/library/os.html)
        **dotenv** - [Documentación de Python-dotenv](https://saurabh-kumar.com/python-dotenv/)
        **webdriver** - [Documentación de Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)
        **BeautifulSoup** - [Documentación de BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
        **numpy** - [Documentación de NumPy](https://numpy.org/doc/)
        **psycopg2** - [Documentación de Psycopg2](https://www.psycopg.org/docs/)

# 📝Webs:

  Pontemasfuerte: https://www.pontemasfuerte.com pagina de suplementos deportivos.
  
  Ahorramas: https://www.ahorramas.com/ pagina web de Ahorramas
  
 # 📝Apis:
 
   api-ninjas : Api rutinas de ejercicio.
   
   tasty : Api para recetas.
 
**Resultados , Conclusiones**
Hemos obtenido 9930 rutinas en la APi.
Hemos obtenido 120 productos completos dinamicos de la pagina web fuertisimo.
Hemos obtenido 62 productos completos dinamicos de la pagina web Ahorramas.
Hemos obtenido 30 recetas completas con la APi.

El precio medio de los suplementos deportivos en esta pagina es de 37,63 euros entrando en todas las categorias de los mismos.
          -Donde el precio medio de las proteinas es de 55.70 euros.
          -El precio medio de los BCAS es de 26.694 euros.
          -El precio medio de los L-Carnitone es es de 17.74 euros.
          -El precio medio de los Creatina es es de 30.73 euros.
          

El preciomaximo  de los suplementos deportivos en esta pagina es de 123.6 euros entrando en todas las categorias de los mismos.
          -Donde el precio medio de las proteinas es de 123.6 euros.
          -El precio medio de los BCAS es de 38.1 euros.
          -El precio medio de los L-Carnitone es es de 18.15 euros.
          -El precio medio de los Creatina es es de 53.9 euros.

Obteniendo como conclusion que el suplemento deportivo mas caro por categoria es la proteina, tambien teniendo en cuenta que es la que con mas frecuencia se usa y los formatos.


Con respecto al analisis de los productos frescos del Ahorra Mas encontramos precios medios sobre 10 euros, precios maximos de 27 euros y precios minimos de 1.39 donde encontramos alguna legumbre.
Observamos en esta seccion que tenemos un descuento de un cupon medio de un 18.5 por ciento. Por lo que los precios suelen bajar bastante.( Ver graficas comparativas en nootebook 6.


Como resultado de las APis hemos logrado un filtro para obtener recetas por tipos de ingredientes, por idiomas, o por servicio.
Y por otro lado con la APi de rutinas hemos conseguido rutinas especializadas a falta de actualizar la base de datos.
🌟

 
**Proximos pasos**

Introcuccion de rutinas desde la misma Api, niveles intermedios y mas grupos musculares.

Introduccion de mas productos tanto suplementos como productos frescos del ahorra mas solo con un click podemos aumentar la muestra, de momento no era objetivo del protecto.

Nueva Api de recetas puesto que la obtenida ha tenido problemas.

Crecimiento de la base de datos.

🏍️
![OIP](https://github.com/user-attachments/assets/a3261f22-9193-45df-bf33-14a396dfd988)
