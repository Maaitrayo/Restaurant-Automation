import streamlit as st
from data.data import login_data

def checkPassword(login_ID,password):
    if(login_data[login_ID] == password):
        status = " Login Successful " 
    else:
        status = "[!] Login Unsuccessful [!] "
    return status

def validLoginID(login_ID, password):
    if(login_ID in login_data.keys()):
        status = checkPassword(login_ID,password)
    else:
        status = "[!] Invalid login ID [!] "
    return status

# def createUserAccount(new_loginID, new_password):
#     user = new_loginID
#     password = new_password
#     if (user!="" and password!=""):
#         login_data[user] = password
#     print(" User Registered ")


st.title('Restaurent Management System')
st.markdown("# Login")

userID = st.text_input('User Id')
password = st.text_input('Password')

if st.button('Submit'):
    login_ID = userID   
    password = int(password)
    status = validLoginID(login_ID, password)
    st.write(f"{status}")
