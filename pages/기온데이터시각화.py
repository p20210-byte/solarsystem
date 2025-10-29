import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 데이터
data = {
    "행성": ["지구", "화성", "화성", "목성", "목성", "목성", "목성",
           "토성", "토성", "토성", "천왕성", "천왕성", "천왕성",
           "해왕성", "해왕성", "해왕성"],
    "위성": ["달", "포보스", "데이모스", "이오", "유로파", "갈리메데", "칼리스토",
           "타이탄", "엔셀라두스", "미마스", "아리엘", "티타니아", "미란다",
           "트리톤", "네레이드", "나이아드"],
    "거리(km)": [384000, 6000, 23460, 420000, 670900, 1070400, 1880000,
              1220000, 2380000, 185539, 1900000, 43600, 129900,
              350000, 5513400, 64000]
}

df = pd.DataFrame(data)

# Streamlit 페이지 설정
st.set_page_config(page_title="태양계 위성 거리 시각화", layout="centered")
st.title("태양계 행성과 위성 간 거리 시각화")
st.write("각 행성과 주요 위성 간의 평균 거리(km)를 한눈에 볼 수 있습니다.")

# Plotly Express 막대그래프
fig = pd.bar(
    df,
    x="거리(km)",
    y="위성",
    color="행성",
    orientation="h",
    title="태양계 행성과 위성 간 거리 (km)",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# 텍스트 표시
fig.update_traces(
    text=df["거리(km)"].apply(lambda x: f"{x:,} km"),
    textposition='outside'
)

# 레이아웃 설정
fig.update_layout(
    xaxis_title="거리 (km)",
    yaxis_title="위성 이름",
    yaxis=dict(autorange="reversed"),
    title_font=dict(size=20, color='black'),
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True
)

# Streamlit에 그래프 표시
st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블
st.subheader("데이터 테이블")
st.dataframe(df)
