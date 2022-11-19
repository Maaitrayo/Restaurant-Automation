import streamlit as st
from data.data import login_data

st.markdown("# Register")

userID = st.text_input('User Id')
password = st.text_input('Password')

def createUserAccount(new_loginID, new_password):
    user = new_loginID
    password = new_password
    if (user!="" and password!=""):
        login_data[user] = password
    status = " User Registered "
    return status 

if st.button('Register'):
    login_ID = userID   
    password = int(password)
    status = createUserAccount(login_ID, password)
    st.write(f"{status}")