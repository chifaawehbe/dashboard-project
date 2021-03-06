## Dashboard Project (Covid)

#### Inroduction
For our open-source project, we will create an interactive **Covid-19** dashboard that allows users to visualize the number of Covid-19 cases or deaths per country as a function of time.

#### Overview
<li> Data Source and Dataset
<li> Create Virtual Environment Setup
<li> Run the Project in Streamlit Cloud
<li> References 

#### Data Source and Dataset
The data used in the implementation of this project is from https://covid.ourworldindata.org/data/owid-covid-data.csv

#### Create Virtual Environment Setup
1. Open VS code
1. Clone the project with `git clone "https://github.com/chifaawehbe/dashboard-project.git"`
1. In the folder, where you cloned the project, go to the terminal 
1. To create the new environment, run the command: `python3 -m venv dashboard-env` 
1. Activate your virtual python environment : `source dashboard-env/bin/activate` 
1. Install the dependencies: `python -m pip install -r requirements.txt`

####  Run the Project in Streamlit Cloud
You can find this project on **Streamlit Cloud** via this link:
https://share.streamlit.io/chifaawehbe/dashboard-project/covid_dashboard.py 

#### Archive link (Software Heritage)
[![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:ddd368c6fcac5444df2484f9f8e1cfb7284374e6/)](https://archive.softwareheritage.org/swh:1:dir:ddd368c6fcac5444df2484f9f8e1cfb7284374e6;origin=https://github.com/chifaawehbe/dashboard-project;visit=swh:1:snp:d14c022645a7a3093a613c0039efa24f4d1bbcf4;anchor=swh:1:rev:e4fee1f836b3d4bc24d2be5dd207ecc72cbf1f22)
  
 ##### Run locally
  1. Go to the folder wher you cloned the project
  1. Open the terminal
  `streamlit run covid_dashboard.py`

#### References 
  <li> https://towardsdatascience.com/plotly-dash-vs-streamlit-which-is-the-best-library-for-building-data-dashboard-web-apps-97d7c98b938c
  <li> https://plotly.com/python/
