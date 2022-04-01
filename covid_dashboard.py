import pandas as pd
import streamlit as st
import matplotlib as plt

st.write('''
    # Covid Dashboard
    Hello :wave:  For our *open-source* project, we created an interactive **Covid-19** dashboard 
    that allows users to visualize the number of  Covid-19 cases or deaths per country 
    as a function of time
    ![](https://media.giphy.com/media/idShevOa24HzYTgz06/giphy.gif)

''')

confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv', on_bad_lines = 'skip')
death = pd.read_csv('time_series_covid19_deaths_global.csv', on_bad_lines = 'skip')
recovered = pd.read_csv('time_series_covid19_recovered_global.csv', on_bad_lines = 'skip')

st.sidebar.checkbox("Show Analysis by State", True, key=1)
select = st.sidebar.selectbox('Select a State',confirmed['Country/Region'])

def simpleGraph():
  fig=plt.figure(figsize=(14,6))
  plt.title("Death toll")
  plt.xticks(rotation=90)
  plt.xlabel("Date", fontsize=8)
  plt.ylabel("Total deaths per million", fontsize=8)
  #sns.lineplot(data=data['total_deaths'])
  return fig



# print(confirmed.head(5))
# print(death.head(5))
# print(recovered.head(5))
