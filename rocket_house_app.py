import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout = "wide")
@st.cache(allow_output_mutation=True)
def get_data(path):

    data = pd.read_csv(path)
    return data


#reading the data

path = "kc_house_data.csv"
data = get_data(path)

data["price/sqft_living"] = data["price"]/data["sqft_living"]

#formating the site



st.title("	:rocket: House Rocket App")
c1, c2 = st.columns((1, 1) )  


#creating the widgets

feature_dropdown = st.sidebar.multiselect(
                                "Select Features to filter",
                                options = data.columns
                                    )


zipcode_dropdown = st.sidebar.multiselect(
                                "Select Zipcode to filter",
                                options = data["zipcode"].unique()
                                    )

#printing the data



if ((zipcode_dropdown != []) & (feature_dropdown != [])):
    data = data.loc[data["zipcode"].isin(zipcode_dropdown)][feature_dropdown]
elif((zipcode_dropdown != []) & (feature_dropdown == [])):
    data = data.loc[data["zipcode"].isin(zipcode_dropdown)]
elif((zipcode_dropdown == []) & (feature_dropdown != [])):
    data = data[feature_dropdown]
else:
    data = data.copy()

st.header("Data overview")  
st.dataframe(data)


df1 = data[["id","zipcode"]].groupby("zipcode").count().reset_index()
df2 = pd.merge(df1,data[["price","zipcode"]].groupby("zipcode").mean().reset_index())
df3 = pd.merge(df2,data[["sqft_living","zipcode"]].groupby("zipcode").mean().reset_index())
df4 = pd.merge(df3,data[["price/sqft_living","zipcode"]].groupby("zipcode").mean().reset_index())
df4.columns = ["zipcode","count","price","sqft_living","price/sqft_living"]

c1.header("Average Values")
c1.dataframe(df4)

c2.header("Descriptive Anlysis")
c2.dataframe(data.describe())