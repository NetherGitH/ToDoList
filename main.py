import streamlit as st
import pyrebase

# Firebase 설정
firebase_config = {
    "apiKey": "YOUR_API_KEY",
    "authDomain": "YOUR_AUTH_DOMAIN",
    "databaseURL": "YOUR_DATABASE_URL",
    "projectId": "YOUR_PROJECT_ID",
    "storageBucket": "YOUR_STORAGE_BUCKET",
    "messagingSenderId": "YOUR_MESSAGING_SENDER_ID",
    "appId": "YOUR_APP_ID"
}

# Firebase 초기화
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# 할 일 추가 함수
def add_task():
    if st.session_state.new_task:
        new_task = {"task": st.session_state.new_task, "done": False}
        db.child("tasks").push(new_task)
        st.session_state.new_task = ""  # 입력 필드 초기화

# 할 일 완료 상태 업데이트 함수
def update_task(task_id, done_status):
    db.child("tasks").child(task_id).update({"done": done_status})

# 할 일 삭제 함수
def delete_task(task_id):
    db.child("tasks").child(task_id).remove()

# 페이지 제목
st.title("Shared To-Do List")

# 새로운 할 일 입력
st.text_input("Add a new task:", key="new_task", on_change=add_task)

# 실시간 할 일 목록 가져오기
tasks = db.child("tasks").get()

# 할 일 목록 표시
st.subheader("Your Shared Tasks")
if tasks.each():
    for task in tasks.each():
        task_id = task.key()
        task_data = task.val()

        col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
        with col1:
            checked = st.checkbox("", value=task_data["done"], key=f"task_{task_id}")
            update_task(task_id, checked)
        with col2:
            st.write(f"~~{task_data['task']}~~" if task_data["done"] else task_data["task"])
        with col3:
            if st.button("Delete", key=f"delete_{task_id}"):
                delete_task(task_id)
else:
    st.write("No tasks yet! Add a task above. 🎉")
