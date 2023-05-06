import streamlit
import pandas
import requests

streamlit.title("My Mom's New Healthy Dinner")
streamlit.header('Breakfast Favorites')
streamlit.text("🥣 Omega3 & Blueberry Juice")
streamlit.text("Idly & Vada")
streamlit.text('🥑 Avacado Toast poori')
streamlit.text('🐔 Biryani ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

#fruits_to_show = my_fruit_list.filter(Fruit=['Avocado','Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Output the screen as table
streamlit.dataframe(fruityvice_normalized)


