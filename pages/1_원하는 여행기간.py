# 1. 여행 기간 슬라이더
travel_days = st.slider(
    "1. 원하는 여행 기간을 선택해주세요 (일)",
    min_value=0,
    max_value=10,
    value=3,  # 기본값
    step=1
)

# 사용자가 선택한 기간을 화면에 실시간으로 보여줍니다.
st.write(f"선택하신 여행 기간: **{travel_days}일**")
