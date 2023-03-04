import streamlit as st
import pandas

st.set_page_config(layout="wide")

content1 = "The Best Company"
st.title(content1)

content2 = """
test

"""
st.write(content2)

content3 = "Our Team"
st.subheader(content3)

col1, col2, col3 = st.columns(3)

#make a dataframe from the csv file
df = pandas.read_csv("data.csv")

with col1:
    #iterate over the dataframe
    for index, row in df[:4].iterrows():
        st.subheader(row['first name'] + " " + row['last name'])
        st.write(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row['first name'] + " " + row['last name'])
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row['first name'] + " " + row['last name'])
        st.write(row['role'])
        st.image("images/" + row['image'])

