import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px


def covid_voeding_function(data_food_group, data_macronutrients, data_covid, data_overweight_adults):

    st.header('Covid en voeding')

    #import data
    # _, _, data_food_group, data_macronutrients, _, data_covid, data_overweight_adults = get_data()

    #copy data
    data_covid_copy = data_covid.copy()
    data_overweight_adults_copy = data_overweight_adults.copy()

    # these columns should actually just be stored in the database
    data_covid_copy["mortality_risk"] = data_covid_copy['total_deaths_per_million'] / data_covid_copy['total_cases_per_million']
    covid_overweight = pd.merge(data_covid_copy, data_overweight_adults_copy.drop(columns=['index', 'Entity']), how='inner', left_on=['iso_code'], right_on=['Code'])

# ----------------------------------------------------------------------------------------------------------------------
    clist_covid = data_covid_copy['location'].unique()
    clist_covid_options = st.multiselect(label = "Selecteer een land:", options =clist_covid, default= 'Netherlands', key=1)
    all_countries_covid = st.checkbox("Selecteer alle landen", key='covid')

    if all_countries_covid:
        clist_covid_options = clist_covid

    data_covid_filtered = data_covid_copy[(data_covid_copy['location'].isin(clist_covid_options))]

    try:
        fig = px.scatter(data_covid_filtered.dropna(subset=['total_cases_per_million', 'total_deaths_per_million', 'continent']), x='total_cases_per_million', y='total_deaths_per_million', color='continent', size='total_deaths_per_million', hover_name='location', title='Covid deaths vs cases on 2021-01-01')
        fig.update_layout(legend_title_text='Continent')
        fig.update_layout(autosize=True)
        fig.update_xaxes(title_text='Total cases per million')
        fig.update_yaxes(title_text='Total deaths per million')
        st.plotly_chart(fig)

    except:
        st.write('Selecteer een land..')
#------------------------------------------------------------------------------------------

    clist_covid_overweight = covid_overweight['location'].unique()
    clist_covid_overweight_options = st.multiselect(label = "Select a country:", options = clist_covid_overweight, default= 'Netherlands', key=2)
    all_countries_overweight = st.checkbox("Selecteer alle landen", key='covid_overweight')

    if all_countries_overweight:
        clist_covid_overweight_options = clist_covid_overweight

    covid_overweight_filtered = covid_overweight[(covid_overweight['location'].isin(clist_covid_overweight_options))]

    covid_overweight_filtered = covid_overweight_filtered.loc[covid_overweight_filtered['Year'] == '2015']

    try:
        fig = px.scatter(covid_overweight_filtered.dropna(subset=['mortality_risk', 'continent']), x='Prevalence of overweight adults (both sexes) - WHO (2019)', y='mortality_risk', color='continent', size='mortality_risk', hover_name='location', range_y=(0, 0.1), title='Mortality risk vs share overweight adults (%)')
        fig.update_xaxes(title_text='share overweight adults (%) (2015)')
        fig.update_yaxes(title_text='Mortality risk')
        st.plotly_chart(fig)
    except:
        st.write('Selecteer een land..')