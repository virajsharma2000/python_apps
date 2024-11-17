import streamlit as st
import written_work_summorizer

text = st.text_area('Copy ans paste your written work here')

summorize_button = st.button('Summorize')

if summorize_button:
 summorized_written_work = written_work_summorizer.summorize_school_written_work(text)

 st.write(summorized_written_work)
