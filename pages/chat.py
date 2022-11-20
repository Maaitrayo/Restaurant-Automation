import streamlit as st
import datetime
import socket
from data.data import access_req, login_data, current_user, userIP_check



from data.data import chat_data

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

if len(userIP_check)!=0:
    st.markdown(f"Welcome to {userIP_check[str(IPAddr)]}'s Global Chat")
else:
    st.markdown(f"Welcome to your Global Chat")
st.sidebar.markdown(f"Global Chat 🎉")

userName = st.text_input('User Id')
message = st.text_input('Message')



# if userName != "" and message != "":
#     chat_data[userName] = message

def checkAdmin():
    admin = False
    # for names in current_user:
    if current_user[-1] in ["Maaitrayo", "Hrittik", "koushik", "Hrishabh"]:
        admin = True
    return admin

def chatInterface():
    clear = st.button("Clear Chat", key=1)
    if clear:
        if checkAdmin():
            chat_data.clear()
        else:
            st.write("Only for admins")

    publish = st.button("Publish")
    if publish:
        if userName != "" and message != "":
            datetime_object = datetime.datetime.now()
            user = f"{userName}_{datetime_object}"
            chat_data[user] = message
    return chat_data

if __name__ == "__main__":
    if access_req["VALIDITY"] == "VALID":
        chatInterface()
        st.write(chat_data)
    else:
        st.write("[!] Login First [!]" )

