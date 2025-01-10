import streamlit as st

# Add a button
if st.button("Click Me"):
    st.write("Button clicked!")

# Add a display of the button state
st.write("Note: Button returns `True` only on the first load after a click.")