# Project 3 – The Use of Data Engineering to Analyze Stock Market 

# Project members: 
Manal Bayoumi, Rocio Cantu, and Melissa Mosby.

# Project Overview: 
Our project will analyze the stock data for different companies: Alphabet Inc. (aka Google), Apple Inc., Intel Corporation, Microsoft Corporation, and Oracle Corporation. Also, it will price and volume of purchase for these stocks on different dates. 

## That project will determine various questions when analyzing these stocks:
•	How do investors pick up their stocks?
•	In buying and selling stocks, do investors depend on the opening or the closing prices of stocks?
•	What factors make stock prices rise or fall for a company like Apple, Google, Intel, Oracle, Microsoft?
•	What is the % of change for stocks for a company like Apple, Google, Intel, Oracle, Microsoft ?
Our analysis will follow a data engineering track. We will employ jupyter notebook and pandas to capture and modify our data using ELT workflows. Next, we will feed our data into SQL. Also, we will generate an ERD diagram to show the relationships of our database tables. We will create a method to read our data from the database with pandas DataFrame. 

## Project Instructions:
First, you need to download the yahoo finance and pandas-data reader packages. In order to do this, please run the following commands in jupyter notebook: 
!pip install yfinance. 
!pip install pandas-datareader.

## Project is divided into three parts
This app include three parts.   
1. Part I ETL
   * this is a jupyter file, follow ETL principle extract data from yahoo finance, transform data by python pandas library, then load into a sqlite database
2. Part II Display
   * this is another jupyter file, download data from database and display for users
3. Part III Web with plotly.js library
   * this is a python file, using steamlit and plotly.js, which is not covered in the lecture.

## Required Package Download
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

## There are several reasons why my group decided to use SQLite:
•	SQLite is a SQL based database that can create a single database file that can easily be uploaded to GitHub and shared with other group members.
•	SQLite facilities the work when using multiple databases. 
•	We can DB Browser read SQLite file and check if the file performs well.
•	SQLite is small like a paper; however, the other SQL is a big library. 
•	Download DB Browser at this link https://sqlitebrowser.org.

## Why SQL is better than MongoDB?
Using SQL over NoSQL in that project is better because stock databases are saved in a table form. SQL can perform analytical queries, such as filters, joins, merges, and aggression on the data. SQL databases are better for multi-row transactions, while NoSQL is better for unstructured data (Smallcombe, 2023).

## Project Ethical Considerations:
There are several efforts for ethical considerations made in the project, such as acknowledging the contribution of others when using data. By that, we mean that we site the code of others if we use it. 
In dealing with data, the data analysts must be transparent when analyzing data free from biased. 

## References
“Alphabet Inc. (GOOG) Stock Historical Prices & Data.” Yahoo! Finance, Yahoo!, 16 Jan. 2024, https://finance.yahoo.com/quote/GOOG/history?p=GOOG 
“Apple Inc. (AAPL) Stock Historical Prices & Data.” Yahoo! Finance, Yahoo!, 16 Jan. 2024, https://finance.yahoo.com/quote/AAPL/history?p=AAPL
“Intel Corporation Stock. (INTC) Stock Historical Prices & Data.” Yahoo! Finance, Yahoo!, 16 Jan. 2024, https://finance.yahoo.com/quote/INTC/history?p=INTC
“Microsoft Corporation Stock. (MSFT) Stock Historical Prices & Data.” Yahoo! Finance, Yahoo!, 16 Jan. 2024, https://finance.yahoo.com/quote/MSFT/history?p=MSFT
“Oracle Corporation Stock. (ORCL) Stock Historical Prices & Data.” Yahoo! Finance, Yahoo!, 16 Jan. 2024, https://finance.yahoo.com/quote/ORCL/history?p=ORCL
Smallcombe, Mark. “SQL VS NOSQL: 5 Critical Differences.” Integrate.Io, 9 Nov. 2023, www.integrate.io/blog/the-sql-vs-nosql-difference/#two. 



