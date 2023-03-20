import pandas as pd
from numpy import uint8

movie= pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/movie_clean.csv')

rating = pd.read_csv('https://objectstorage.sa-saopaulo-1.oraclecloud.com/n/gr4oj5h2hdd0/b/documentos/o/rating.csv',index_col='Unnamed: 0')

change_code= {'as943':'as942', 'as5894':'as5087', 'as9037': 'as4402', 'as9059':'as7296', 'as9270' :'as7054', 'ns6706':'ns304','ns7346':'ns160', 'ns8023':'ns1271'}

rating.movieId = rating.movieId.replace(change_code)

movie.date_added = pd.to_datetime(movie.date_added)

pelis = movie

"""creo rango de años"""

cortes= [1919,1960,1999,2022]
labels =['gold_cine','new_wave','2000']

pelis['interval_year'] = pd.cut(pelis.release_year,bins=cortes,labels=labels)

dum= pd.get_dummies(pelis.interval_year) # se  crea el dummies

pelis = pelis.drop(columns=['date_added','description','plataform','rating_x','cast','type','duration_type','interval_year','country'])

pelis= pd.concat([pelis,dum],axis=1) #se concatena

def new_column(char,columns):
  pelis.loc[pelis.listed_in.str.contains(char),[columns]] = 1

def new_column_w(chars,columns):
  for c in chars:
    pelis.loc[pelis.listed_in.str.contains(c),[columns]] = 1

entertainment=['variety','tv','interest','unscripted','reality','music','lifestyle','concert','culture','shows','family','cooking','travel','arts' ]
romance=['romance','romantic','lgbtq']
scifi=['sci-fi','fantasy','science fiction','superhero']
terror=['horror','thriller','thrillers','mystery','crime']
kid=['kids','kid','animation','cartoons']
document=['documentary','biographical','docuseries','documentaries']
drama=['drama','suspense','melodrama','romance','medical']
suspence=['suspense','western','survival','war']
sport=['sports','sport','fitness']
action=['western','thriller','superhero','military','war','action','espionage','sci-fi']
musical=['musical','concert','concerts']
lg=['lgbtq','lgbtq+']
comedy=['stand-up','parody','comedies','comedy']

new_column_w(romance,'romance')
new_column_w(entertainment,'entertainment')
new_column_w(scifi,'sci-fi')
new_column_w(terror,'thriller')
new_column_w(kid,'kid')
new_column_w(document,'documentary')
new_column_w(drama,'drama')
new_column_w(suspence,'suspense')
new_column_w(action,'action')
new_column_w(musical,'musical')
new_column_w(lg,'lgbtq')
new_column_w(comedy,'comedy')
new_column('anime','anime')

select=['comedy','drama','action',	'suspense',	'romance','entertainment','sci-fi',	'thriller',	'kid','documentary','musical','lgbtq','anime']


pelis[select]=pelis[select].fillna(0)
pelis=pelis.astype({
    'comedy':uint8,
    'drama':uint8,
    'action':uint8,	
    'suspense':uint8,	
    'romance':uint8,
    'entertainment':uint8,
    'sci-fi':uint8,	
    'thriller':uint8,	
    'kid':uint8,
    'documentary':uint8,
    'musical':uint8,
    'lgbtq':uint8,
    'anime':uint8})

pelis.drop(columns=['director','listed_in','title'],inplace=True)

sel= ['userId', 'movieId','release_year','duration_int','score','gold_cine','new_wave','2000','romance',	'entertainment','sci-fi','thriller','kid','documentary','drama','suspense','action','musical','lgbtq','comedy','anime','rating']

def export_peli():
  export = pelis
  return export





