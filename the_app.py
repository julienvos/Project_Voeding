import streamlit as st
import pandas as pd
import numpy as np
import plotly as px

from get_the_data_from_database import get_data



st.title('Voeding en demografie')

#import all the data
data_bmi_men, data_bmi_women, data_food_group, data_macronutrients, data_life_expectancy, data_covid, data_overweight_adults = get_data()

st.subheader('raw data')
st.write(data_bmi_men)





