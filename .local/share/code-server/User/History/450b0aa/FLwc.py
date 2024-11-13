# put streamlit code here as needed

import altair as alt
import streamlit as st
from vega_datasets import data 
import pandas as pd

st.title("My First Streamlit App")
st.text("The URL for this app is: https://huggingface.co/kchun9")

url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
data = pd.read_csv(url)

st.write(data.head())


# City별 건물 수 계산
building_count = data.groupby('City')['Location Name'].count().reset_index()
building_count.columns = ['City', 'Building Count']

# Altair 막대 그래프
chart = alt.Chart(building_count).mark_bar().encode(
    x='City:N',
    y='Building Count:Q',
    tooltip=['City', 'Building Count']
).properties(
    title="City별 건물 개수"
).interactive()

# Streamlit 앱에 그래프 표시
st.altair_chart(chart, use_container_width=True)
st.text("이 그래프는 각 도시별 건물 수를 보여줍니다.")


# Year Constructed별 총 면적 계산
yearly_area = data.groupby('Year Constructed')['Square Footage'].sum().reset_index()
yearly_area.columns = ['Year Constructed', 'Total Square Footage']

# Altair 라인 차트
line_chart = alt.Chart(yearly_area).mark_line().encode(
    x='Year Constructed:O',
    y='Total Square Footage:Q',
    tooltip=['Year Constructed', 'Total Square Footage']
).properties(
    title="연도별 건물의 총 면적 변화"
).interactive()

# Streamlit 앱에 그래프 표시
st.altair_chart(line_chart, use_container_width=True)
st.text("이 그래프는 연도별로 건설된 건물의 총 면적 변화를 보여줍니다.")





filtered_data = data[['Year Constructed', 'Square Footage', 'Building Name']].dropna()
filtered_data = filtered_data[
    (filtered_data['Year Constructed'] >= 1920) & 
    (filtered_data['Year Constructed'] <= 2023)
]

# 그래프 1: 산점도 (Year Constructed vs. Square Footage)
scatter_plot = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x=alt.X('Year Constructed:Q', title='Year Constructed'),
    y=alt.Y('Square Footage:Q', title='Square Footage'),
    color=alt.Color('Square Footage:Q', scale=alt.Scale(scheme='viridis'), title='Square Footage'),
    tooltip=['Building Name', 'Year Constructed', 'Square Footage']
).properties(
    title='Building Size by Year Constructed',
    width=700,
    height=400
).interactive()

st.altair_chart(scatter_plot, use_container_width=True)