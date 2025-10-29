import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# 데이터
data = {
    "행성 - 위성": ["지구-달", "화성-포보스", "화성-데이모스", "목성-이오", "목성-유로파", "목성-갈리메데", "목성-칼리스토",
           "토성-타이탄", "토성-엔셀라두스", "토성-미마스", "천왕성-아리엘", "천왕성-티타니아", "천왕성-미란다",
           "해왕성-트리톤", "해왕성-네레이드", "해왕성-나이아드"],
    "거리(km)": [384000, 6000, 23460, 420000, 670900, 1070400, 1880000,
              1220000, 2380000, 185539, 1900000, 43600, 129900,
              350000, 5513400, 64000]
}

df = pd.DataFrame(data)

# Streamlit 페이지 설정
st.set_page_config(page_title="태양계 위성 거리 시각화", layout="centered")
st.title("태양계 행성과 위성 간 거리 시각화")
st.write("각 행성과 위성 간의 거리(km)를 한눈에 볼 수 있습니다.")

# 그래프 그리기
plt.figure(figsize=(20, 10))
plt.bar(df["행성 - 위성"], df["거리(km)"], color='skyblue')
plt.xlabel("행성 - 위성")
plt.ylabel("거리 (km)")
plt.title("태양계 위성 거리")
plt.xticks(rotation=45)


# Streamlit에 그래프 표시
st.pyplot(plt)
