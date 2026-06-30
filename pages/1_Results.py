import streamlit as st

from utils.ui import render_header

st.set_page_config(page_title="Results | Grant Application Quality Checker", layout="wide")

render_header("Grant Application Quality Checker")

st.divider()


st.info("Upload an application on the home page to see results here.")

