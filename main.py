from fastapi import FastAPI
import pandas as pd

#https://n3xzky.deta.dev/docs

app = FastAPI()

# Primero creamos una función para cargar los archivos csv de las diferentes plataformas
def cargardf(valor):
    amazon='amazon'
    netflix ='netflix'
    disney='disney'
    hulu='hulu'
    archivos = [amazon,netflix,disney,hulu]
    df = pd.read_csv(netflix+".csv")
    if valor == "amazon":
      df = pd.read_csv(amazon+".csv")
    if valor == "hulu":
      df = pd.read_csv(hulu+".csv")
    if valor == "todos":
       lista_df = []
       for archivo in archivos:
            df1 = pd.read_csv(archivo+".csv")
            lista_df.append(df1)
       df = pd.concat(lista_df)
    return df

#La primera ruta es una ruta de bienvenida
@app.get("/")
def read_root():
    return {"Bienvenidos"}

#La segunda ruta es para buscar una palabra clave en la plataforma seleccionada
@app.get("/get_word_count/{plataforma}/{keyword}")
def get_word_count(plataforma: str, keyword: str):
    df = cargardf(plataforma)
    filtrar = df[df['title'].str.contains(keyword, na=False)]
    result = {plataforma, str(len(filtrar))}
    return result

#La tercera ruta es para buscar un puntaje especifico en un año especifico
@app.get("/get_score_count/{plataforma}/{score}/{year}")
def get_score_count(plataforma: str, score: float, year: int):
    df = cargardf(plataforma)
    filtro = df[(df['score'] > score) & (df['release_year'] == year)]
    result = {plataforma, str(len(filtro))}
    return result

#la cuarta ruta es para buscar la segunda mejor puntuacion de la pelicula de una plataforma especifica
@app.get("/get_second_score/{plataforma}")
def segunda_mejor_puntuacion(plataforma: str):
    peliculas = cargardf(plataforma)
    peliculas = peliculas[peliculas["type"]=="movie"]
    peliculas = peliculas.sort_values(by=['score', 'title'], ascending=[False, True])
    peli = peliculas.iloc[1]["title"]
    puntaje = peliculas.iloc[1]["score"]
    result = {str(peli), str(puntaje)}
    return result

#la quinta ruta es para ver la pelicula con mayor duracion en una plataforma especifica
@app.get("/get_longest/{plataforma}/{duration_type}/{año}")
def get_longest(plataforma: str, duration_type: str, año: int): 
    df = cargardf(plataforma) 
    df = df[(df['duration_type'] == duration_type) & (df['release_year'] == año) & (df['type'] == "movie")]
    df = df.sort_values('duration_int', ascending=False)
    title = df.iloc[0, 2]
    duration_int = df.iloc[0, 12]
    duration_type = df.iloc[0, 13]
    result = {"title": str(title), "duration_int": str(duration_int), "duration_type": str(duration_type)}
    return result

#La sexta ruta es para ver la cantidad de series y peliculas por rating
@app.get("/get_rating_count/18+")
def search_count_by_rating(rating: str):
    df = cargardf("todos")
    filtered_movies = df[df['rating'] == rating]
    count_movies = len(filtered_movies)
    filtered_series = df[df['rating'] == rating]
    count_series = len(filtered_series)
    result = {str(rating), str(count_movies), str(count_series)}
    return result
