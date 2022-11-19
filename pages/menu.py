import streamlit as st
import pandas as pd
from PIL import Image
from data.data import cart_details


st.markdown("Select food testing")
st.sidebar.markdown("# Menue 🎉")

foods = pd.read_csv("data/food_data.csv")
food_item = st.selectbox(
    'How would you like to be contacted?',
    foods['name'].values)

def dispalyFoods(name, image_loc, pos, cart_details):
    image = Image.open(f"{image_loc}{name}_{pos}.jpeg")
    st.text(f"{name} {pos}")
    st.image(image)
    st.text(f"price : 1{pos}0")
    cart_status = st.button("Add to Cart", key=f"{pos}")
    if cart_status:
        cart_details[f"{name} {pos}"] = int(f"1{pos}0")
    return cart_status, cart_details

def calculateTotalPrice(cart_details):
    sum = 0
    for key in cart_details:
        sum = sum+cart_details[key]
    
    return sum

def selectFoodItems(cart_details):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        cart_status, cart_details = dispalyFoods(name, image_loc, 1, cart_details)
        if cart_status:st.write("added to cart")
    with col2:
        cart_status, cart_details = dispalyFoods(name, image_loc, 2, cart_details)
        if cart_status:st.write("added to cart")
    with col3:
        cart_status, cart_details = dispalyFoods(name, image_loc, 3, cart_details)
        if cart_status:st.write("added to cart")
    with col4:
        cart_status, cart_details = dispalyFoods(name, image_loc, 4, cart_details)
        if cart_status:st.write("added to cart")
    
    return cart_details

if __name__ == "__main__":
    name = food_item
    image_loc = f"images/{name}/"
    cart_details = selectFoodItems(cart_details)
    # sum = calculateTotalPrice(cart_details)
    # st.write(cart_details)
    # st.write("Total Sum = ", sum)
   
    
    