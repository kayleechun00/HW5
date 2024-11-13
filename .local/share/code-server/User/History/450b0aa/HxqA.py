# put streamlit code here as needed

import altair as alt
import streamlit as st
from vega_datasets import data 
import pandas as pd

st.title("My First Streamlit App")
st.text("The URL for this app is: https://huggingface.co/kchun9")

url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
data = pd.read_csv(url)


st.text("""Number of Buildings by City:
This visualization will display the total number of buildings in each city. 
The bar chart will allow us to quickly identify which cities have the most or fewest buildings, 
providing an overview of building distribution across different locations.""")


building_count = data.groupby('City')['Location Name'].count().reset_index()
building_count.columns = ['City', 'Building Count']

chart = alt.Chart(building_count).mark_bar().encode(
    x='City:N',
    y='Building Count:Q',
    tooltip=['City', 'Building Count']
).properties(
    title="Number of Buildings by City"
).interactive()


st.altair_chart(chart, use_container_width=True)



st.text("""Total Building Square Footage by Year
This line chart will show the total building square footage constructed each year. 
By visualizing the data over time, we can observe trends in construction activity 
and understand how the total building area has evolved throughout the years. 
This helps identify periods of significant growth or decline in construction.""")

yearly_area = data.groupby('Year Constructed')['Square Footage'].sum().reset_index()
yearly_area.columns = ['Year Constructed', 'Total Square Footage']


line_chart = alt.Chart(yearly_area).mark_line().encode(
    x='Year Constructed:O',
    y='Total Square Footage:Q',
    tooltip=['Year Constructed', 'Total Square Footage']
).properties(
    title="Total Building Square Footage by Year"
).interactive()


st.altair_chart(line_chart, use_container_width=True)






st.text

filtered_data = data[['Year Constructed', 'Square Footage', 'Location Name']].dropna()
filtered_data = data[
    (data['Year Constructed'] >= 1800) & 
    (data['Year Constructed'] <= 2023)
][['Year Constructed', 'Square Footage', 'Location Name']].dropna()


scatter_plot = alt.Chart(filtered_data).mark_circle(size=40).encode(
    x=alt.X('Year Constructed:Q', title='Year Constructed', scale=alt.Scale(domain=[1800, 2023])),
    y=alt.Y('Square Footage:Q', title='Square Footage'),
    color=alt.Color('Square Footage:Q', scale=alt.Scale(scheme='plasma'), title='Square Footage'),
    tooltip=['Location Name', 'Year Constructed', 'Square Footage']
).properties(
    title='Building Size by Year Constructed',
    width=800,
    height=500
).interactive()

st.altair_chart(scatter_plot, use_container_width=True)






city_data = data[['City', 'Square Footage']].dropna()
city_sum = city_data.groupby('City').sum().reset_index()

# 총 면적 기준으로 상위 10개 도시 필터링
top_10_cities = city_sum.nlargest(10, 'Square Footage')

# 막대 그래프 생성
bar_chart = alt.Chart(top_10_cities).mark_bar().encode(
    x=alt.X('sum(Square Footage):Q', title='Total Square Footage'),
    y=alt.Y('City:N', sort='-x', title='City'),
    color=alt.Color('City:N', scale=alt.Scale(scheme='category20')),
    tooltip=['City', 'sum(Square Footage)']
).properties(
    title='Top 10 Cities by Total Square Footage',
    width=700,
    height=400
).interactive()

st.altair_chart(bar_chart, use_container_width=True)