''' 
# What is Streamlit 

- Its a python library and Its a faster way to build and share data apps. 
- when we are working as a data analyst and data scientist then we have to deploy our ML model on some webiste so for 
  that we need to have good understanding in the website development but here comes the role of streamlit which say 
  if you run few python code then we can create a good Dashboard.
- With the help of streamlit we can create good looking, fully interactive website without learning html, css, javascript
  and flask.
- Steamlit is a libaray which is bulit on the top of react. it will use react at the backend to show the user the required 
  front end page.
  
  ===================================================================
  
### DISADVANTAGE OF STREAMLIT 
  
- We can'nt create a more customize website through it. we can just create basic website. for more customization we
  need to look into Flask. 
'''
# First we learn about the text based utility. So in this like title,header,subheader,write,markdown and latex is
# comes under the TEXT BASED UTILITY.
import streamlit as st
import pandas as pd
import time
st.title('Startup Dashboard')
st.header('I am Learning Streamlit. ')
st.subheader('I am loving it. ')
st.write('This is a normal page')

st.markdown("""
            ### My favouraite movies 
            - Race 3
            - Ultimate game
            - Pokemon 
            - Ben 10
            """)

st.code("""
        def foo(input):
          return foo**2
        x = foo(2)
        """)
st.latex('x^2+y^2+2 = 0')

# Here we have different type of DISPLAY ELEMENT like Dataframe, metrics and Json.
df = pd.DataFrame({
    "Name": ["Sahil","Arpit","Harshit"],
    "Marks":[80,70,95],
    "Package":[10,8,16]
  })
st.dataframe(df)

st.metric("Revenue","5 Lac", '3%')
st.metric("Budget","3 lac","-3%")

st.json({
    "Name": ["Sahil","Arpit","Harshit"],
    "Marks":[80,70,95],
    "Package":[10,8,16]
  })

# Here we can DISPLAY MEDIA such as Audio and video. 
st.image("Sahil Pic.jpeg")
# st.video("Task12.m4v")    # With the help of this function we can load the video
# st.audio("Task12")          # With the help of This function we can load the audio

# Here we can CREATE LAYOUT like sidebar and columns.

st.sidebar.title("Title ka Sidebar")

col1,col2 = st.columns(2)      # this will print the side by side image.

with col1:
  st.image("Sahil Pic.jpeg")
  
with col2:
  st.image("Sahil Pic.jpeg")

# Here we can display the STATUS MESSEAGE in the window like error,success,info,warning, progress bar.

st.error('Login Failed')
st.success('Code Ran')
st.info("Login Successful")
st.warning("Login Successful")

bar = st.progress(0)
for i in range(1,101):
  # time.sleep(0.5)
  bar.progress(i)
  
# Here we can take the input from the user like text input, number input, date input,button, dropdown, fileuploader.

email = st.text_input('Enter Email ')
number = st.number_input("Enter the number ")
date = st.date_input("Enter the Calender Date.")
time = st.time_input("Enter the time")







