import streamlit as st
import asyncio

async def async_task():
    await asyncio.sleep(2)
    return "Async Task Completed!"

st.write("Starting async task...")
result = asyncio.run(async_task())
st.write(result)
