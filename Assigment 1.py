import numpy as np
import pandas as pd
import streamlit as st

st.title("THIS IS FIRST ASSIGNMENT!!!!!")
st.write("All the student do it for cloud computing!!")

data = pd.DataFrame(
    {'Name':["Salman","Ali","Hussain","Ahmed","Hamoud","mohammed","ibrahim","abdullah"],
     "age":[20,21,25,19,17,18,11,15]}
)

st.write("Following is student deatils:")
st.write(data)

chart_data=pd.DataFrame(
    np.random.randn(20,4),
    columns=["A","B","C",'D']
)

st.bar_chart(chart_data)