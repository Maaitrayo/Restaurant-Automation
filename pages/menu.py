import streamlit as st
import pandas as pd

st.markdown("Select food")
st.sidebar.markdown("# Menue 🎉")

# foods = pd.read_csv(r"D:\users\Desktop\RECENT WORK FILES\login system\data/food_data.csv")
# food_item = st.multiselect(
#     'How would you like to be contacted?',
#     foods['name'].values)


food_dic = {"milk" : 10,
            "bread" : 20,
            "tea" : 10,
            "rice" : 50}

food_item = st.multiselect(
    'How would you like to be contacted?',
    food_dic.keys())

if st.button("Select"):
    food_item_list = []
    food_item_list.append(food_item)

    for food in food_item_list:
        st.write(food)
    
    
