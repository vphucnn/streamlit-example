# page2.py
import streamlit as st
import foof


st.write(foof.hello)
st.write(foof.greeting("Jonathan"))
if "shared" in st.session_state:
    st.write(st.session_state["shared"])
