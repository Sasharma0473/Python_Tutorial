import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')


startup_fund = pd.read_csv('startup_cleaned_data.csv')
startup_fund['date'] = pd.to_datetime(startup_fund['date'],errors='coerce')
startup_fund['year'] = startup_fund['date'].dt.year
startup_fund['month'] = startup_fund['date'].dt.month

def load_selected_investor(investor):
    st.title(investor)
    
    # Load the 5 recent investment
    last5_df = startup_fund[startup_fund['investor'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader("Most Recent Five Investment of Investor")
    st.dataframe(last5_df)
    
    col1,col2 = st.columns(2)
    
    # Top 5 biggest investment 
    with col1:
        big5_investment = startup_fund[startup_fund['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending = False).head()
        st.subheader("Top Five Biggest Investment")
        st.dataframe(big5_investment)
        
    # Here we are plotting the graph of big 5 investment
    with col2:
        big5_investment_series = startup_fund[startup_fund['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending = False).head()
        st.subheader("Top Five Biggest Investment")
        fig,ax = plt.subplots()
        ax.bar(big5_investment_series.index,big5_investment_series.values)
        st.pyplot(fig)
    
    col3, col4 = st.columns(2)
    
    with col3:
        vertical_series = startup_fund[startup_fund['investor'].str.contains(investor)].groupby('vertical')['amount'].sum().head()
        st.subheader('Investment in Each Vertical')
        st.dataframe(vertical_series)
    
    with col4:
        # Here we are plotting the pie chart showing the total amount on the baisc of vertical invest by the investor.
        vertical_series = startup_fund[startup_fund['investor'].str.contains(investor)].groupby('vertical')['amount'].sum().head().sort_values(ascending = False)
        st.subheader("Investment in Each Vertical")
        fig1,ax1 = plt.subplots()
        ax1.pie(vertical_series, labels=vertical_series.index,autopct = '%0.01f')
        st.pyplot(fig1)
        
    col5, col6 = st.columns(2)
    
    with col5:
        round_series = startup_fund[startup_fund['investor'].str.contains('investor')].groupby('round')['amount'].sum().head().sort_values(ascending = False)
        st.subheader('Investment In Each Round')
        st.dataframe(round_series)
        
    with col6:
        round_series = startup_fund[startup_fund['investor'].str.contains('investor')].groupby('round')['amount'].sum().head().sort_values(ascending = False)
        st.subheader("Investment in Each Round")
        fig2,ax2 = plt.subplots()
        ax2.pie(round_series, labels=round_series.index,autopct = '%0.01f')
        st.pyplot(fig2)
        
    col7, col8 = st.columns(2)
    
    with col7:
        city_series = startup_fund[startup_fund['investor'].str.contains('investor')].groupby('city')['amount'].sum().head().sort_values(ascending = False)
        st.subheader('Investment In Each City')
        st.dataframe(city_series)
        
    with col8:
        city_series = startup_fund[startup_fund['investor'].str.contains('investor')].groupby('city')['amount'].sum().head().sort_values(ascending = False)
        st.subheader("Investment in Each City")
        fig3,ax3 = plt.subplots()
        ax3.pie(city_series, labels=city_series.index,autopct = '%0.01f')
        st.pyplot(fig3)
    
    # print(startup_fund.info())
    col9, col10 = st.columns(2)
    
    with col9:
        year_series = startup_fund[startup_fund['investor'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader('Year On Year Investment')
        st.dataframe(year_series)
        
    with col10:
        startup_fund['year'] = startup_fund['date'].dt.year
        year_series = startup_fund[startup_fund['investor'].str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader("Year On Investment")
        fig4,ax4 = plt.subplots()
        ax4.plot(year_series.index, year_series.values)
        st.pyplot(fig4)
        
def load_selected_startup(startup):
    st.title(startup)
    st.subheader('StartUp Details')
    startup_details= startup_fund[startup_fund['startup'].str.contains(startup)][['vertical','sub vertical','city']]
    st.dataframe(startup_details)
 

def load_overall_analysis():
    st.title('Overall Analysis')  
    col1,col2,col3,col4 = st.columns(4)  
    
    
    # Total Invested Amount
    with col1:
        total = round(startup_fund['amount'].sum())
        st.metric('Total Money', str(total)+' cr')
    # Maximum Amount Infused in the startup
    with col2:
        max_amount = startup_fund.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0]
        st.metric('Max Amount Invested' , str(max_amount)+' cr')
    with col3:
        mean_startup = round(startup_fund.groupby('startup')['amount'].sum().mean())
        st.metric('Mean ', str(mean_startup)+' cr')
    with col4:
        num_startup = startup_fund['startup'].nunique()
        st.metric('No of Startup', num_startup)
    
    col11, col12 = st.columns(2)
    
    with col11:
        st.subheader("Month On Month Graph")
        select_options = st.selectbox('Select Type', ['Total','Count'])
        if select_options == 'Total':
            temp_df = startup_fund.groupby(['year','month'])['amount'].sum().reset_index()
            temp_df['x_axis']= temp_df['year'].astype('str') +'-'+ temp_df['month'].astype('str')

            fig5,ax5 = plt.subplots()
            ax5.plot(temp_df['x_axis'],temp_df['amount'])
            # plt.xticks(rotation='vertical')
            # plt.xlim('2015-1','2015-12')
            st.pyplot(fig5)
        else:
            temp_df = startup_fund.groupby(['year','month'])['amount'].count().reset_index()
            temp_df['x_axis']= temp_df['year'].astype('str') +'-'+ temp_df['month'].astype('str')
            fig5,ax5 = plt.subplots()
            ax5.plot(temp_df['x_axis'],temp_df['amount'])
            # plt.xticks(rotation='vertical')
            # plt.xlim('2015-1','2015-12')
            st.pyplot(fig5)
    
    with col12:
        st.subheader('Amount in Top Sector')
        select_options1 = st.selectbox('Select Type', ['Total1', 'Count1'])
        if select_options1 == 'Total1':
            top_sector = startup_fund.groupby('vertical')['amount'].sum().sort_values(ascending = False).head()
        else:
            top_sector = startup_fund.groupby('vertical')['amount'].count().sort_values(ascending = False).head()
        fig8,ax8 = plt.subplots()
        ax8.pie(top_sector, labels=top_sector.index, autopct='%0.01f')
        st.pyplot(fig8)
    
    col13,col14 = st.columns(2)
    
    with col13:
        # It will give the category wise funding in each sector.
        st.subheader("Category wise Amount Funding ")
        amount_fund = startup_fund.groupby('round')['amount'].sum().sort_values(ascending = False).head(5)
        fig9,ax9 = plt.subplots()
        ax9.pie(amount_fund, labels=amount_fund.index, autopct='%0.01f')
        st.pyplot(fig9)
    
    with col14:
        # This will give the city wise funding in India 
        st.subheader('City Wise Funding')
        city_fund = startup_fund.groupby('city')['amount'].sum().sort_values(ascending = False).head(5)
        fig10, ax10 = plt.subplots()
        ax10.pie(city_fund,labels = city_fund.index,autopct='%0.01f')
        st.pyplot(fig10)
        
    col_1, col_2 = st.columns(2)
    
    with col_1:
        # Here we are are calculating the year wise top start. 
        st.subheader('Year Wise Top Startup')
        top_startup_yearwise = startup_fund.groupby(['year','startup'])['amount'].sum().nlargest(10).sort_index(ascending = False)
        fig_1,ax_1 = plt.subplots()
        ax_1.pie(top_startup_yearwise, labels=top_startup_yearwise.index, autopct='%0.01f')
        st.pyplot(fig_1)
    
    # Here we are calculating the top investor
    st.subheader('Top Investor')
    top_investor = startup_fund.groupby('investor')['amount'].sum().sort_values(ascending = False).head()
    fig_2,ax_2 = plt.subplots()
    ax_2.pie(top_investor, labels=top_investor.index, autopct='%0.01f')
    st.pyplot(fig_2)
    
    
    
    # with col3:
    #     startup_name = startup_fund.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).index[0]
    #     st.metric(st.write('Name of Startup Is', startup_name))
    
    
        
# startup_fund['investor_name'] = startup_fund['investor_name'].fillna('Undisclosed')
# There are few missing values in the Investor Name, So we have fill those missing values with undisclosed with the 
# help of below code.

# st.dataframe(startup_fund)
st.sidebar.title('Startup Funding Analysis')
options = st.sidebar.selectbox('Select One ', ['Overall Analysis','StartUp','Investor'])

if options == 'Overall Analysis':
    load_overall_analysis()
elif options == 'StartUp':
    selected_startup = st.sidebar.selectbox('Select StartUp',sorted(startup_fund['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    if btn1:
        load_selected_startup(selected_startup)
    # st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(startup_fund['investor'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_selected_investor(selected_investor)
    # st.title('Investor Analysis')
