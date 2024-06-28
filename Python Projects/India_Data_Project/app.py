import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide',page_title='India Data')

# Read the file 
India_data = pd.read_csv('India.csv')

# Take the state as a list to create a dropdown in the sidebar menu of India Data Visulization Project.
state_list = India_data['State'].unique().tolist()
state_list.insert(0,'OverAll India')

st.sidebar.title("India's Data Visualization")
selected_states = st.sidebar.selectbox('Select a State',state_list)
primaray_parameter = st.sidebar.selectbox('Select Primaray Parameter',sorted(India_data.columns[6:]))
secondary_parameter = st.sidebar.selectbox('Select Secondary Parameter', sorted(India_data.columns[6:]))
plot = st.sidebar.button('Plot Graph')

if plot:
    st.text("Size Represent Primaray Parameter")
    st.text("Color Represent Secondary parameter")
    if selected_states == 'OverAll India':
        # Plot Graph for India
        fig = px.scatter_mapbox(India_data,lat='Latitude',lon='Longitude',zoom=3,size=primaray_parameter,hover_name='District',
                                color= secondary_parameter, mapbox_style='carto-positron',width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)
    else:
        # Plot for States
        state_df = India_data[India_data['State']== selected_states]
        fig = px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',zoom=5,size=primaray_parameter,hover_name='District',
                                color= secondary_parameter, mapbox_style='carto-positron',width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)
