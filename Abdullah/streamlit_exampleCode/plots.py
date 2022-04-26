import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns = ['a','b','c']

)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a',y = 'b', tooltip = ['a','b']
)

# st.graphviz_chart(""" 
# digraph{
#     whatch 
# }
# """)

st.map()


st.altair_chart(chart)

plt.scatter(data['a'],data['b'])
plt.title('scatter')
st.pyplot()

st.line_chart(data)


st.bar_chart(data)

# st.image()

# st.audio()

# st.video()


