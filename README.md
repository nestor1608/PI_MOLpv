<!DOCTYPE html>
<html>
<head>
	<title>Proyecto Individual MLOdv</title>
	<style>
		body {
			text-align: center;
		}
		h1, h2 {
			text-align: center;
		}
	</style>
</head>
<body>
<img src='https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png'>
	<h1 style='align:center'> **PROYECTO INDIVIDUAL Nº1** </h1>
	<h2>SoyHenry Labs</h2>

<p><strong>Información personal</strong></p>
<p>Nombre: Nestor Javier Gentil</p>
<p>Correo: nestor_gentil@hotmail.com</p>
<p>Cohorte: 08</p>

## Planteo del Problema

Una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha!

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula 😭): Datos sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas…. 😩.


## Descripción del proyecto

Después de analizar los datos disponibles, me di cuenta de que no son maduros y no se han transformado. Además, no hay procesos automatizados para la actualización de nuevas películas o series

Por lo tanto, he realizado un trabajo de Data Engineer para tener un MVP (Minimum Viable Product) para la próxima semana.</p>

## Rol a desarrollar

En este proyecto, mi rol será el de Data Scientist, y también asumiré el papel de Data Engineer en la primera fase para preparar los datos. Mi objetivo es  la limpieza y transformacion de los datos obtenidos por la empresas y crear un modelo de Machine Learning eficiente que brinde un sistema de recomendacion personalizado a cada cliente que brinde una sensacion de acompañamiento personalizado. 
💻💪


:red_circle: **INICIO** :red_circle:

* **MLOpsReviews**: _Bases de datos recibidas_
* **main**: _Script que le da estructura a la API para que sea funcional_
* **limpieza_datos_movie**:  _Paso a paso detallado del proceso de ETL_
* **modelo_ML**: _Se crea el modelo de **Machine Learning** y una estructura para que el modelo sea funcinal_
* **app_streamlit**: _Se crea una muestra grafica de puesta en funcionamiento del modelo de **ML**_
* **conect**: _archivo que conecta a los datos_

:red_circle: **Funciones de la API:** :red_circle::

* Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
* Cantidad de películas por plataforma con filtro de PLATAFORMA
* Actor que más se repite según plataforma y año


**Para el deployment de la API, Render**

:link: https://nestor-pi-henry.onrender.com

:warning: **Algunas aclaraciones sobre las consultas** :warning:


* :white_check_mark: amazon, netflix, hulu y disney plus son las plataformas que acepta.

 ### **Herramientas utilizadas**

:small_orange_diamond: **[Python](https://www.python.org/)**: Lenguaje de programación, aplicado a lo ancho y largo del proyecto.

:small_orange_diamond: **[Pandas](https://pandas.pydata.org/)** : Pandas es una libreria escrita para el lenguaje Python para la manipulación y el análisis de datos.


:small_orange_diamond: **[Scikit-learn](https://scikit-learn.org/stable/)**: Scikir-learn es una libreria basada en Python para crear modelos de apredinzaje libre como machine learning y deep learning.

:small_orange_diamond: **[FastAPI](https://fastapi.tiangolo.com/)** : Framework para la construcción de la API en Python

:small_orange_diamond: **[Uvicorn](https://www.uvicorn.org/)** : Permite controlar el funcionamiento de la API de manera local.

:small_orange_diamond: **[Render](https://render.com)**
: plataforma online y gratuita, que nos permite realizar el deployment de nuestra API.

:small_orange_diamond: **[Streamlit](https://streamlit.io/)**: Streamlit nos sirve para darle una interfaz al modelo de recomendación y se pueda ver su funcinalidad.

 ## Modelo de recomendacion

Para la visualizacion del producto MLOps se desarrollo un modelo que prediga si una pelicula sera de su interes. El modelo arrojara como resultado si esa pelicula es recomendable para el cliente.

_¿Cuantas veces hacemos zapping por las plataformas y buscamos una pelicula que nos llame la atencion o que nos produzca algo al verla y que  **NO SEA UNA PERDIDA DE TIEMPO HABERLA VISTO**?_

_Cuantas veces buscamos recomendaciones de peliculas y pretendemos que sean buenas y que esa recomendacion no sea mala o una signifique perdida de tiempo_

## El modelo podria ser implementado tanto como para predecir como para sugerir

<img style='width:500px' src=_src/prueba_ml.png>
<img style='width:500px' src=_src/prueba_final_ml2.png>
<img style='width:500px ' src=_src/prueba_final_ml3.png>
<img style='width:500px' height:100px' src=_src/prueba_final_ml1.png>


### Contacto
* GitHub: :link: https://github.com/nestor1608
* Mail: nestor_gentil@hotmail.com

</body>
</html>