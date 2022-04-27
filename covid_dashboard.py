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

st.markdown('''
          Coronavirus disease (COVID-19) is an infectious disease caused by a newly 
            discovered coronavirus. Most people infected with the COVID-19 virus will 
            experience mild to moderate respiratory illness and recover without requiring 
            special treatment.''')

# st.write('''
#     ![](https://media.giphy.com/media/idShevOa24HzYTgz06/giphy.gif)
# ''')
            
st.sidebar.title("Visualization Selector")
#st.sidebar.markdown("Select the Continent:")

@st.cache
def load_data():
  covid = pd.read_csv('owid-covid-data.csv')
  covid['date'] = pd.to_datetime(covid['date'])
  return covid


def plot():
  
    covid = load_data()

    #datepicker
    today = datetime.date.today()
    dateselecters = st.sidebar.date_input('Start date', datetime.date(2020,3,1))
    tomorrow = today + datetime.timedelta(days=1)
    dateselectere = st.sidebar.date_input('End date', tomorrow)
    if dateselecters < dateselectere:
        st.success('Start date: `%s`\n\nEnd date:`%s`' % (dateselecters, dateselectere))
    else:
      st.error('Error: End date must fall after start date.')

    #covid["date"] = pd.to_datetime(covid["date"]).dt.date
    mask = (covid['date']<dateselectere) & (covid['date'] >= dateselecters)
    covid2=covid[mask]

    clist = covid2['location'].unique().tolist()

    countries = st.multiselect("Select country", clist, default = 'France')
    st.header("You selected: {}".format(", ".join(countries)))

    dfs = {country: covid2[covid2["location"] == country] for country in countries}

    fig = go.Figure()
    for country, covid2 in dfs.items():
        fig = fig.add_trace(go.Scatter(x=covid2["date"], y=covid2["total_cases"], name=country))

    st.plotly_chart(fig)



page = st.sidebar.selectbox('Total cases',('Total cases', 'Total deaths'))
if page == 'Total cases':
  st.title("Total cases by country")   
  plot()

# else:
  # st.title("Total cases in Oceania") 
  # ocean = covid.loc[covid['continent'] == "Oceania"] 
  # fig = px.line(ocean, x="date", y='total_cases')
  # st.plotly_chart(fig)


#cumulative, raw, smooth
#normalized data