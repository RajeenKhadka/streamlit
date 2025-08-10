import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Displaying text on the screen
st.write("Hello World 123")
st.write({"Key":"Value"})
st.write(True)
"Hello World"
3+4

button1 = st.button("Press me 1")
print("Button 1:", button1)

button2 = st.button("Press me 2")
print("Button 2:", button2)

st.title("Super simple title")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("This is _Markdown_")
st.caption("This is caption")

code_example = """
def greet(name):
    print('hello', name)
"""

st.code(code_example, language="python")

st.divider()

#Using image
st.image(os.path.join(os.getcwd(), "static","f1.png"))
st.divider()

# Data frames
st.title("Data Frame")
df = pd.DataFrame({
    'Name':['Rajeen','Joanna','Dolma','Anafi','Bryant'],
    'Age':[29,28,27,26,22],
    'Nickname': ['King','Cutie','MiAmor','Yasin','B-dawg']
})
st.dataframe(df)

#Editable dataframe
st.header("Data editor")
editable_df = st.data_editor(df)

#Static dataframe
st.header("Static table")
st.table(df)

#Metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label='Average Age', value=round(df['Age'].mean(),1))

#Chart elements
st.header("Age Distribution Chart")
# Using the existing df to create a chart
age_data = pd.DataFrame({
    'Name': df['Name'],
    'Age': df['Age']
})
st.area_chart(age_data.set_index('Name'))

st.subheader('Bar chart')
st.bar_chart(age_data.set_index('Name'))

st.subheader('line chart')
st.line_chart(age_data.set_index('Name'))

st.subheader('Scatter Chart')
scatter_data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100)
})

st.scatter_chart(scatter_data)

#Map section
st.subheader('New York City Map')
map_data = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [40.7128, -74.0060],
    columns=['lat','lon']
)

st.map(map_data)
