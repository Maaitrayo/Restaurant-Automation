import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("Select food testing")
st.sidebar.markdown("# Menue 🎉")

foods = pd.read_csv("data/food_data.csv")
food_item = st.selectbox(
    'How would you like to be contacted?',
    foods['name'].values)

def dispalyFoods(name, image_loc, pos):
    image = Image.open(f"{image_loc}{name}_{pos}.jpeg")
    st.text(f"{name} {pos}")
    st.image(image)
    st.text(f"price : 1{pos}0")
    cart_status = st.button("Add to Cart", key=f"{pos}")
    return cart_status


name = food_item
image_loc = f"images/{name}/"

col1, col2, col3, col4 = st.columns(4)
with col1:
    cart_status = dispalyFoods(name, image_loc, 1)
    if cart_status:st.write("added to cart")
with col2:
    cart_status = dispalyFoods(name, image_loc, 2)
    if cart_status:st.write("added to cart")
with col3:
    cart_status = dispalyFoods(name, image_loc, 3)
    if cart_status:st.write("added to cart")
with col4:
    cart_status = dispalyFoods(name, image_loc, 4)
    if cart_status:st.write("added to cart")
   
    
    