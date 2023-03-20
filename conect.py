import pandas as pd

def load_data():
  dataset = pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/movie_clean.csv')
  return dataset



# dt1 = pd.read_csv('./ratings/1.csv')
# dt2 = pd.read_csv('./ratings/2.csv')
# dt3 = pd.read_csv('./ratings/3.csv')
# dt4 = pd.read_csv('./ratings/4.csv')
# dt5 = pd.read_csv('./ratings/5.csv')
# dt6 = pd.read_csv('./ratings/6.csv')
# dt7 = pd.read_csv('./ratings/7.csv')
# dt8 = pd.read_csv('./ratings/8.csv')



def data_rating():
    #data=[dt1,dt2,dt3,dt4,dt5,dt6,dt7,dt8,]
    dataset = pd.read_parquet('rating.parquet') #pd.concat(data)
    return dataset