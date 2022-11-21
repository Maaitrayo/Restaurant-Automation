import streamlit as st
from data.data import login_data,access_req, current_user, userIP_check
import socket


 
# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)
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
        status = validLoginID(login_ID, password)

        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        st.write(f"{status}")
        if status == " Login Successful ":
            current_user.append(login_ID)
            userIP_check[str(IPAddr)] = login_ID
            access_req["VALIDITY"] = "VALID"
        else:
            access_req["VALIDITY"] = "NOT VALID"
        
        return status

if __name__ == "__main__"   :
    secureInfo(userID, password)
    if st.button("Logout"):
        access_req["VALIDITY"] = "NOT VALID"
        if len(current_user)!=0 and  len(userIP_check)!=0:
            current_user.pop()
            userIP_check.pop()

    st.write(userIP_check)
