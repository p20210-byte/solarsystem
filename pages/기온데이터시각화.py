import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load data
data = {
    "행성": ["지구", "화성", "화성", "목성", "목성", "목성", "목성",
           "토성", "토성", "토성", "천왕성", "천왕성", "천왕성",
           "해왕성", "해왕성", "해왕성"],
    "위성": ["달", "포보스", "데이모스", "이오", "유로파", "갈리메데", "칼리스토",
           "타이탄", "엔셀라두스", "미마스", "아리엘", "티타니아", "미란다",
           "트리톤", "네레이드", "나이아드"],
    "거리(km)": [384000, 6000, 23460, 420000, 670900, 1070400, 1880000,
              1220000, 2380000, 185539, 1900000, 43600, 129900,
              350000, 5513400, 64000])
df = pd.DataFrame(data)    

# Clean and prepare data
st.title("태양계 행성과 위성 거리 시각화")

st.write("아래 그래프는 태양계 각 행성과 주요 위성 간의 평균 거리(km)를 보여줍니다.")

# 행성 선택 옵션
selected_planet = st.selectbox("행성을 선택하세요:", ["전체"] + sorted(df["행성"].unique().tolist()))

if selected_planet != "전체":
    filtered_df = df[df["행성"] == selected_planet]
else:
    filtered_df = df
    
# Calculate yearly statistics
plt.figure(figsize=(10, 6))
plt.barh(filtered_df["위성"], filtered_df["거리(km)"], color="skyblue")
plt.xlabel("거리 (km)")
plt.ylabel("위성")
plt.title(f"{selected_planet if selected_planet != '전체' else '모든 행성'}의 위성 거리")

for i, val in enumerate(filtered_df["거리(km)"]):
    plt.text(val + 50000, i, f"{val:,} km", va='center', fontsize=9)

plt.gca().invert_yaxis()  # 위에서부터 보기 좋게 정렬
st.pyplot(plt)

st.subheader("📊 데이터 테이블")
st.dataframe(filtered_df)
