import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import datetime

st.title('COVID-19 Dashboard')
st.markdown(''' Hello :wave:  For our *open-source* project, we created an interactive **Covid-19** dashboard 
that allows users to
- Visualize the number of  Covid-19 *Cases* or *Deaths* per *Country* over user selected period of Time''')

# st.markdown('''
#           Coronavirus disease (COVID-19) is an infectious disease caused by a newly 
#             discovered coronavirus. Most people infected with the COVID-19 virus will 
#             experience mild to moderate respiratory illness and recover without requiring 
#             special treatment.''')

# st.write('''
#     ![](https://media.giphy.com/media/idShevOa24HzYTgz06/giphy.gif)
# ''')
            
st.sidebar.title("Visualization Selector")

@st.cache(allow_output_mutation=True)
def load_data(url):
    df = pd.read_csv(url)
    df["date"] = pd.to_datetime(df.date).dt.date
    df['date'] = pd.DatetimeIndex(df.date)
    return df

#Load the data
url = "owid-covid-data.csv"
covid = load_data(url)

#Remove the locations that are not a country
countries = covid.location.unique().tolist()

not_a_country = ['World', 'International', 'Oceania', 'Africa', 'Asia', 'Europe', 'European Union', 
'High income', 'Low income', 'Lower middle income', 'Upper middle income', 'North America', 'South America']

for x in not_a_country:
    countries.remove(x)

selected_countries = st.multiselect("Choose a country", countries, default=["France"])
#st.markdown(f"### You Selected: {', '.join(selected_countries)}")
#st.header("You selected: {}".format(", ".join(selected_countries)))

# 7day rolling avgerage
covid['rolling_avg_cases_per_million'] = covid['new_cases_per_million'].rolling(window=7).mean()
covid['rolling_avg_cases_per_million'] = covid['rolling_avg_cases_per_million'].fillna(0)

covid['rolling_avg_deaths_per_million'] = covid['new_deaths_per_million'].rolling(window=7).mean()
covid['rolling_avg_deaths_per_million'] = covid['rolling_avg_deaths_per_million'].fillna(0)

# cumulated number
covid=covid.sort_values(['date']).reset_index(drop=True)

covid['new_cases_per_million'] = covid['new_cases_per_million'].fillna(0)
covid['cumulative_number_cases_per_million'] = covid.groupby(['location'])['new_cases_per_million'].cumsum(axis=0)

covid['new_deaths_per_million'] = covid['new_deaths_per_million'].fillna(0)
covid['cumulative_number_deaths_per_million'] = covid.groupby(['location'])['new_deaths_per_million'].cumsum(axis=0)

# Matching the countries selected to the countries in the dataframe
def match_countries(list_selected_counties):
    covid_countries = covid[covid['location'].isin(list_selected_counties)]
    return covid_countries

covid_countries = match_countries(selected_countries)

# Data Picker
data = st.sidebar.selectbox('Choose the data',('Total cases', 'Total deaths'))

# Data Type Picker
data_type = st.sidebar.radio("Choose the data type", ["Cumulated data", "Raw data", "7 days rolling average"])

# Date Picker
today = datetime.date.today()
start = st.sidebar.date_input('Start date', datetime.date(2020,3,1))
tomorrow = today + datetime.timedelta(days=1)
end = st.sidebar.date_input('End date', tomorrow)
# if start < end:
#     st.success('Start date: `%s`\n\nEnd date:`%s`' % (start, end))
# else:
#   st.error('Error: End date must fall after start date.')

# Mask for the selected countries and date 
start = np.datetime64(start)
end = np.datetime64(end)
covid_countries['date'] = pd.to_datetime(covid_countries['date'])
mask = (covid_countries['date'] > start) & (covid_countries['date'] <= end)
new_covid = covid_countries.loc[mask]

# Plot Function
def plot(data_type, graph_title, y_title):
    fig = px.line(new_covid, x=new_covid['date'], y=new_covid[data_type], color='location',
    color_discrete_sequence=px.colors.qualitative.G10)
    
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0})
    
    
    graph = st.plotly_chart(fig.update_layout(title = graph_title, xaxis_title = 'Date', 
    yaxis_title = y_title), use_container_width=True)

    return graph

# Configure all the possible cases
if data == 'Total cases' and data_type == 'Cumulated data':
  plot(data_type='cumulative_number_cases_per_million', graph_title = 'Covid cases Cumulated data',
  y_title='Cumulated number of cases (per million)')
  

if data == 'Total cases' and data_type == 'Raw data':
  plot(data_type='new_cases_per_million', graph_title = 'Covid cases Raw data',
  y_title='Raw number of cases (per million)') 

if data == 'Total cases' and data_type == '7 days rolling average':
  plot(data_type='rolling_avg_cases_per_million', graph_title = 'Covid cases 7 days rolling average',
  y_title='7 days rolling average of cases (per million)')
  
if data == 'Total deaths' and data_type == 'Cumulated data':
  plot(data_type='cumulative_number_deaths_per_million', graph_title = 'Covid deaths Cumulated data',
  y_title='Cumulated number of deaths (per million)')
  
if data == 'Total deaths' and data_type == 'Raw data':
  plot(data_type='new_deaths_per_million', graph_title = 'Covid deaths Raw data',
  y_title='Raw number of deaths (per million)')  

if data == 'Total deaths' and data_type == '7 days rolling average':
  plot(data_type='rolling_avg_deaths_per_million', graph_title = 'Covid deaths 7 days rolling average',
  y_title='7 days rolling average of deaths (per million)')

#st.subheader('Dataframe of filter selected')
#st.dataframe(new_covid)
  


