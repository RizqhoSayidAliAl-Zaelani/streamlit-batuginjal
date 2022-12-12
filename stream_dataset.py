import pickle
import streamlit as st

# membaca model
dataset_model = pickle.load(open('dataset_model2.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Batu Ginjal Berdasarkan Test Urin')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    gravity = st.text_input ('input nilai gravity')

with col2 :
    ph = st.text_input ('input nilai ph')

with col1 :
    osmo = st.text_input ('input nilai osmo')

with col2 :
    cond  = st.text_input ('input nilai cond')

with col1 :
    urea = st.text_input ('input nilai urea')

with col2 :
    calc = st.text_input ('input nilai calc')

# code untuk prediksi
ginjal_diangnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi') :
    ginjal_prediction = dataset_model.predict([[gravity, ph, osmo, cond, urea, calc]])

    if(ginjal_prediction[0] == 1):
        ginjal_diangnosis = 'Pasien terkena batu ginjal'
    else :
        ginjal_diangnosis = 'Pasien tidak terkena batu ginjal'
    
    st.success(ginjal_diangnosis)