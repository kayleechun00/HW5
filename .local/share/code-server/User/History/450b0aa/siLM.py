# put streamlit code here as needed

import altair as alt
import streamlit as st
from vega_datasets import data 
import pandas as pd

st.title("My First Streamlit App")

url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
data = pd.read_csv(url)

