import streamlit as st

st.title("Probabilistic analysis of selected stock".upper())

text_1 = """1. Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying within given band formed by lower and upper limit provided
by user.
"""
st.write(text_1)
if st.button(label="Query1 >>"):
    st.switch_page(page='pages/query_1.py')

text_2 = """2. Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying out of given band formed by lower and upper limit provided
by user.
"""
st.write(text_2)
if st.button(label="Query2 >>"):
    st.switch_page(page='pages/query_2.py')


text_3 = """3. Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying above limit provided by user.
"""
st.write(text_3)
if st.button(label="Query3 >>"):
    st.switch_page(page='pages/query_3.py')


text_4 = """4. Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying below limit provided by user.
"""
st.write(text_4)
if st.button(label="Query4 >>"):
    st.switch_page(page='pages/query_4.py')
