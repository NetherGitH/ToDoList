import streamlit as st
from github import Github

# GitHub Personal Access Token 입력
GITHUB_TOKEN = "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"
REPO_NAME = "NetherGitH/ToDoList"  # 예: "username/repo-name"

# GitHub 연결
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# 할 일 추가 함수
def add_task():
    if st.session_state.new_task:
        repo.create_issue(title=st.session_state.new_task)
        st.session_state.new_task = ""  # 입력 필드 초기화

# 할 일 삭제 함수
def close_task(issue_number):
    issue = repo.get_issue(number=issue_number)
    issue.edit(state="closed")

# Streamlit UI
st.title("GitHub To-Do List")

# 새로운 할 일 입력
st.text_input("Add a new task:", key="new_task", on_change=add_task)

# GitHub Issues 가져오기
st.subheader("Your Shared Tasks")
issues = repo.get_issues(state="open")
if issues.totalCount > 0:
    for issue in issues:
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.write(f"- {issue.title}")
        with col2:
            if st.button("Mark as Done", key=f"done_{issue.number}"):
                close_task(issue.number)
else:
    st.write("No tasks yet! Add a task above. 🎉")
