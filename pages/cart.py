import streamlit as st


from data.data import cart_details


st.markdown("Welcome to your cart")
st.sidebar.markdown(f"Your cart 🎉")

def calculateTotalPrice(cart_details):
    sum = 0
    for key in cart_details:
        sum = sum+cart_details[key]
    
    return sum


if __name__ == "__main__":
    sum = calculateTotalPrice(cart_details)
    if st.button("Clear Cart"):
        cart_details.clear()
        sum = 0
    st.write(cart_details)
    st.write("Total Sum = ", sum)
    
