# put streamlit code here as needed

import altair as alt
import streamlit as st
from vega_datasets import data 
import pandas as pd

st.title("My First Streamlit App")

url = "https://raw.githubusercontent.com/UIUC-iSchool-DataViz/is445_data/main/building_inventory.csv"
data = pd.read_csv(url)

st.write(data.head())


building_count = data.groupby('Campus')['Building Number'].count().reset_index()
building_count.columns = ['Campus', 'Building Count']

# Streamlit select box 추가
selected_campus = st.selectbox("Select a Campus", building_count['Campus'])

# 선택한 캠퍼스 데이터 필터링
filtered_data = building_count[building_count['Campus'] == selected_campus]

# Altair 막대 그래프
chart = alt.Chart(filtered_data).mark_bar().encode(
    x='Campus',
    y='Building Count',
    tooltip=['Campus', 'Building Count']
).interactive()  # Zoom and pan 가능

st.altair_chart(chart, use_container_width=True)

# 연도별 총 건물 면적 계산
yearly_area = data.groupby('Year Built')['Gross Square Feet'].sum().reset_index()
yearly_area.columns = ['Year Built', 'Total Gross Square Feet']

# Altair 라인 차트
line_chart = alt.Chart(yearly_area).mark_line().encode(
    x='Year Built:O',  # 연도를 순서대로 표시
    y='Total Gross Square Feet:Q',
    tooltip=['Year Built', 'Total Gross Square Feet']
).interactive()  # 줌/팬 가능

st.altair_chart(line_chart, use_container_width=True)
