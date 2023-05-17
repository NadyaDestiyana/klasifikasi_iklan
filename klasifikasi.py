import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('iklan.sav', 'rb'))

st.title('Prediksi User Menekan Iklan')

Daily_Time_Spent_on_Site = st.number_input('Waktu yang Dihabiskan Di Dalam Situs')
Age = st.number_input('Umur')
Area_Income = st.number_input('Rata-rata Pendapatan Wilayah User')
Daily_Internet_Usage = st.number_input('Rata-rata User Menggunakan Internet')
Male = st.number_input('Laki-laki (0: Tidak; 1: Ya)')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[Daily_Time_Spent_on_Site, Age, Area_Income, Daily_Internet_Usage, Male]])

    if(prediksi[0] == 0):
        prediksi = 'Pengguna Tidak Menekan Iklan'
    else:
        prediksi = 'Pengguna Menekan Iklan'
st.success(prediksi)