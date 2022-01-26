import streamlit as st
from connect_with_csv.convert_csv_data import read_csv_files

from pages.BMI_vs_voeding import bmi_function
from pages.covid_vs_voeding import covid_voeding_function
from pages.life_expectancy_vs_voeding import life_expectancy_function

#------------------------------------------------------------------
# conn = init_connection()
st.title('Voeding en demografie')

#import all the data
data_food_group, data_macronutrients, data_life_expectancy, data_bmi_men, data_bmi_women, data_overweight_adults, data_covid = read_csv_files()

page = st.sidebar.selectbox(label ='Selecteer een onderwerp:', options=['BMI vs voeding','Levensverwachting vs voeding', 'corona vs voeding'])


if page == 'BMI vs voeding':
    bmi_function(data_bmi_men, data_bmi_women, data_food_group, data_macronutrients)
    
elif page == 'Levensverwachting vs voeding':
    life_expectancy_function(data_life_expectancy)

elif page == 'corona vs voeding':
    covid_voeding_function(data_food_group, data_macronutrients,data_covid, data_overweight_adults)





# grafieken maken
# selectie van data maken voor grafieken/charts
# landkaart? geocoding
# sliders etc

# layout: Titel, figuur (met slider etc voor filteren), sidebar(voor selectie van data onderwerpen)





