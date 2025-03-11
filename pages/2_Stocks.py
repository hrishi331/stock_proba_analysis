import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf
import nsepython as nse
from scipy.stats import norm
import streamlit as st
import plotly.express as px
import datetime
import time


# Streamlit - header
st.header('EDA - Equity')

stocks = nse.nse_eq_symbols() # stock list
script = st.selectbox('Script',stocks,index=None)

# Streamlit data window select
st.write('Select data window')
l1,r1 = st.columns(2,gap='large')
start_date = l1.date_input('from')
end_date = r1.date_input('to')


#----------------------------
# script = 'NIFTY 50'
# start_date = '2020-01-01'
# end_date = '2025-02-11'
#----------------------------

if st.button("SUBMIT"):
    # initialize progress bar
    bar = st.progress(0)

    # Progressing 
    for i in range(101):
        time.sleep(0.05)
        bar.progress(i)

    # Task completion
    bar.success("Task completed !!")

# Data download
if start_date<end_date:
    df = nse.equity_history(script,"EQ",
                            start_date=str(start_date.strftime('%d-%m-%Y')),
                            end_date=str(end_date.strftime('%d-%m-%Y')))
    
    df = df[['CH_TIMESTAMP','CH_TRADE_HIGH_PRICE','CH_TRADE_LOW_PRICE',
    'CH_OPENING_PRICE','CH_CLOSING_PRICE']]
    df.columns = ['Date','High','Low','Open','Close'] # column name changed
    df = df.set_index('Date') # index set

    # Dataframe cleaning
    for i in df:
        df[i] = df[i].astype(float)


    for i in df:
        df[i] = round(df[i].diff(-1)*100/df[i].shift(-1),2)

    df = df.dropna()

    if type and script and df.shape[0]>0:

        # Result henceforth

        st.subheader('Results')

        # 1. streamlit - 5 point summery
        with st.expander("**1. 5 point summery**"):
            col_1 = st.radio('OLHC',['High','Open','Low','Close'],
                            index=0,horizontal=True,key=1)
            
            # Calculating parameters
            count_ = round(df[col_1].count(),2)
            mean_ = round(df[col_1].mean(),2)
            std_ = round(df[col_1].std(),2)
            min_ = round(df[col_1].min(),2)
            max_ = round(df[col_1].max(),2)

            # Display results
            st.write(f'observations : {count_}')
            st.write(f'mean : {mean_} %')
            st.write(f'std dev : {std_} %')
            st.write(f'min : {min_} %')
            st.write(f'max : {max_} %')

        # 2. Probabilities and ranges
        with st.expander('**2. Probabilities and ranges**'):
            st.caption("**Calculated using Confidence Interval Estimation method")
            col_2 = st.radio('OLHC',['High','Open','Low','Close'],index=0,
                            key=2,horizontal=True)
            st.write(r"Probability | lower side % change | upper side % change")

            # Display result using loop
            for i in range(1,101):
                probability = i
                alpha = 1 - probability/100
                z = norm.ppf(1-alpha/2)
                ll = round(df[col_2].mean() - z , 2)
                ul = round(df[col_2].mean() + z , 2)
                st.write(f"{probability}% | {ll}% | {ul}%")
                


        # 3. Distribution
        with st.expander('**3. Distribution**'):
            col_3 = st.radio('OLHC',['High','Open','Low','Close'],index=0,
                            key=3,horizontal=True)
            
            # calculating all parameters
            mea_n = round(df[col_3].mean(),2)
            st_d = round(df[col_3].std(),2)
            mi_n = round(df[col_3].min(),2)
            ma_x = round(df[col_3].max(),2)

            # figure plot
            fig,ax = plt.subplots(figsize = (7,3))
            sns.histplot(df[col_3],kde=True)
            
            # Vlines
            plt.axvline(mea_n,color='blue',ls = '--',label = f'mean : {round(mea_n,2)}')
            plt.axvline(mi_n,color='red',ls = '--',label = f'min : {round(mi_n,2)}')
            plt.axvline(ma_x,color='green',ls = '--',label = f'max : {round(ma_x,2)}')
           
            # Vspans
            y_min,y_max = ax.get_ylim()
            plt.axvspan(-st_d,st_d,color = 'grey',ymin=y_min,ymax=y_max,alpha = 0.5,label = f"+/- std : [{round(-st_d,2)},{round(st_d,2)}]")
            plt.axvspan(-st_d*2,st_d*2,color = 'grey',ymin=y_min,ymax=y_max,alpha = 0.3,label = f"+/- 2std : [{round(-st_d*2,2)},{round(st_d*2,2)}]")
            plt.axvspan(-st_d*3,st_d*3,color = 'grey',ymin=y_min,ymax=y_max,alpha = 0.1,label = f"+/- 3std : [{round(-st_d*3,2)},{round(st_d*3,2)}]")
        
            plt.legend(prop = {'size':8})
            # Display plot
            st.pyplot(fig)

            # Caption
            st.caption("**Assumption : Data is normally distributed")
        
else:
    pass



