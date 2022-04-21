import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

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
  covid = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
  covid['date'] = pd.to_datetime(covid['date'])
  return covid


def plot():
    #covid = pd.DataFrame(px.data.gapminder())
    covid = load_data()

    clist = covid['location'].unique().tolist()

    countries = st.multiselect("Select country", clist)
    st.header("You selected: {}".format(", ".join(countries)))

    dfs = {country: covid[covid["location"] == country] for country in countries}

    fig = go.Figure()
    for country, covid in dfs.items():
        fig = fig.add_trace(go.Scatter(x=covid["date"], y=covid["total_cases"], name=country))

    st.plotly_chart(fig)



page = st.sidebar.selectbox('Total cases',('By country', 'By time'))
if page == 'By country':
  st.title("Total cases by country")   
  plot()

# else:
  # st.title("Total cases in Oceania") 
  # ocean = covid.loc[covid['continent'] == "Oceania"] 
  # fig = px.line(ocean, x="date", y='total_cases')
  # st.plotly_chart(fig)


