<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

# <h1 align=center>**`Juan Pablo Carmona Alvarez`**</h1>

<p align="center">
<img src="https://files.realpython.com/media/What-is-Data-Engineering_Watermarked.607e761a3c0e.jpg"  height=300>
</p>

¡Bienvenidos al primer proyecto individual de la etapa de labs! En esta ocasión, deberán hacer un trabajo situándose en el rol de un ***Data Engineer***.  

<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Se debe crear una `Application Programming Interface` que funciona como puente entre dos aplicaciones para que se comuniquen entre sí.

En este caso usaremos **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.

<p align=center>
<img src = 'https://i.ibb.co/9t3dD7D/blog-zenvia-imagens-3.png' height=250><p>

## Rol a desarrollar

Como parte del equipo de data de una empresa, el área de análisis de datos le solicita a mi área de Data Engineering ciertos requerimientos para el óptimo desarrollo de sus actividades. debo elaborar las *transformaciones* requeridas y disponibilizar los datos mediante la *elaboración y ejecución de una API*.



## **Propuesta de trabajo**

**`Transformaciones`**:  Se realizaron las siguientes transformaciones a 4 csv's o base de datos de 4 plataformas distintas:


+ Cada archivo csv se tuvo que someter a crear una nueva columna llamada **`ID`** la cual tenia como dato la primera letra de la plataforma junto con el show_id (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating de cada archivo se tuvieron que remplazar por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”)

+ Las fechas inicialmente estaban en formato mes-dia-año, a lo que se transformaron en el formato **`AAAA-mm-dd`** para cada archivo csv

+ Todos los campos de texto de cada archivo se transformaron en **minúsculas**, sin excepciones

+ El campo ***duration*** fue convertido en dos campos: **`duration_int`** y **`duration_type`**. El primero en un integer y el segundo en un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:  Para entrelazar las consultas y los archivos csv o base de datos utilizamos el framework ***FastAPI***. Y le dimos a consultar lo siguiente:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating
<br/>


**`Deployment`**: En este caso para hacer el Deployment en FastAPI utilizamos Deta, esto nos permitio subir la API a un servidor para que el usuario la pueda usar
<br/>

<br/>
