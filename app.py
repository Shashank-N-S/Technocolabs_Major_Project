import numpy as np
import pandas as pd  
import sklearn
import tensorflow as tf 
import streamlit as st 

def load_data(file):
    data = pd.read_csv(file)
    return data

def load_model(model):
    loaded_model = tf.keras.models.load_model(model)
    return loaded_model

def app():
    st.markdown('<style>body{background-color: white ;}</style>',unsafe_allow_html=True)

    html_temp = """
        <div style = "background-color: lightblue ; padding: 10px;">
            <center><h1>SPOTIFY HIT PREDICTOR </h1></center>
        </div><br>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    danceability = st.number_input('Enter the DANCEABILITY score. Range:(0-1)')
    energy = st.number_input('Enter the ENERGY score. Range:(0 - 1)')
    key = st.number_input('Enter the KEY score. Range:(0 - 1)')
    loudness = st.number_input('Enter the LOUDNESS score. Range:(-50 - 0)')
    mode = st.number_input('Enter the MODE score. Range:(0 - 1)')
    speechiness = st.number_input('Enter the SPEECHINESS score. Range:(0 - 1)')
    acousticness = st.number_input('Enter the ACOUSTICNESS score. Range:(0 - 1)')
    instrumentalness = st.number_input('Enter the INSTRUMENTALNESS score. Range:(0 - 1)')
    liveness = st.number_input('Enter the LIVENESS score. Range:(0 - 1)')
    valence = st.number_input('Enter the VALENCE score. Range:(0 - 1)')
    tempo = st.number_input('Enter the TEMPO score. Range:(0 - 300)')
    duration_ms = st.number_input('Enter the DURATION_MS score. Range:(10000 - 10000000)')
    time_signature = st.number_input('Enter the TIME SIGNATURE score. Range:(0 - 5)')
    chorus_hit = st.number_input('Enter the CHORUS HIT score. Range:(0 - 300)')
    sections = st.number_input('Enter the SECTIONS score. Range:(1 - 200)')
    
    sample_data = [danceability, energy, key, loudness,
       mode, speechiness, acousticness, instrumentalness, liveness,
       valence, tempo, duration_ms, time_signature, chorus_hit,    
       sections]

    prep_data = np.array(sample_data).reshape(1, -1)

    decade = st.selectbox('Choose the decade for which you want to check the trend.',['1960s', '1970s', '1980s', '1990s', '2000s', '2010s'] )

    if st.button('PREDICT'):
        if decade == '1960s':
            predictor_60 = load_model('Trained_model_60')
            prediction_60 = predictor_60.predict(prep_data)
            result_60 = np.argmax(prediction_60)
            
            if result_60 == 0:
                st.error('THE SONG WITH ABOVE RATINGS WOULD BE A FLOP SONG.')

            elif result_60 == 1:
                st.success('THE SONG WITH ABOVE RATINGS WOULD BE A HIT SONG.')

        elif decade == '1970s':
            predictor_70 = load_model('Trained_model_70')
            prediction_70 = predictor_70.predict(prep_data)
            result_70 = np.argmax(prediction_70)
            
            if result_70 == 0:
                st.error('THE SONG WITH ABOVE RATINGS WOULD BE A FLOP SONG.')

            elif result_70 == 1:
                st.success('THE SONG WITH ABOVE RATINGS WOULD BE A HIT SONG.')

        elif decade == '1980s':
            predictor_80 = load_model('Trained_model_80')
            prediction_80 = predictor_80.predict(prep_data)
            result_80 = np.argmax(prediction_80)
            
            if result_80 == 0:
                st.error('THE SONG WITH ABOVE RATINGS WOULD BE A FLOP SONG.')

            elif result_80 == 1:
                st.success('THE SONG WITH ABOVE RATINGS WOULD BE A HIT SONG.')
            
        elif decade == '1990s':
            predictor_90 = load_model('Trained_model_90')
            prediction_90 = predictor_90.predict(prep_data)
            result_90 = np.argmax(prediction_90)
            
            if result_90 == 0:
                st.error('THE SONG WITH ABOVE RATINGS WOULD BE A FLOP SONG.')

            elif result_90 == 1:
                st.success('THE SONG WITH ABOVE RATINGS WOULD BE A HIT SONG.')
            
        elif decade == '2000s':
            predictor_00 = load_model('Trained_model_00')
            prediction_00 = predictor_00.predict(prep_data)
            result_00 = np.argmax(prediction_00)
            
            if result_00 == 0:
                st.error('THE SONG WITH ABOVE RATINGS WOULD BE A FLOP SONG.')

            elif result_00 == 1:
                st.success('THE SONG WITH ABOVE RATINGS WOULD BE A HIT SONG.')
            
        elif decade == '2010s':
            predictor_10 = load_model('Trained_model_10')
            prediction_10 = predictor_10.predict(prep_data)
            result_10 = np.argmax(prediction_10)
            
            if result_10 == 0:
                st.error('THE SONG WITH ABOVE RATINGS WOULD BE A FLOP SONG.')

            elif result_10 == 1:
                st.success('THE SONG WITH ABOVE RATINGS WOULD BE A HIT SONG.')
            

if __name__ == '__main__':
    app()