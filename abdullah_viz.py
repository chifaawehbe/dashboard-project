import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import datetime

st.title('COVID Dashboard')
st.markdown('''Hello :wave:  For our *open-source* project, we created an interactive **Covid-19** dashboard 
    that allows users to visualize the number of  Covid-19 cases or deaths per country 
    as a function of time''')

# st.markdown('''
#           Coronavirus disease (COVID-19) is an infectious disease caused by a newly 
#             discovered coronavirus. Most people infected with the COVID-19 virus will 
#             experience mild to moderate respiratory illness and recover without requiring 
#             special treatment.''')


            
st.sidebar.title("Visulization selector") #making sidebar


covid = pd.read_csv('owid-covid-data.csv') #loading data through CSV

# st.write('OWID COVID DATASET')


########## DATE SELECTOR #############

start_date = st.sidebar.date_input('Start date', datetime.date(2020,3,1)) #dateselecter for start date

today = datetime.date.today() #to get todays date 

tomorrow = today + datetime.timedelta(days=1) #tomorrows date

end_date = st.sidebar.date_input('End date', tomorrow) #dataselecter for end date, it has tomorrow because end date is always ahead

# if start_date < end_date:
#     st.success('Start date: `%s`\n\nEnd date: `%s`' % (start_date, end_date))
# else:
#     st.error('Error: End date must fall after start date.')


covid["date"] = pd.to_datetime(covid["date"]) # converting covid[data] to a datetime format

covid['date'] = covid['date'].dt.date # converting covid[data] to a datetime format 

mask = (covid['date']< end_date) & (covid['date'] >= start_date) #creating a filter for the dates that will be selected

covid2=covid[mask] # new date filter dateframe

##############################################

# st.dataframe(covid2) #viewing dataframe on dashbaord

clist = covid2['location'].unique().tolist() #unique list of countries

countries = st.multiselect("Select Country", clist, default = 'France') # creating a multiselector for countries, DEFAULT country 'France'
st.header("You selected: {}".format (", ".join(countries))) # header to print what countries selected

dfs = {country: covid2[covid2["location"] == country] for country in countries} #making dictionary of dataframe based on country selected

page = st.sidebar.selectbox('Selected Option',('Total cases', 'Total deaths')) #select box in sidebar

rad = st.sidebar.radio('select option', ['7 Day Rolling Average','Raw Number', 'Cummulative Number'])

diff_deaths = covid2['total_deaths'].diff() # have to difference between rows to calculate rolling average
diff_cases = covid2['total_cases'].diff()

deaths_roll = diff_deaths.rolling(window = 7).mean() #7 day rolling average
cases_roll = diff_cases.rolling(window = 7).mean()


if page == 'Total cases':

    if rad == '7 Day Rolling Average':
        st.write("7 day rolling average of Cases")
        fig = go.Figure()
        for country, covid2 in dfs.items():
            fig = fig.add_trace(go.Scatter(x=covid2["date"], y= cases_roll, name= country))
        st.plotly_chart(fig)

if page == 'Total deaths':

    if rad == '7 Day Rolling Average':
        st.write("7 day rolling average of Deaths")
        fig = go.Figure()
        for country, covid2 in dfs.items():
            fig = fig.add_trace(go.Scatter(x=covid2["date"], y= deaths_roll, name= country))
        st.plotly_chart(fig)

