import streamlit as st
import plotly.graph_objects as go

fig = go.Figure(data=[go.Surface(z=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])])
st.plotly_chart(fig, use_container_width=True)
