import streamlit as st
import json
from pathlib import Path
import os

# 페이지 설정
st.set_page_config(
    page_title="Sign In",
    page_icon="🤖"
)

# 데이터 저장 경로 설정
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
USER_PROFILE_PATH = DATA_DIR / "user_profiles.json"

# 사용자 프로필 데이터 구조
def init_user_profiles():
    if not USER_PROFILE_PATH.exists():
        with open(USER_PROFILE_PATH, "w", encoding="utf-8") as f:
            json.dump({"users": {}}, f, ensure_ascii=False, indent=4)

def load_user_profiles():
    if USER_PROFILE_PATH.exists():
        with open(USER_PROFILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"users": {}}

def save_user_profile(user_id, profile_data):
    profiles = load_user_profiles()
    profiles["users"][user_id] = profile_data
    with open(USER_PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profiles, f, ensure_ascii=False, indent=4)

def authenticate_user(username, password):
    profiles = load_user_profiles()
    if username in profiles["users"]:
        if profiles["users"][username]["pw"] == password:
            return True
    return False

# 메인 페이지
def main():
    st.title("🤖 Welcome to EngageBot")
    st.markdown("""
    EngageBot is an AI chatbot designed to support international students in learning English and fostering social interaction.
    """)

    # 로그인 폼
    with st.form("login_form"):
        st.header("Login")
        username = st.text_input("ID")
        password = st.text_input("Password", type="password")
        
        col1, col2 = st.columns(2)
        with col1:
            login_submitted = st.form_submit_button("Login")
        with col2:
            if st.form_submit_button("Sign Up"):
                st.switch_page("pages/1_sign_up.py")

        if login_submitted:
            if not username or not password:
                st.error("Please enter both username and password.")
            elif authenticate_user(username, password):
                st.session_state.user_id = username
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.switch_page("pages/2_main_chat.py")
            else:
                st.error("Invalid username or password.\n\nIf you don't have an account, please sign up.")

# 앱 실행
if __name__ == "__main__":
    init_user_profiles()
    main() 