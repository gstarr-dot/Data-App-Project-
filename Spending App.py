import streamlit as st 
import json 
import os 
import pandas as pd 
import matplotlib.pyplot as plt 

File = "spending.json"

def load_data():  #loads saved spending data 
    if os.path.exists(File):
        with open(File, "r") as f:
            return json.load(f)
    return []

def save_data(data):   #saves spending data
    with open(File, "w") as f:
        json.dump(data, f)


#add sidebar menu 
page = st.sidebar.selectbox("Navigation", ["Home", "Charts"])

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

    selected_category = st.selectbox(
        "Filter by Category",
        ["All"] + list(df["category"].unique())
    )

    min_amount = st.slider(
        "Minimum Amount",
        0.0, 
        float(df["amount".max())
        0.0
    )

    data = load_data()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
        #Filters Subheader
        st.subheader("Filters")
        
        #Delete entries subheader
        st.subheader("Delete Entries")
        for i, expense in enumerate(data):
            st.write(
                f"{expense['date']} | "
                f"{expense['category']} | "
                f"${expense['amount']}"
            )
            
            if st.button(f"Delete Entry {i}"):
                data.pop(i)
                save_data(data)
                st.success("Entry Deleted")
                st.rerun()
                
    else:
        st.write("No spending data available.")

#Add page for charts
elif page == "Charts": 
    st.title("Spending Charts")
    data = load_data() 

    if not data:
        st.write("No Inputs - Input Data to create visuals.")
    else: 
        df = pd.DataFrame(data)

        #Groups the data
        category_totals = df.groupby("category")["amount"].sum()

        chart_type = st.selectbox("Select Chart", ["Bar Chart", "Pie Chart"])

        #Bar chart 
        if chart_type == "Bar Chart":
            st.subheader("Bar Chart for Spending by Category")
            st.bar_chart(category_totals)

        #Pie Chart
        elif chart_type == "Pie Chart":
            st.subheader("Pie Chart for Spending by Category")

            fig, ax = plt.subplots()
            ax.pie(
                category_totals, 
                labels=category_totals.index,
                autopct="%1.1f%%"
            )

            ax.axis("equal")

            st.pyplot(fig)
                   
                      
                      
                        
        
                 


