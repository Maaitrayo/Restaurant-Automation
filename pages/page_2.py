import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("Select food testing")
st.sidebar.markdown("# Menue 🎉")

foods = pd.read_csv(r".\data\food_data.csv")
food_item = st.selectbox(
    'How would you like to be contacted?',
    foods['name'].values)


if st.button("Select"):
    # food_item_list = []
    # food_item_list.append(food_item)

    if food_item == "pizza":
        name = "pizza"
        image_loc = r"./images\pizza/"
    elif food_item == "burger":
        image_loc = r"./images\burger/"
        name = "burger"

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        image_1 = Image.open(f"{image_loc}{name}_{1}.jpeg")
        st.text(f"{name} 1")
        st.image(image_1)
    with col2:
        image_2 = Image.open(f"{image_loc}{name}_{2}.jpeg")
        st.text(f"{name} 2")
        st.image(image_2)
    with col3:
        image_3 = Image.open(f"{image_loc}{name}_{3}.jpeg")
        st.text(f"{name} 3")
        st.image(image_3)
    with col4:
        image_4 = Image.open(f"{image_loc}{name}_{4}.jpeg")
        st.text(f"{name} 4")
        st.image(image_4)
   
    
    