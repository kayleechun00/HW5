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



st.write("Year Constructed 분포:", data['Year Constructed'].describe())
st.write("Year Constructed 고유 값들:", data['Year Constructed'].unique())


# 필요한 열 필터링 및 전처리
filtered_data = data[['Year Constructed', 'Square Footage', 'Location Name']].dropna()
filtered_data = data[
    (data['Year Constructed'] >= 1800) & 
    (data['Year Constructed'] <= 2023)
][['Year Constructed', 'Square Footage', 'Location Name']].dropna()

# 산점도 생성
scatter_plot = alt.Chart(filtered_data).mark_circle(size=60).encode(
    x=alt.X('Year Constructed:Q', title='Year Constructed', scale=alt.Scale(domain=[1800, 2023])),
    y=alt.Y('Square Footage:Q', title='Square Footage'),
    color=alt.Color('Square Footage:Q', scale=alt.Scale(scheme='plasma'), title='Square Footage'),
    tooltip=['Location Name', 'Year Constructed', 'Square Footage']
).properties(
    title='Building Size by Year Constructed',
    width=700,
    height=400
).interactive()

st.altair_chart(scatter_plot, use_container_width=True)







# 도시별 총 면적 합계 계산
city_data = data[['City', 'Square Footage']].dropna()
city_sum = city_data.groupby('City').sum().reset_index()

# 막대 그래프 생성
bar_chart = alt.Chart(city_sum).mark_bar().encode(
    x=alt.X('sum(Square Footage):Q', title='Total Square Footage'),
    y=alt.Y('City:N', sort='-x', title='City'),
    color=alt.Color('City:N', scale=alt.Scale(scheme='category20')),
    tooltip=['City', 'sum(Square Footage)']
).properties(
    title='Total Square Footage by City',
    width=700,
    height=400
).interactive()

st.altair_chart(bar_chart, use_container_width=True)
