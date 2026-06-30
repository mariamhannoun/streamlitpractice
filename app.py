import streamlit as st

from utils.ui import render_header, render_footer, render_cards, render_masthead, render_nosection, render_errormessage

# render_masthead()

st.set_page_config(page_title="Grant Application Quality Checker", layout="wide")


render_header("Grant Application Quality Checker")


st.title("Upload SmartyGrants export", text_alignment="center", anchor=False)

render_nosection()

with st.form("application_checker"):

    data = st.file_uploader("Drag and drop your file here", type="pdf", accept_multiple_files=False, max_upload_size=100)

    # st.form_submit_button(label="Check application")

    submitted = st.form_submit_button(label="Check application")

if submitted:
    if data is None:
        render_errormessage()
    else:
        st.switch_page("pages/1_Results.py")


render_cards()

render_nosection()

render_footer()