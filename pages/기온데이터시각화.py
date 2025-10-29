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

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))

for idx, row in df.iterrows():
    ax.barh(row['위성'], row['거리(km)'], color=planet_colors[row['행성']])
    ax.text(row['거리(km)'] + 50000, idx, f"{row['거리(km)']:,} km", va='center')


ax.set_xlabel("거리 (km)")
ax.set_ylabel("위성 이름")
ax.set_title("태양계 행성과 위성 간 거리 (km)")
ax.invert_yaxis()  # 위성 순서를 위에서 아래로
plt.tight_layout()


# Streamlit에 그래프 표시
st.pyplot(fig)

# 데이터 테이블
st.subheader("데이터 테이블")
st.dataframe(df)
