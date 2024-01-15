# Project III Tech Stock Data Engineering
   
---
## Instructions
This app include three parts.   
1. PartI ETL
   * this is a jupyter file, follow ETL principle extract data from yahoo finance, transform data by python pandas library, then load into a sqlite database
2. PartII Display
   * this is another jupyter file, download data from database and display for users
3. PartIII Web with plotly.js library
   * this is a python file, using steamlit and plotly.js, which not covered in the lecture. create a interactive webpage to the user

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
```
