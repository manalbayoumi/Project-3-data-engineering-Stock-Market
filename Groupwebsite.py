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
    stock=st.radio("select a stock",key="visibility",options=["Apple","Google","Intel","Oracle","Microsoft"])
    button0= st.button("Introduction")
    button1=st.button("Orginal and ETL Data")
    button2=st.button("SQLite")
    button3=st.button("ERD")
    button4=st.button("Display the Data")
    button5=st.button("Plotting the Data")
    button6=st.button("Plotting the Candle")
    button7=st.button("About the Group")
    button8=st.button("Conclusion")
    button9=st.button("References")


st.title(":green[Project 3] :violet[Data] :blue[Engineering]")
st.write("---")

if button0: 
    intro="""
    # Project Overview: 
### Our project will analyze historical stock data for five companies:    
*  :blue[Alphabet Inc. (aka Google)]
* :red[Apple Inc.]
* :violet[Intel Corporation]
* :green[Microsoft Corporation]
* :orange[Oracle Corporation]   

"""
    st.write(intro)
elif button1:
    st.write("# Original Data")
    st.image("./Web/before_ETL.png")
    st.write("---")

    st.write("# Transformed Data")
    st.image("./Web/after_ETL.png")
    text="""
    To make it more efficent for analysing, use `ETL` to transform data, including
* Adding addtional column
   * stock_ticker: for easily identify stocks.
   * normalization: for comparing different stock gain and loss.
   * percentage_change: to determine which is the best and worst day to invest.
   * accumulative_return: to determine how investor get return from the market.
* Changing datatype for database to record.
* remove redundant floating point. 
"""
    st.write(text)
elif button2:
    st.write("# SQLite Tables")
    st.image("./Web/Sqlite_table.PNG")
    st.write("# Apple Stock")
    st.image("./Web/Sql_Apple.PNG")
    
elif button3:   
    st.write("# ERD")
    st.image("./Web/ERDdiagram.jpg")


elif button4: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    st.write(df)

elif button5: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    fig=bubble(df)
    st.plotly_chart(fig,use_container_width=True)

elif button6: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    fig=candleplot(df, stock)
    st.plotly_chart(fig,use_container_width=True)

elif button7: 
    st.write(":green[Manal Bayoumi]")
    st.write(":red[Melissa Mosby]")
    st.write(":blue[Rocio Cantu]")

elif button8: 
    message="""

## That project will determine various questions when analyzing these stocks:
* How do investors pick up their stocks?   
They analyze the data, check the daily price for the stock. They try to understand the company's business before choosing a stock.
* In buying and selling stocks, do investors depend on the opening or the closing prices of stocks?
* What factors make stock prices rise or fall for a company like Apple, Google, Intel, Oracle, Microsoft?


* Our analysis will follow a data engineering track. We will employ jupyter notebook and pandas to capture and modify our data using ELT workflows. 
Next, we will feed our data into SQL. Also, we will generate an ERD diagram to show the relationships of our database tables. 
We will create a method to read our data from the database with pandas DataFrame. 

"""
    st.write(message)

elif button9: 
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

else: st.image("title.png")


    

    





