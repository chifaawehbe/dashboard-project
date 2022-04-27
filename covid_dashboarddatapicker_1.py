import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import datetime

st.title('COVID dashboard')
st.markdown('''Hello :wave:  For our *open-source* project, we created an interactive **Covid-19** dashboard 
    that allows users to visualize the number of  Covid-19 cases or deaths per country 
    as a function of time''')

st.markdown('''g
          Coronavirus disease (COVID-19) is an infectious disease caused by a newly 
            discovered coronavirus. Most people infected with the COVID-19 virus will 
            experience mild to moderate respiratory illness and recover without requiring 
            special treatment.''')

st.write('''
    ![](https://media.giphy.com/media/idShevOa24HzYTgz06/giphy.gif)
''')
            
st.sidebar.title("Visualization Selector")
#st.sidebar.markdown("Select the Continent:")

@st.cache
def load_data():
  covid = pd.read_csv('owid-covid-data.csv')
  covid['date'] = pd.to_datetime(covid['date'])
  return covid

covid = load_data()
#data_load_state.text('Data is baked')

def simpleGraph(data):
  # fig=plt.figure(figsize=(14,6))
  # plt.title("Total cases by Continent")
  # plt.xticks(rotation=90)
  # plt.xlabel("Date", fontsize=8)
  # plt.ylabel("Total cases per million", fontsize=8)
  fig = px.line(data, x='date', y='total_cases')
  #plt.plot('date','total_cases', data)
  #plt.show()
  #sns.lineplot(x='date', y=data['total_cases'])
  plt.savefig('plot.png')
  return fig


today = datetime.date.today()
dateselecters = st.sidebar.date_input('Start date', datetime.date(2019,3,1))
tomorrow = today + datetime.timedelta(days=1)
dateselectere = st.sidebar.date_input('End date', tomorrow)
if dateselecters < dateselectere:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (dateselecters, dateselectere))
else:
    st.error('Error: End date must fall after start date.')

# Create a list of possible values and multiselect menu with them in it.
COUNTRIES = covid['location'].unique()
COUNTRIES_SELECTED = st.multiselect('Select countries', COUNTRIES, default='France')

# Mask to filter dataframe
mask_countries = covid['location'].isin(COUNTRIES_SELECTED)

data = covid[mask_countries]

fig = px.line(data, x = "date", y = "total_cases", title = 'country')
st.plotly_chart(fig)

# continent = st.sidebar.selectbox('Select a Continent',covid['continent'])
# if continent == "Asia":
#   st.title("Total cases in Asia") 
#   asia = covid.loc[covid['continent'] == "Asia"]  
#   #st.pyplot(simpleGraph(asia), use_container_width = True)
#   fig = px.line(asia, x="date", y='total_cases')
#   st.plotly_chart(fig)

# if continent == "Europe":
#   st.title("Total cases in Europe") 
#   europe = covid.loc[covid['continent'] == "Europe"] 
#   fig = px.line(europe, x="date", y='total_cases')
#   st.plotly_chart(fig)
  
# if continent == "Africa":
#   st.title("Total cases in Africa") 
#   africa = covid.loc[covid['continent'] == "Africa"] 
#   fig = px.line(africa, x="date", y='total_cases')
#   st.plotly_chart(fig)
  
# if continent == "Africa":
#   st.title("Total cases in Africa") 
#   africa = covid.loc[covid['continent'] == "Africa"] 
#   fig = px.line(africa, x="date", y='total_cases')
#   st.plotly_chart(fig)


