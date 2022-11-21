import streamlit as st
from PIL import Image
from data.data import *

def viewOrders(name):
    image_loc = f"images/{name[:-2]}/"
    image = Image.open(f"{image_loc}{name[:-2]}_{name[-1]}.jpeg")
    st.text(f"{name}")
    st.image(image)

def calculateTotalPrice():
    sum = 0
    for key in cart_details:
        sum = sum+cart_details[key]
    
    return sum

def ingredientsLeft():
    for food in cart_details.keys():
        food_name = food[:-2]
        food_key = FOOD_CODES[food_name] 
        for item in FOOD_ITEM_LISTS[food_key][0].keys():
            if item in INGREDIENTS.keys():
                INGREDIENTS[item] = INGREDIENTS[item] - FOOD_ITEM_LISTS[food_key][0][item]
    st.write(INGREDIENTS)


if __name__ == "__main__":
    st.title("Manage your Inventory : ")
    if len(current_user)!=0:
        st.write("Customer Name           : ", current_user[-1])
        st.write("Number of items ordered : ", len(cart_details))
        st.write("Total Cost              : ", calculateTotalPrice())
        column1, column2 = st.columns(2)
        with column1:
            st.write("Ordered Items : ")
            for food in cart_details.keys():
                viewOrders(food)
        with column2:
            st.write("Items in Inventory : ")
            ingredientsLeft()
