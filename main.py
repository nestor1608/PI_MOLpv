from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
import pandas as pd
from conect import load_data
import json


df = load_data()
df.date_added= pd.to_datetime(df.date_added)
app = FastAPI()

@app.get('/')
async def root():
    return RedirectResponse(url='/docs/')

@app.get('/data')
async def get_data():
    data = load_data()
    return JSONResponse(content=json.loads(data.to_json())) 

@app.get('/duration/{year}/{platform}/{duration_type}')
async def get_max_duration(year:int, platform:str, duration_type:str):
    select =df[(df.date_added.dt.year==year) & (df.plataform == platform) & (df.duration_type==duration_type)]
    result = select[select.duration_int== select.duration_int.max()]
    return f'La pelicula con mayor duracion en el año {year} en la plataforma {platform} es {result["title"].values[0]}'  #.to_json(orient="records", lines=True)

@app.get('/score/{platform}/{scored}/{year}')
async def get_score_count(platform:str, scored:float, year:int):
    select =df[(df.plataform == platform) & (df.date_added.dt.year==year) &(df.score >= scored)]
    return {'Cantidad': len(select)}

@app.get('/plataform/{platform}')
async def get_count_platform(platform:str):
    select = df[df.plataform == platform]
    return f'Hay {str(len(select))} peliculas cargadas en la plataforma {platform}' 

@app.get('/actor/{platfor}/{year}')
async def get_actor(platform:str, year:int):
    select = df[(df.plataform == platform) & (df.date_added.dt.year==year)]
    aux= []
    for i in select.cast:
        if isinstance(i,str):
            gen = i.split(',')
            for c in gen:
                aux.append(c.strip())
    return f'Actor que mas se repite en esta seleccion es {pd.Series(aux).value_counts().index[0]}'


