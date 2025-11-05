import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
# 데이터
data = {
    "행성 - 위성": ["Earth-Moon", "Mars-Phobos", "Mars-Deimos", "Jupiter-Io", "Jupiter-Europa", "Jupiter-Ganymede", "Jupiter-Callisto",
           "Saturn-Titan", "Saturn-Enceladus", "Saturn-Mimas", "Uranus-Ariel", "Uranus-Titania", "Uranus-Miranda",
           "neptune-Triton", "neptune-Nereid", "neptune-Naiad"],
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
plt.bar(df["행성 - 위성"], df["distance(km)"], color='skyblue')
plt.xlabel("행성 - 위성")
plt.ylabel("distnace(km)")
plt.title("satellite distance")
plt.xticks(rotation=45)


# Streamlit에 그래프 표시
st.pyplot(plt)
