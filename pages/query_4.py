import yfinance as yf 
import pandas as pd
import numpy as np 
import datetime
from dateutil.relativedelta import relativedelta
import streamlit as st
import time

st.title("Query 4")
text_4 = """Find probability of selected parameter % change(e.g.Close,Open,...etc) 
lying below limit provided by user
"""
st.write(text_4)
st.write('Example')
st.image('images/query 4.JPG',width=500)

script = st.selectbox('Script',pd.read_csv('nifty500_stocklist.csv'),index=0)

# Start and end date of data
st.write('Selecet time window')
start_date = st.date_input('from')
end_date = st.date_input('to')


# download data
df = yf.download(script,start=start_date,end=end_date).iloc[::-1]

if df.shape[0]>0 and script!='-':
    # Dataframe cleaning 

    df.columns = ['Close','High','Low','Open','Volume']
    df = df.reset_index()

    df = df.set_index('Date')

    # Decimal set to 2
    def set_decimals(i):
        return round(i,2)

    for i in df:
        df[i] = df[i].apply(set_decimals)

    # Making data stationary
    for i in df:
        df[i] = round((df[i].diff(-1)/df[i].shift(-1))*100,2)

    # Dropping nulls 
    df.dropna(inplace=True)


    param = st.radio('Select OLHC parameter',df.columns)
    lim = st.number_input(r'Enter limit (% change)')


    data = df[df[param]<=lim][param]
    resultant_obs = data.shape[0]
    total_obs = df.shape[0]
    proba = round(resultant_obs*100/total_obs,2)

    if st.button('FIND PROBABILITY'):
        bar = st.progress(0)

        for i in range(101):
            time.sleep(0.01)
            bar.progress(i)

        bar.success('Task Completed!!')

        st.subheader("RESULT")
        st.write(f"Probability of % change in {param} w.r.t. prev {param}")
        st.write(f"lying below {lim} % is")
        st.write(f"{proba} %")
else:
    pass
