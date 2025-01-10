import streamlit as st

# 세션 상태에서 할 일 목록 저장
if "todo_list" not in st.session_state:
    st.session_state.todo_list = []

# 할 일 추가 함수
def add_task():
    if st.session_state.new_task:
        st.session_state.todo_list.append({"task": st.session_state.new_task, "done": False})
        st.session_state.new_task = ""  # 입력 필드 초기화

# 페이지 제목
st.title("To-Do List")

# 새로운 할 일 입력
st.text_input("Add a new task:", key="new_task", on_change=add_task)

# 할 일 목록 표시
st.subheader("Your Tasks")
if st.session_state.todo_list:
    for i, item in enumerate(st.session_state.todo_list):
        col1, col2 = st.columns([0.1, 0.9])
        # 체크박스 업데이트
        with col1:
            checked = st.checkbox("", value=item["done"], key=f"task_{i}")
            st.session_state.todo_list[i]["done"] = checked
        # 할 일 텍스트 표시
        with col2:
            st.write(f"~~{item['task']}~~" if item["done"] else item["task"])
else:
    st.write("No tasks yet! Add a task above. 🎉")
