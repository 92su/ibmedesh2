import streamlit as st
import pandas as pd
import plotly.express as px


st.sidebar.subheader('Upload Excel File')

uploaded_file = st.sidebar.file_uploader("Choose a XLSX file", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file,sheet_name=1)
    st.dataframe(df)
    st.table(df)


    df = df.sort_values(by='academicyear',ascending=True)
    selected = st.multiselect('Select Academic year',df.columns[1:],[df.columns[1]])

    # Mutating the dataframe to keep selected columns only
    st.write(df[['academicyear']+selected].set_index('academicyear'))


    # creating a plotly  line chart
    fig = px.line(df,x='academicyear',y=selected)

    st.write(fig)
