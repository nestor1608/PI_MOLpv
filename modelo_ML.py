from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd 
from conect import data_rating
from trasform_data_ml import export_peli


pelis= pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/pelis.csv')
#rating = export_rating()
rating = data_rating() #pd.read_csv('rating.csv')#'https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/rating.csv',index_col='Unnamed: 0')

change_code= {'as943':'as942', 'as5894':'as5087', 'as9037': 'as4402', 'as9059':'as7296', 'as9270' :'as7054', 'ns6706':'ns304','ns7346':'ns160', 'ns8023':'ns1271'}
pelis.duration_int.fillna(0,inplace=True)
rating.movieId = rating.movieId.replace(change_code)
movie= pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/movie_clean.csv') 

def title_movie():
    title= movie['title'].unique()
    return title

def data_fit(user):
    df1= pelis[pelis.show_id.isin(rating[rating.userId==user].movieId)]
    df2= rating[rating.userId==user][['movieId', 'rating']]
    nuevo = pd.merge(df1,df2,left_on='show_id',right_on='movieId')
    if nuevo.shape[0]==0: return f'No se encontro el usuario'
    return nuevo.drop(columns=['movieId'])


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


"""Funcion final que ocupa las otras para saacar el resultado"""
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