import streamlit as st
import pandas as pd
import numpy as np


import plotly.express as px

def life_expectancy_function(data_life_expectancy):

    st.header('Levensverwachting en voeding')

    clist_life_expectancy = data_life_expectancy['Entity'].unique()

    clist_options = st.multiselect(label = "Select a country:", options =clist_life_expectancy, default= 'Netherlands')

    data_life_expectancy_filtered = data_life_expectancy[(data_life_expectancy['Entity'].isin(clist_options))]
    try:
        fig = px.line(data_life_expectancy_filtered.sort_values(by=['Year'], ascending=[True]), x='Year', y='Life expectancy', color='Code', title='Life expectancy through the years')
        fig.update_layout(autosize=True)
        fig.update_layout(legend_title_text='Countries')
        st.plotly_chart(fig)
    except:
        st.write('Selecteer een land..')