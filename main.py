import streamlit as st

# 세션 상태에서 클릭 횟수 저장
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# 버튼 클릭 이벤트 처리
def increment_counter():
    st.session_state.click_count += 1

# 페이지 제목
st.title("Button Click Counter")

# 버튼 및 클릭 횟수 출력
if st.button("Click Me!", on_click=increment_counter):
    st.success("Button clicked!")

# 현재 클릭 횟수 표시
st.write(f"Button has been clicked **{st.session_state.click_count}** times.")
