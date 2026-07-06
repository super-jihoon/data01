import streamlit as st

st.header('드롭다운')

option = st.selectbox(
     '선호하는 여행 장소는 어디인가요?',
     ('국내 여행', '해외 여행'))

st.write('당신이 선호하는 여행 장소는? ', option)
