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

st.write('''
    ![](https://media.giphy.com/media/idShevOa24HzYTgz06/giphy.gif)
''')
            
st.sidebar.title("Visualization Selector")
#st.sidebar.markdown("Select the Continent:")

@st.cache
def load_data():
  covid = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
  covid['date'] = pd.to_datetime(covid['date'])
  return covid

covid = load_data()

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

fig = px.line(covid, x='date', y = ['new_deaths','new_cases'])
st.plotly_chart(fig)



# continent = st.sidebar.selectbox('Select a Continent',covid['continent'].unique())
# if continent == "Asia":
#   st.title("Asia") 
#   asia = covid.loc[covid['continent'] == "Asia"]  
#   #st.pyplot(simpleGraph(asia), use_container_width = True)
#   fig = px.line(asia, x="date", y='total_cases')
#   st.plotly_chart(fig)

#   st.title("New cases and new deaths") 
#   asia = covid.loc[covid['continent'] == "Asia"]  
#   #st.pyplot(simpleGraph(asia), use_container_width = True)
#   fig = px.line(asia, x='date', y = ['new_deaths','new_cases'])
#   fig.show()
  

# elif continent == "Europe":
#   st.title("Total cases in Europe") 
#   europe = covid.loc[covid['continent'] == "Europe"] 
#   fig = px.line(europe, x="date", y='total_cases')
#   st.plotly_chart(fig)
  
# elif continent == "Africa":
#   st.title("Total cases in Africa") 
#   africa = covid.loc[covid['continent'] == "Africa"] 
#   fig = px.line(africa, x="date", y='total_cases')
#   st.plotly_chart(fig)
  
# elif continent == "North America":
#   st.title("Total cases in North America") 
#   na = covid.loc[covid['continent'] == "North America"] 
#   fig = px.line(na, x="date", y='total_cases')
#   st.plotly_chart(fig)

# elif continent == "South America":
#   st.title("Total cases in South America") 
#   sa = covid.loc[covid['continent'] == "South America"] 
#   fig = px.line(sa, x="date", y='total_cases')
#   st.plotly_chart(fig)

# #if continent == "Oceania":
# else:
#   st.title("Total cases in Oceania") 
#   ocean = covid.loc[covid['continent'] == "Oceania"] 
#   fig = px.line(ocean, x="date", y='total_cases')
#   st.plotly_chart(fig)


