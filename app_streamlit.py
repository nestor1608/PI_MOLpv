import streamlit as st
import pandas as pd 
from modelo_ML import title_movie, select_pelic,call_api



st.title('Recomendador de películas')
st.write(call_api())

# Pide al usuario que ingrese el ID de usuario
user_id = st.number_input('ID de usuario', min_value=0, max_value= 115077)# df['id_usuario'].max())

# Pide al usuario que ingrese la película
movies = title_movie()
movie = st.selectbox('Película', movies)
if st.button('Me Gustara?'):

    result = select_pelic(user_id,movie)
# Si no se encuentra ninguna fila, muestra un mensaje de error
    if not result:
        st.error('Hubo algun error')
    else:
        st.success(result)
    
