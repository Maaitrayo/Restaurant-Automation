import streamlit as st
from data.data import login_data
from data.data import access_req

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


st.title('Restaurent Management System')
st.markdown("# Login")

userID = st.text_input('User Id')
password = st.text_input('Password')

def secureInfo(userID, password):
    if st.button('Submit'):
        login_ID = userID   
        password = int(password)
        status = validLoginID(login_ID, password)
        st.write(f"{status}")
        if status == " Login Successful ":
            access_req["VALIDITY"] = "VALID"
        return status

if __name__ == "__main__"   :
    secureInfo(userID, password)
