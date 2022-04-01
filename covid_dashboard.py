import pandas as pd
import streamlit as st
import matplotlib_inline as plt

confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv', on_bad_lines='skip')
death = pd.read_csv('time_series_covid19_deaths_global.csv', on_bad_lines='skip')
recovered = pd.read_csv('time_series_covid19_recovered_global.csv', on_bad_lines='skip')


print(confirmed.shape)
print("Hello")

print(confirmed.head())
