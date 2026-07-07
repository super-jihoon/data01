import streamlit as st

# 페이지 제목 설정
st.set_page_config(page_title="여행 취향 분석기", page_icon="✈️")

st.title("✈️ 나의 여행 취향 분석기: Explorer's Compass")
st.write("당신의 여행 스타일을 입력하면 최적의 여행 테마를 분석해 드립니다.")

st.markdown("---")

# 1. 여행 기간 (슬라이더: 1일~10일)
st.subheader("1. 여행의 호흡")
duration = st.slider("원하는 여행 기간을 선택해주세요 (일 단위)", min_value=1, max_value=10, value=5)
st.write(f"🗓️ 선택된 기간: **{duration}일**")

# 2. 여행 종류 (드롭다운: 국내/해외)
st.subheader("2. 공간의 확장")
travel_type = st.selectbox("어디로 떠나고 싶으신가요?", ["국내여행", "해외여행"])

# 3. 선호 국가 및 도시 (텍스트 입력)
st.subheader("3. 상세 목적지")
col1, col2 = st.columns(2)

with col1:
    country = st.text_input("가고 싶은 국가를 적어주세요", placeholder="예: 일본, 프랑스, 대한민국")
with col2:
    city = st.text_input("방문하고 싶은 도시명을 적어주세요", placeholder="예: 도쿄, 파리, 부산")

st.markdown("---")

# 분석 결과 버튼
if st.button("🔮 나의 여행 취향 결과 분석하기"):
    if country and city:
        st.balloons()
        st.success(f"분석이 완료되었습니다, {travel_type} 전문가님!")
        
        # 결과 요약
        st.info(f"**{country} {city}**에서 즐기는 **{duration}일**간의 멋진 여행이 예상됩니다.")
        
        # 간단한 분석 멘트
        if duration <= 3:
            st.write("📍 짧고 굵은 **'에너지 충전형'** 여행을 선호하시네요!")
        elif 4 <= duration <= 7:
            st.write("📍 현지의 매력을 충분히 느끼는 **'심층 탐방형'** 여행이 어울립니다.")
        else:
            st.write("📍 일상을 완전히 잊게 해주는 **'완전 몰입형'** 여행을 계획 중이시군요!")
    else:
        st.warning("국가와 도시명을 모두 입력해 주세요!")
