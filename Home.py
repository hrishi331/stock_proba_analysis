import streamlit as st

st.title("Probabilistic analysis of selected stock".upper())

st.page_link(r"pages\query_1.py",label='**Query 1**')
text_1 = """Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying within given band formed by lower and upper limit provided
by user
"""
st.write(text_1)


st.page_link(r"pages\query_2.py",label='**Query 2**')
text_2 = """Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying out of given band formed by lower and upper limit provided
by user
"""
st.write(text_2)


st.page_link(r"pages\query_3.py",label='**Query 3**')
text_3 = """Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying above limit provided by user
"""
st.write(text_3)


st.page_link(r"pages\query_4.py",label='**Query 4**')
text_4 = """Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying below limit provided by user
"""
st.write(text_4)