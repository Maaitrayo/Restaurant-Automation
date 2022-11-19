import streamlit as st
import datetime
from data.data import access_req



from data.data import chat_data


st.markdown("Welcome to your Global Chat")
st.sidebar.markdown(f"Global Chat 🎉")

userName = st.text_input('User Id')
message = st.text_input('Message')



# if userName != "" and message != "":
#     chat_data[userName] = message

def chatInterface():
    if st.button("Clear Chat"):
        chat_data.clear()

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

