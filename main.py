import streamlit as st

st.markdown("""
<style>
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; } /*배경 애니메이션*/
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #8ec5fc, #e0c3fc, #a1c4fd, #c2e9fb);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
    color: white;
    transition: all 0.5s ease; /*배경화면*/
}

[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #8ec5fc, #e0c3fc, #a1c4fd, #c2e9fb);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
    color: #f8faff;
    transition: all 0.5s ease; /*왼쪽 사이드*/
}

.stApp h1 {
    color: #dbeafe;
    text-shadow: 2px 2px 5px #000;
    font-weight: 900; /*제목*/
}

div.stButton > button {
    background: linear-gradient(90deg, #89f7fe, #66a6ff);
    color: #1b2a4e;
    border-radius: 12px;
    height: 3em;
    width: 10em;
    font-weight: bold;
    border: none;
    box-shadow: 0px 0px 10px rgba(102,166,255,0.5);
    transition: all 0.3s ease; /*버튼*/
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #66a6ff, #89f7fe);
    box-shadow: 0px 0px 20px rgba(137,247,254,0.8);
    transform: scale(1.05); /*버튼 올렸을때*/
}
</style>
""", unsafe_allow_html=True)
st.title('태양계 행성들의 위성')

selected_planet = st.selectbox('행성을 선택해주세요:', [
    '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성'
])

planet_data = {
    '수성': {
        '특징': '태양에서 가장 가깝고 태양계에서 가장 작은 행성이다.',
        '대표적인_위성': '없다.',
    },
    '금성': {
        '특징': '지구와 유사한 크기이지만, 두꺼운 이산화탄소 대기와 그로 인한 극단적인 온실효과가 있다.',
        '대표적인_위성': '없다.',
    },
    '지구': {
        '특징': '생명체가 존재하며 대기가 질소와 산소로 구성되어 있다.',
        '대표적인_위성': '달',
        '위성_특징': {
            '달': {
                '설명': '지구에서 가장 가까운 천체이다.',
                '이미지': 'https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e001861/GSFC_20171208_Archive_e001861~thumb.jpg?as=webp'
            },
        },
    },
    '화성': {
        '특징': '매우 희박한 이산화탄소 대기, 낮은 중력, 물의 흔적이 있다.',
        '대표적인_위성': '포보스, 데이모스',
        '위성_특징': {
            '포보스': {
                '설명': '화성을 공전하고 있는 두 위성 중 가까이 있는 위성이다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA10367/PIA10367~medium.jpg'
            },
            '데이모스': {
                '설명': '화성의 두 번째 위성으로, 포보스보다 작고 더 멀리 위치해 있으며, 미국의 천문학자인 아사프 홀이 발견했다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA11826/PIA11826~thumb.jpg?as=webp'
            },
        },
    },
    '목성': {
        '특징': '태양계에서 가장 큰 거대 가스 행성으로, 강력한 자기장과 빠른 자전, 거대한 폭풍 대적점이 특징이다.',
        '대표적인_위성': '이오, 유로파, 가니메데, 칼리스토',
        '위성_특징': {
            '이오': {
                '설명': '평균 반지름이 약 1,800km로 달과 비슷한 크기이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Io_highest_resolution_true_color.jpg'
            },
            '유로파': {
                '설명': '표면 아래 거대한 지하 바다가 존재할 가능성이 높아 생명체 후보지로 주목받는다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA09246/PIA09246~thumb.jpg?as=webp'
            },
            '가니메데': {
                '설명': '반지름 2,634km로 태양계에서 가장 큰 위성이다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA00706/PIA00706~thumb.jpg?as=webp'
            },
            '칼리스토': {
                '설명': '태양계에서 세 번째로 큰 위성으로, 표면 충돌구가 많다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA03456/PIA03456~thumb.jpg?as=webp'
            },
        },
    },
    '토성': {
        '특징': '거대한 고리와 많은 위성을 가진 행성이다.',
        '대표적인_위성': '타이탄, 엔셀라두스, 미마스',
        '위성_특징': {
            '타이탄': {
                '설명': '토성의 가장 큰 위성으로, 소형 천체망원경으로 관찰할 수 있다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA08736/PIA08736~thumb.jpg?as=webp'
            },
            '엔셀라두스': {
                '설명': '지름이 504km밖에 되지 않은 매우 작은 위성으로, 얼음 기둥이 분출되는 현상이 있다.',
                '이미지': 'https://images-assets.nasa.gov/image/JPL-2015_10_28-PIA17202/JPL-2015_10_28-PIA17202~thumb.jpg?as=webp'
            },
            '미마스': {
                '설명': '토성의 7번째로 큰 자연 위성으로, 표면의 거대한 충돌구가 특징이다.',
                '이미지': 'https://upload.wikimedia.org/wikipedia/commons/b/bc/Mimas_Cassini.jpg'
            },
        },
    },
    '천왕성': {
        '특징': '푸른색을 띠는 가스 행성으로, 자전축이 거의 옆으로 누워있다.',
        '대표적인_위성': '아리엘, 티타니아, 미란다',
        '위성_특징': {
            '아리엘': {
                '설명': '천왕성의 위성 중에 가장 반사율이 높다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA01534/PIA01534~medium.jpg'
            },
            '티타니아': {
                '설명': '천왕성의 위성들 중 가장 크다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA00036/PIA00036~thumb.jpg?as=webp'
            },
            '미란다': {
                '설명': '천왕성의 둥근 다섯 개의 위성 중 가장 작고 가장 안쪽에 위치한다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA02217/PIA02217~thumb.jpg?as=webp'
            },
        },
    },
    '해왕성': {
        '특징': '푸른색을 띠는 가스 행성으로, 강력한 바람과 폭풍이 특징이다.',
        '대표적인_위성': '트리톤, 나이아드, 탈라사',
        '위성_특징': {
            '트리톤': {
                '설명': '해왕성의 가장 큰 위성으로, 역행 공전을 한다.',
                '이미지': 'https://images-assets.nasa.gov/image/PIA01536/PIA01536~medium.jpg'
            },
            '나이아드': {
                '설명': '해왕성에 가까운 궤도를 가진 작은 위성이다.',
                '이미지': 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAzMjFfMjA3%2FMDAxNjE2MjcyMjY3Mzc3.GcVCyEpuBOjmL5MYKMx7nhQO6PRPLOZw69Xq82sWNHMg.q-XXl9uFfxqt4wo3PBV00gcN_slPFe8PrVjUpWI7-P4g.JPEG.efremov%2F6582ca2b0be9989efeb08938850dd031.jpg&type=sc960_832'
            },
            '탈라사': {
                '설명': '불규칙한 모양이며, 위성들의 파편이 뭉쳐 만들어졌을 가능성이 있다.',
                '이미지': 'https://i.namu.wiki/i/nzlHwp7k7Ks4XuEcCgihOdyPtuacC_UZDWC8R96r6_BNvCiNkr9011uJENiXD32SxKPKcX1mt4SN_bi1_vdPjGb2Ut6UZUd_inSDH_VMRvpwMf01WHzuniHC2QGHjHPlkDDUzmoYkB5U-6t_JKdVkA.webp'
            },
        },
    },
}

if st.button('특징 보기'):
    if selected_planet in planet_data:
        특징 = planet_data[selected_planet].get('특징', '정보 없음')
        대표적인_위성 = planet_data[selected_planet].get('대표적인_위성', '정보 없음')
        위성_특징 = planet_data[selected_planet].get('위성_특징', None)

        st.subheader(f"{selected_planet}")
        st.write(f"**특징**: {특징}")
        st.write(f"**대표적인 위성**: {대표적인_위성}")

        if isinstance(위성_특징, dict):
            for 위성, 정보 in 위성_특징.items():
                st.markdown(f"### {위성}")
                st.write(정보['설명'])
                st.image(정보['이미지'], use_container_width=True)
        else:
            st.write("위성 관련 상세 정보가 없습니다.")
    else:
        st.error(f"{selected_planet}에 대한 정보가 없습니다.")
