# 추가 1: langchain과 dotenv 모듈 임포트
import streamlit as st
import json
from pathlib import Path
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
import random
load_dotenv()

import streamlit as st
from langchain_core.messages.chat import ChatMessage

# 페이지 설정
st.set_page_config(
    page_title="EngageBot - Group Chat",
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

# 중요 ★: Breaktime Chat Engine > Scenario Starter Chain
def create_initial_chain(user_profile):
    # 랜덤한 상황 설정
    scenarios = [
        "Cafeteria at Lunchtime",
        "School Hallway",
        "On the Way to and from School",
        "P.E. Class",
        "Library",
        "Classroom",
        "School Playground",
        "Cafe Near School"
    ]
    selected_scenario = random.choice(scenarios)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a friendly student who is similar to the user:
        - Age: {user_profile['age']}
        - Language Level: {user_profile['language_level']}
        
        You are currently at: {selected_scenario}
        
        Your role is to:
        1. Act like a student of similar age and language level
        2. Start a natural conversation based on the current situation
        3. Keep the conversation engaging and friendly
        4. Ask questions that would be natural for students to discuss
        5. Be supportive and encouraging
        6. At the end of the conversation, please add a suitable emoji that matches the tone of the chat."""),
        ("human", "Let's start a conversation!")
    ])
    
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    output_parser = StrOutputParser()
    return prompt | llm | output_parser

# 중요 ★: Breaktime Chat Engine > Personalized Casual Chat Chain
def create_conversation_chain(user_profile):
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a friendly student who is similar to the user:
        - Age: {user_profile['age']}
        - Nationality: {user_profile['nationality']}
        - Language Level: {user_profile['language_level']}
        
        Your role is to:
        1. Respond in a way appropriate for the student's age and language level
        2. Keep the conversation engaging and natural
        3. Ask follow-up questions to encourage discussion
        4. Provide gentle corrections if needed
        5. Be supportive and encouraging
        6. At the end of the conversation, please add a suitable emoji that matches the tone of the chat."""),
        ("human", "{question}")
    ])
    
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.7)
    output_parser = StrOutputParser()
    return prompt | llm | output_parser

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
        
        if st.button("Group Chat Time", key="sidebar_group_chat", use_container_width=True):
            # # 그룹 채팅으로 이동 시 breaktime 채팅 세션 초기화
            # if "messages_breaktime_chat" in st.session_state:
            #     del st.session_state.messages_breaktime_chat
            st.switch_page("pages/3_group_chat.py")
        if st.button("Breaktime Chat", key="welcome_breaktime", use_container_width=True):
            st.switch_page("pages/4_breaktime_chat.py")
        st.markdown("---")
        if st.button("Logout", key="sidebar_logout", use_container_width=True):
            st.session_state.clear()
            st.switch_page("main.py")

    # 메인 채팅 영역
    st.title("🤖 Breaktime Chat!")

    # 초기 메시지 설정
    if "messages_breaktime_chat" not in st.session_state:
        st.session_state.messages_breaktime_chat = []
        
        # 초기 대화 시작
        initial_chain = create_initial_chain(user_profile)
        initial_response = initial_chain.invoke({"question": "Let's start a conversation!"})
        st.session_state.messages_breaktime_chat.append({
            "role": "assistant",
            "content": initial_response
        })

    # 채팅 메시지 표시
    for message in st.session_state.messages_breaktime_chat:
        st.chat_message(message["role"]).write(message["content"])

    # 사용자 입력 처리
    if prompt := st.chat_input("Type your thoughts here..."):
        # 사용자 입력 메시지 표시
        st.chat_message("user").write(prompt)

        # 사용자 메시지 추가
        st.session_state.messages_breaktime_chat.append({"role": "human", "content": prompt})
        
        # AI 응답 생성
        conversation_chain = create_conversation_chain(user_profile)
        
        # 대화 컨텍스트 구성
        context = {
            "question": f"""Previous conversation: {st.session_state.messages_breaktime_chat[-4:]}
User's response: {prompt}
Please respond naturally and continue the conversation in a way that would be natural for students of similar age and language level."""
        }
        
        response = conversation_chain.invoke(context)
        
        # AI 응답 추가
        st.session_state.messages_breaktime_chat.append({"role": "assistant", "content": response})
        st.rerun()

if __name__ == "__main__":
    main()
