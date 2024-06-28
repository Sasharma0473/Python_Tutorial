import streamlit as st

email = st.text_input("Enter the Email")
password = st.text_input("Enter the Password")
gender = st.selectbox('Select Gender',['Male','Female','Others'])

btn = st.button("Log IN")


# If the button is clicked then The login is successful otherwise it failed.
if btn:
    if email == 'sasharma8859@gmail.com' and password == '1234':
        st.success("Login Successful")
        st.balloons()
        st.write(gender)
    else:
        st.error("Login Failed")