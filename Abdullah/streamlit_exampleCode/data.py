import pandas as pd
import numpy as np
import streamlit as st
import time

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
disc = {
    "name" : "abdullah",
    "age" : 21,
    "city" : ["islamabad","Pakistan"]
}

data = pd.read_csv('Salary_Data.csv')
print(data)

st.dataframe(data)
st.table(a)
st.json(disc)
st.write(data)

@st.cache
def ret_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))