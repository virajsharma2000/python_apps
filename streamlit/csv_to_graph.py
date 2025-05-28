import streamlit as st
import pandas as pd
import matplotlib.pyplot as plot
import io

def plot_graph(csv_file_bytes):
 file = io.BytesIO(csv_file_bytes)
 csv = pd.read_csv(file)

 x = csv[csv.columns[0]]
 y = csv[csv.columns[1]]

 fig, ax = plot.subplots()

 ax.set_xlabel(csv.columns[0])
 ax.set_ylabel(csv.columns[1])

 ax.scatter(x, y)

 st.pyplot(fig)


file = st.file_uploader('upload a csv file')

if st.button('Plot Graph'):
 bytes_of_file = file.getvalue()

 plot_graph(bytes_of_file)




