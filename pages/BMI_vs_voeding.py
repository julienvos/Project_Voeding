import streamlit as st
import pandas as pd
import numpy as np

from get_the_data_from_database import get_data

import plotly.express as px
from format_date import format_year #to get rid of all milliseconds etc.

def bmi_function(data_bmi_men, data_bmi_women, data_food_group, data_macronutrients):

    st.header('BMI en voeding')

    #bmi charts

    clist_bmi = data_bmi_men['Entity'].unique()

    clist_options = st.multiselect(label = "Selecteer een land:", options =clist_bmi, default= 'Netherlands', key='bmi')


    try:
        fig = px.box(data_bmi_men[(data_bmi_men['Entity'].isin(clist_options))], x='Mean BMI (male)', y='Entity', color='Entity', hover_name='Entity', title='Vergelijking BMI mannen tussen verschillende landen (door de jaren heen)')
        fig.update_layout(autosize=True)
        fig.update_layout(legend_title_text='Countries')
        fig.update_layout(yaxis=dict(title='Countries'))
        st.plotly_chart(fig)

    except:
        st.write("Graag een land invoeren..")

    try:
        fig = px.box(data_bmi_women[(data_bmi_women['Entity'].isin(clist_options))], x='Mean BMI (female)', y='Entity', color='Entity', hover_name='Entity', title='Vergelijking BMI vrouwen tussen verschillende landen (door de jaren heen)')
        fig.update_layout(autosize=True)
        fig.update_layout(legend_title_text='Countries')
        fig.update_layout(yaxis=dict(title='Countries'))
        st.plotly_chart(fig)

    except:
        st.write("Graag een land invoeren..")



    #foodgroup charts
    year_food_group = st.selectbox(label= "Selecteer een jaar", options=data_food_group['Year'].unique(), format_func=format_year, key=1)

    clist_food = data_food_group['Entity'].unique()
    clist_food_options = st.multiselect(label = "Selecteer een land:", options =clist_food, default= 'Netherlands', key='food_group')

    data_food_group_filtered = data_food_group.loc[data_food_group['Year'] == year_food_group]

    try:
        fig = px.bar(data_food_group_filtered[(data_food_group_filtered['Entity'].isin(clist_food_options))], x='Code', y=['Other(kcalories person per day)', 'Sugar(kcalories person per day)', 'Oils & Fats(kcalories person per day)', 'Meat(kcalories person per day)', 'Dairy & Eggs(kcalories person per day)', 'Fruit and Vegetables(kcalories person per day)', 'Starchy Roots(kcalories person per day)', 'Pulses(kcalories person per day)', 'Cereals and Grains(kcalories person per day)', 'Alcoholic Beverages(kcalories person per day)'], barmode='group', title='Consumption between countries')
        fig.update_layout(legend_title_text='Food groups')
        fig.update_layout(yaxis=dict(title='Kcalories per person per day'))
        fig.update_layout(xaxis=dict(title='Country'))

        #rename legend
        newnames = {'Other(kcalories person per day)':'Other', 'Sugar(kcalories person per day)': 'Sugar','Oils & Fats(kcalories person per day)':'Oils & Fats', 'Meat(kcalories person per day)':'Meat','Dairy & Eggs(kcalories person per day)': 'Dairy & Eggs', 'Fruit and Vegetables(kcalories person per day)': 'Fruit and Vegetables', 'Starchy Roots(kcalories person per day)': 'Starchy Roots', 'Pulses(kcalories person per day)': 'Pulses', 'Cereals and Grains(kcalories person per day)': 'Cereals and Grains',
                'Alcoholic Beverages(kcalories person per day)': 'Alcoholic Beverages'}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                            legendgroup = newnames[t.name],
                                            hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))
                                            
        fig.update_layout(autosize=True)
        
        st.plotly_chart(fig)

    except:
        st.write('Selecteer een land..')


    #macronutrients
    year_macronutrients = st.selectbox(label= "Selecteer een jaar", options=data_macronutrients['Year'].unique(), format_func=format_year, key=2)

    clist_macronutrients = data_macronutrients['Entity'].unique()
    clist_macronutrients_options = st.multiselect(label = "Selecteer een land:", options =clist_macronutrients, default= 'Netherlands', key='macronutrient')

    data_macronutrients_filtered = data_macronutrients.loc[data_macronutrients['Year'] == year_macronutrients]

    try:
        fig = px.bar(data_macronutrients_filtered[(data_macronutrients_filtered['Entity'].isin(clist_macronutrients_options))], x='Code', y=['Calories from animal protein (FAO (2017))', 'Calories from plant protein (FAO (2017))', 'Calories from fat (FAO (2017))', 'Calories from carbohydrates (FAO (2017))'], barmode='group',title='Energieopname per land per macronutrient')

        newnames = {'Calories from animal protein (FAO (2017))': 'Animal Protein', 'Calories from plant protein (FAO (2017))': 'Plant Protein', 'Calories from fat (FAO (2017))': 'Fat', 'Calories from carbohydrates (FAO (2017))': 'Carbohydrates'}
        fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                        legendgroup = newnames[t.name],
                                        hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])))


        fig.update_xaxes(title_text='Country')
        fig.update_yaxes(title_text='Kcalories per person per day')
        fig.update_layout(legend_title_text='Macronutrients')
        st.plotly_chart(fig)
    except:
        st.write("Selecteer een land...")