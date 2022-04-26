import streamlit as st

st.title('WIDGETS')

if st.button('Subscribe'):
    st.write('hello my name is jef')

name = st.text_input("Name")

st.write(name)

address = st.text_area("Enter your address")
st.write(address)

st.date_input('enter a date')

st.time_input('enter a time')

if st.checkbox("you accept the terms and conditions", value= False):
    st.write('thankyou')

v1 = st.radio('colors',['r','g','b'],index = 1)
v2 = st.selectbox('colors',['r','g','b'],index = 0)

st.write(v1,v2)

v3 = st.multiselect('colors',['r','g','b'])
st.write(v3)

st.slider('age', min_value=18, max_value=30, step = 2)

st.number_input('numbers', min_value=18, max_value=30, step = 2)
