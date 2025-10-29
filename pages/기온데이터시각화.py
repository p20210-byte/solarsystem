import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

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

st.set_page_config(page_title="태양계 위성 거리 시각화", layout="centered")

st.title("🌞 태양계 행성과 위성 사이의 거리 시각화")
st.write("각 행성과 주요 위성 간의 평균 거리(km)를 시각적으로 확인할 수 있습니다.")

planets = ["전체"] + sorted(df["행성"].unique().tolist())
selected_planet = st.selectbox("행성을 선택하세요:", planets)

if selected_planet != "전체":
    filtered_df = df[df["행성"] == selected_planet]
else:
    filtered_df = df

fig = px.bar(
    filtered_df,
    x="거리(km)",
    y="위성",
    color="행성",
    orientation="h",
    title=f"{selected_planet if selected_planet != '전체' else '전체 행성'}의 위성 거리 (km)",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_traces(text=filtered_df["거리(km)"].map(lambda x: f"{x:,} km"), textposition='outside')

fig.update_layout(
    xaxis_title="행성과 위성 사이의 거리 (km)",
    yaxis_title="위성 이름",
    yaxis=dict(autorange="reversed"),  # 위에서부터 정렬
    title_font_size=20,
    showlegend=(selected_planet == "전체")
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 데이터 테이블")
st.dataframe(filtered_df)
