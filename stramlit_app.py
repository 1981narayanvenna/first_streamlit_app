import streamlit
import pandas
import requests
import snowflake.connector

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

fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Output the screen as table
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT* from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains :")
streamlit.dataframe(my_data_rows)

streamlit.header("What fruit would you like to add?")
fruit_choice2 = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice2)
