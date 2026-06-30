from pathlib import Path

import streamlit as st

STATIC_DIR = Path(__file__).parent.parent / "static"

NSW_DESIGN_SYSTEM_CSS = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/nsw-design-system@3.24.10/dist/css/main.min.css">
"""


def _load(*relative_path: str) -> str:
    return (STATIC_DIR / Path(*relative_path)).read_text()


def render_masthead():
    st.markdown(_load("html", "masthead.html"), unsafe_allow_html=True)

def render_nosection():
    st.markdown(_load("html", "nosection.html"), unsafe_allow_html=True)


def render_header(title: str):
    st.markdown(NSW_DESIGN_SYSTEM_CSS, unsafe_allow_html=True)
    st.markdown(f"<style>{_load('css', 'main.css')}</style>", unsafe_allow_html=True)
    st.markdown(_load("html", "header.html"), unsafe_allow_html=True)
    st.markdown(
        f'<div class="header-bar"><span class="header-title">{title}</span></div>',
        unsafe_allow_html=True,
    )

def render_cards():
    st.markdown(_load("html", "cards.html"), unsafe_allow_html=True)

def render_errormessage():
    st.markdown(_load("html", "errormessage.html"), unsafe_allow_html=True)


def render_footer():
    st.markdown(_load("html", "footer.html"), unsafe_allow_html=True)
