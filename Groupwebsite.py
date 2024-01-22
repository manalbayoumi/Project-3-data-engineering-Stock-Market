import pandas as pd
import sqlite3
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st 


def Database_to_Frame(table_name):
    """extract the data from the database and convert it to python dataframe"""
    query=f"Select * from {table_name}"
    value=engine.execute(query)
    query=f"""SELECT name FROM PRAGMA_TABLE_INFO('{table_name}')"""
    column=engine.execute(query)
    clean_column=[]
    for item in list(column):
        clean_column.append(item[0])
    temp=pd.DataFrame(value,columns=clean_column)
    temp["date"]=pd.to_datetime(temp["date"])
    temp.set_index("date",inplace=True)
    return temp

def bubble(df):
    """Given me any dataframe, plot a bubble chart by plotly.js"""
    temp=df.dropna()
    fig=px.scatter(temp,x=temp.index, y="Percentage_change",size=temp["Percentage_change"].abs(),color=temp["Percentage_change"])
    return fig

def candleplot(candle,title="candle_plot_for_stock"):
    """Given me any dataframe, plot a candle chart by plotly.js"""
    fig=go.Figure(data=[go.Candlestick(x=candle.index,open=candle["Open"],close=candle["Close"], high=candle["High"], low=candle["Low"], 
                        increasing_line_color="green", decreasing_line_color="red")])
    fig.update_layout(title=title)
    return fig

engine=sqlite3.connect("Group_Project_3.db")
# ----------------------------------------------------------
# Manipulating a web
st.set_page_config(layout="wide")
with st.sidebar:
    buttona=st.button("Introduction")
    button1=st.button("Installation")
    button0=st.button("Project Overview")
    button2=st.button("Original and ETL Data")
    button3=st.button("Display the Data")
    button4=st.button("SQLite")
    button5=st.button("ERD")
    stock=st.radio("select a stock",key="visibility",options=["Apple","Google","Intel","Oracle","Microsoft"])
    button6=st.button("Plotting the Data")
    button8=st.button("About the Group")
    button9=st.button("Conclusion")
 

st.title(":green[Project 3] :violet[Data] :blue[Engineering]")
st.write("---")

if buttona:
    st.image("./Web/data.jpg")

elif button0: 
    intro="""
     
## Our project will analyze historical stock data for five companies:
#
#

"""
    st.write(intro)    
    col1,col2,col3,col4, col5=st.columns(5)
    with col1:
        st.image("./Web/Google.png")
    with col2:
        st.image("./Web/Apple.png") 
    with col3:
        st.image("./Web/intel.png")
    with col4:
        st.image("./Web/Microsoft.jpg",width=180)
    with col5:
        st.image("./Web/Oracle.png")
    

elif button1: 
    message="""
    ### Required downloaded package
    *Please run the following command in jupyter or bash terminal*
```bash
!pip install yfinance
!pip install pandas-datareader
!pip install streamlit --upgrade
!pip install plotly
```
## Run the web server
* navigate to the correct folder
* make sure you have run `Required Package Download` at least once
```python
streamlit run Groupwebsite.py
```
"""
    st.write(message)

elif button2:
    st.write("# Original Data")
    st.image("./Web/before_ETL.png")
    st.write("---")

    st.write("# Transformed Data")
    st.image("./Web/after_ETL.png")
    text="""
    To make it more efficent for analyzing, use `ETL` to transform data, including:
* Adding the following column
   * stock_ticker: for easily identify stocks.
   * normalization: for comparing different stock gain and loss.
   * percentage_change: to determine which is the best and worst day to invest.
   * accumulative_return: to determine how investor get return from the market.
   * Changing datatype for database to record.
   * removing redundant floating point. 

"""
  
    st.write(text)

elif button3: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    st.write(df)

elif button4:
    st.write("# SQLite Tables")
    st.image("./Web/Sqlite_table.PNG")
    st.write("# Apple Stock")
    st.image("./Web/Sql_Apple.PNG")
    
elif button5:   
    st.write("# ERD")
    st.image("./Web/ERDdiagram.jpg")


elif button6: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    fig=bubble(df)
    st.plotly_chart(fig,use_container_width=True)
    fig=candleplot(df, stock)
    st.plotly_chart(fig,use_container_width=True)


elif button8:
    col1,col2,col3=st.columns(3)
    with col1:
        st.write("# Melissa Mosby")
        st.image("./Web/Melissa_picture_8272.jpg")
    with col2:
        st.write("# Rocio Cantu")
        st.image("./Web/Rocio_picture_2903.jpg") 
    with col3:
        st.write("# Manal Bayoumi")
        st.image("./Web/Manal_picture_7035.jpg")

elif button9: 
    message="""

# List of possible questions in the next data analysis step:
* How do investors pick their stocks?   
* In buying and selling stocks, do investors depend on the opening or the closing prices of stocks?
* What factors make stock prices rise or fall for a company like Apple, Google, Intel, Oracle, Microsoft?
* What makes an investor pick one company's stock over another?

"""

    st.write(message)






    

    





