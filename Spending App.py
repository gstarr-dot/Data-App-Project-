import streamlit as st 
import json 
import os 
import pandas as pd 

File = "spending.json"

def load_data():  #loads saved spending data 
    if os.path.exists(File):
        with open(File, "r") as f:
            return json.load(f)
    return []

def save_data(data):   #saves spending data
    with open(File, "w") as f:
        json.dump(data, f)

def save_data(data):   #saves spending data
    with open(File, "w") as f:
        json.dump(data, f)

#add sidebar menu 
page = st.sidebar.selectbox("Navigation", ["Home", "Charts])

#home page 
if page == "Home":

st.title("Spending Tracker") # Tittle for page

st.header("Add New Spending") # Subheader  

#User enters amount, data, and selects category 
amount = st.number_input("Amount", min_value=0.01, step=0.01)
category = st.selectbox("Category", ["Food", "Transportation", "Entertainment/Subscriptions", "Other"])
date = st.date_input("Date")

if st.button("Save spending"):
    data =load_data() 

    new_expense = {
        "amount": amount,
        "category": category,
        "date": str(date)
    }

    data.append(new_expense)
    save_data(data)

#Show all saved and new spending 
st.header("All Spending")

data = load_data()
if data:
    df = pd.DataFrame(data)
    st.dataframe(df)
else:
    st.write("No spending data available.")


