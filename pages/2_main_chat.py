import streamlit as st
import json
from pathlib import Path

# 페이지 설정
st.set_page_config(
    page_title="EngageBot - Main Chat",
    page_icon="🤖",
    layout="wide"
)

# 데이터 저장 경로 설정
DATA_DIR = Path("data")
USER_PROFILE_PATH = DATA_DIR / "user_profiles.json"

def load_user_profile(user_id):
    with open(USER_PROFILE_PATH, "r", encoding="utf-8") as f:
        profiles = json.load(f)
        return profiles["users"].get(user_id)

def main():
    # 세션 상태 확인
    if "user_id" not in st.session_state or not st.session_state.user_id:
        st.switch_page("main.py")
        return

    # 사용자 프로필 로드
    user_profile = load_user_profile(st.session_state.user_id)
    if not user_profile:
        st.error("User profile not found. Please log in again.")
        st.switch_page("main.py")
        return

    # 사이드바 설정
    with st.sidebar:
        st.header("Chat Scenarios")
        st.markdown("---")
        
        # 시나리오 선택 버튼
        if st.button("Group Chat Time", key="sidebar_group_chat", use_container_width=True):
            st.switch_page("pages/3_group_chat.py")
        
        if st.button("Breaktime Chat", key="sidebar_break", use_container_width=True):
            st.switch_page("pages/4_breaktime_chat.py")
        
        st.markdown("---")
        if st.button("Logout", key="sidebar_logout", use_container_width=True):
            st.session_state.clear()
            st.switch_page("main.py")

    # 메인 채팅 영역
    st.title("🤖 EngageBot Chat")
    
    # 초기 환영 메시지
    with st.chat_message("assistant"):
        st.write(f"Welcome, {user_profile['id']}!")
    
    with st.chat_message("assistant"):
        st.write("I'm EngageBot, your friend powered by GPT.")
    
    with st.chat_message("assistant"):
        st.write("Where would you like to start?")
        
        # 시나리오 선택 버튼
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Group Chat Time", key="welcome_group_chat", use_container_width=True):
                st.switch_page("pages/3_group_chat.py")
        with col2:
            if st.button("Breaktime Chat", key="welcome_breaktime", use_container_width=True):
                st.switch_page("pages/4_breaktime_chat.py")

if __name__ == "__main__":
    main() 