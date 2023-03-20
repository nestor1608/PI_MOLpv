import pandas as pd

def load_data():
  dataset = pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/movie_clean.csv')
  return dataset
