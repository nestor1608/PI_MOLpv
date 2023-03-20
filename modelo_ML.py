from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd 
import requests
import json


"""Funcion que transformara el JSON de las apis en DataFrame para su modelado """
def transfor_dataframe(url):
    data = json.loads(url.text)
    df = pd.DataFrame(data)
    return df

"""LLamada a  las Apis"""
url_movie = requests.get('https://nestor-pi-henry.onrender.com/data')
url_pelis = requests.get('https://suport-ml.onrender.com/peli_ml')

"""Funcion que retornara un aviso si algo en las llamadas de las Apis fallo"""
def call_api():
    if url_movie.status_code==200 and url_pelis.status_code==200:
        return f'se conecto correctamente a  las apis'
    else:
        return f'Ocurrio algun problema con las apis'


""" Se generan los datos tanto de la apis como del documento proveniente de Oracle cloud """

movie=transfor_dataframe(url_movie)
pelis=transfor_dataframe(url_pelis)
rating = pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/rating.csv',index_col='Unnamed: 0')

change_code= {'as943':'as942', 'as5894':'as5087', 'as9037': 'as4402', 'as9059':'as7296', 'as9270' :'as7054', 'ns6706':'ns304','ns7346':'ns160', 'ns8023':'ns1271'}

rating.movieId = rating.movieId.replace(change_code)
pelis.duration_int.fillna(0,inplace=True)

""" Genera y devuelve una lista de titulos unicos para que puedan ser usados en el Selectbox de streamlit"""
def title_movie():
    title= movie['title'].unique()
    return title

"""Filtra los datos para su usoen el modelo"""
def data_fit(user):
    df1= pelis[pelis.show_id.isin(rating[rating.userId==user].movieId)]
    df2= rating[rating.userId==user][['movieId', 'rating']]
    nuevo = pd.merge(df1,df2,left_on='show_id',right_on='movieId')
    if nuevo.shape[0]==0: return f'No se encontro el usuario'
    return nuevo.drop(columns=['movieId'])

""" Genera y entrena modelo y envia a la proxima funcion """
def model_predict(user):
    data = data_fit(user)
    X = data.drop(columns=['show_id','rating'])
    y= data["rating"]
    if X.shape[0] > 3 & X.shape[0] >= 11 :
        param_grid={'n_neighbors':[3,5,7,9,11], 'weights':['uniform','distance']}
        model= KNeighborsRegressor()
        grid= GridSearchCV(model,param_grid,cv=5)
        best = grid.fit(X,y)
        print(grid.best_estimator_)
    elif X.shape[0] < 9 & X.shape[0] > 3 :
        param_grid={'n_neighbors':[3,5,7], 'weights':['uniform','distance']}
        model= KNeighborsRegressor()
        grid= GridSearchCV(model,param_grid,cv=5)
        best = grid.fit(X,y)
    else:
        model= KNeighborsRegressor(n_neighbors=1)
        best = model.fit(X,y)
    return best

""" Esta funcion seleciona los id de las peliculas que el usuario ya vio para filtra la tabla de datos para cargar el modelo de machine learning"""
def select_movie(peli):
    id=movie[movie.title == peli]['show_id']
    result = pelis[pelis.show_id.isin(id.values)]
    return result


"""Funcion final donde predice el resultado y genera una respuesta """
def select_pelic(user,peli):
    model=model_predict(user)
    X = select_movie(peli)
    X = X.drop(columns=['show_id'])
    y_pred = model.predict(X)
    if (y_pred > 4):
        return f'Estoy seguro te gustara..!!'
    elif (y_pred >= 3.0 and y_pred < 3.9):
        return f'Podrias verla'
    else:
        return f'No creo que te guste'