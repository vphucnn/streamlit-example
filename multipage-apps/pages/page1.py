# page1.py
import streamlit as st
import foof
foof.hello = 123


if "shared" not in st.session_state:
    st.session_state["shared"] = True
