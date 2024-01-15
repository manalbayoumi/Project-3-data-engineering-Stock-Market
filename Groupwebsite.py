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
    button1=st.button("display the data")
    button2=st.button("plotting the data")
    button3=st.button("plotting the candle")
    button4=st.button("About the Group")



st.title(":green[Project_3] :violet[Data] :blue[Engineering]")
st.write("---")


if button1: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    st.write(df)

elif button2: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    fig=bubble(df)
    st.plotly_chart(fig,use_container_width=True)

elif button3: 
    temp=stock+"_price"
    df=Database_to_Frame(temp)
    fig=candleplot(df, stock)
    st.plotly_chart(fig,use_container_width=True)

elif button4: 
    st.write(":green[Manal Bayoumi]")
    st.write(":red[Melissa Mosby]")
    st.write(":blue[Rocio Cantu]")

else: st.image("title.png")
    

    





