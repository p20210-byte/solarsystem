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

st.set_page_config(page_title="태양계 행성 위성 거리 시각화", layout="centered")

st.title("태양계 행성과 위성 간 거리 시각화")
st.write("각 행성과 위성 간의 평균 거리(km)를 시각화합니다.")


planets = ["전체"] + sorted(df["행성"].unique().tolist())
selected_planet = st.selectbox("행성을 선택하세요:", planets)


if selected_planet != "전체":
    filtered_df = df[df["행성"] == selected_planet]
else:
    filtered_df = df.copy()

fig = px.bar(
    filtered_df,
    x="거리(km)",      
    y="위성",            
    color="행성" if selected_planet == "전체" else None, 
    orientation="h",    
    title=f"{selected_planet if selected_planet != '전체' else '모든 행성'}의 위성 거리 (km)",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_traces(
    text=filtered_df["거리(km)"].map(lambda x: f"{x:,} km"),
    textposition='outside'
)

fig.update_layout(
    xaxis_title="거리 (km)",
    yaxis_title="위성 이름",
    yaxis=dict(autorange="reversed"), 
    title_font=dict(size=20, color='black'),
    xaxis=dict(showgrid=True),
    plot_bgcolor='rgba(0,0,0,0)',     
    showlegend=(selected_planet == "전체")
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("데이터 테이블")
st.dataframe(filtered_df)

st.caption("참고: 데이터는 예시이며, 실제 거리와 다를 수 있습니다.")
