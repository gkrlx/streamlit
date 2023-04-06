import streamlit as st



st.set_page_config(
    page_title="선택과목조사",
    page_icon="📖",
)

st.write("# 2학년 선택과목 선택")

number = st.number_input('반을 입력하십시오', step=1, min_value=1, max_value=9)
number = st.number_input('번호을 입력하십시오', step=1, min_value=1, max_value=29)

genre = st.radio(
    "과목을 선택하십시오",
    ('문학', '수학2'))

if genre == '수학2':
    options = st.multiselect(
        '과목을 선택하십시오(3개 선택)',
        ['물리', '화학', '생명과학', '지구과학', '과학탐구실험'], max_selections=3)
else:
    genre = st.multiselect(
        "과목을 선택하십시오(3개 선택)",
        ('윤리와 사상', '세계지리', '세계사', '동아시아사', '정치와 법', '생활과 윤리'))

genre = st.radio(
    "과목을 선택하십시오",
    ('일본어', '중국어'))

if st.button('제출'):
    st.write(" # ':red[처리가 완료되었습니다.]'")











