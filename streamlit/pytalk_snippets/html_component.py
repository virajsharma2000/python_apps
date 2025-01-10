import streamlit as st
import streamlit.components.v1 as components

# Render a custom HTML component
html_code = """
<div style="background-color: lightblue; padding: 20px; text-align: center;">
    <h2>Custom Component</h2>
    <p>This is an HTML-based custom component.</p>
</div>
"""
components.html(html_code, height=200)
