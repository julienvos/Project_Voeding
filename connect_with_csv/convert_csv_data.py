import pandas as pd
import numpy as np

import streamlit as st

st.cache
def read_csv_files():
    diet_by_food_group_composition = pd.read_csv('Data/dietary-compositions-by-commodity-group.csv', parse_dates=['Year'])
    diet_by_macronutrient = pd.read_csv('Data/daily-caloric-supply-derived-from-carbohydrates-protein-and-fat.csv', parse_dates=['Year'])
    life_expectancy = pd.read_csv('Data/life-expectancy.csv', parse_dates=['Year'])
    bmi_men = pd.read_csv('Data/mean-body-mass-index-bmi-in-adult-males.csv', parse_dates=['Year'])
    bmi_women = pd.read_csv('Data/mean-body-mass-index-bmi-in-adult-women.csv', parse_dates=['Year'])
    share_overweight_adults = pd.read_csv('Data/share-of-adults-who-are-overweight.csv', parse_dates=['Year'])
    covid_data = pd.read_csv('Data/owid-covid-data.csv', parse_dates=['date'])

    covid_data_filtered = covid_data[['iso_code', 'continent', 'location', 'date', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'new_deaths_per_million', 'icu_patients_per_million', 'hosp_patients_per_million', 'weekly_icu_admissions_per_million', 'weekly_hosp_admissions_per_million', 'people_vaccinated_per_hundred', 'median_age']]
    covid_data_filtered = covid_data_filtered.loc[covid_data_filtered['date'] == '2021-01-01']

    diet_by_food_group_composition.columns = ['Entity', 'Code', 'Year',
        'Other(kcalories person per day)',
        'Sugar(kcalories person per day)',
        'Oils & Fats(kcalories person per day)',
        'Meat(kcalories person per day)',
        'Dairy & Eggs(kcalories person per day)',
        'Fruit and Vegetables(kcalories person per day)',
        'Starchy Roots(kcalories person per day)',
        'Pulses(kcalories person per day)',
        'Cereals and Grains(kcalories person per day)',
        'Alcoholic Beverages(kcalories person per day)']

    return diet_by_food_group_composition, diet_by_macronutrient, life_expectancy, bmi_men, bmi_women, share_overweight_adults, covid_data_filtered

