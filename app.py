# ============================================================
# 🌦️ AGENTIC AI WEATHER ASSISTANT
# Streamlit + LangChain + Groq + wttr.in
# ============================================================

import streamlit as st
import requests

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain.tools import tool


# ============================================================
# 1. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Weather Assistant",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 2. CUSTOM CSS
# ============================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eaf4ff, #f7faff);
}
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: #123b70;
}
.subtitle {
    text-align: center;
    font-size: 17px;
    color: #526b87;
    margin-bottom: 25px;
}
[data-testid="stChatMessage"] {
    background-color: white;
    border-radius: 14px;
    padding: 15px;
    border: 1px solid #dce8f5;
}
div.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 3. HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🌦️ AI Weather Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your intelligent assistant for real-time weather information'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 4. WEATHER TOOL
# ============================================================

@tool
def get_weather(city: str) -> str:
    """
    Get current weather conditions for a city.
    Input should be a city name, such as Bengaluru, Mumbai, or London.
    Returns temperature, feels-like temperature, humidity, wind speed,
    and weather description.
    """
    try:
        city = city.strip()

        if not city:
            return "Please provide a valid city name."

        url = f"https://wttr.in/{city}"
        params = {"format": "j1"}

        response = requests.get(
            url,
            params=params,
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]

        area = data.get("nearest_area", [{}])[0]
        area_name = area.get("areaName", [{}])[0].get("value", city)
        country = area.get("country", [{}])[0].get("value", "")

        description = current.get(
            "weatherDesc", [{}]
        )[0].get("value", "Not available")

        result = {
            "City": area_name,
            "Country": country,
            "Temperature (C)": current.get("temp_C"),
            "Feels Like (C)": current.get("FeelsLikeC"),
            "Weather": description,
            "Humidity (%)": current.get("humidity"),
            "Wind Speed (km/h)": current.get("windspeedKmph"),
            "Wind Direction": current.get("winddir16Point"),
            "Visibility (km)": current.get("visibility"),
            "UV Index": current.get("uvIndex")
        }

        return str(result)

    except requests.exceptions.Timeout:
        return "Weather service timed out. Please try again."

    except requests.exceptions.RequestException as e:
        return f"Unable to connect to the weather service: {e}"

    except (KeyError, IndexError, ValueError) as e:
        return f"Could not process weather data: {e}"


# ============================================================
# 5. CREATE AGENT
# ============================================================

@st.cache_resource
def create_weather_agent(api_key: str):
    """Create and cache the weather agent for the given API key."""

    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        api_key=api_key,
        temperature=0
    )

    agent = create_agent(
        model=llm,
        tools=[get_weather],
        system_prompt=(
            "You are a helpful AI Weather Assistant. "
            "Use the get_weather tool whenever the user asks about "
            "current weather conditions in a city. "
            "Provide clear, friendly, easy-to-understand answers. "
            "Include temperature, feels-like temperature, weather "
            "description, humidity, and wind speed when available. "
            "Do not invent weather data. If the tool fails, explain "
            "that current weather information could not be retrieved."
        )
    )

    return agent


# ============================================================
# 6. SIDEBAR
# ============================================================

with st.sidebar:
    st.title("⚙️ Settings")

    st.markdown("### 🔑 Groq API Key")

    # Read secrets only if the file exists.
    try:
        saved_key = st.secrets.get("GROQ_API_KEY", "")
    except (FileNotFoundError, RuntimeError):
        saved_key = ""

    api_key = st.text_input(
        "Enter your Groq API key",
        value=saved_key,
        type="password",
        placeholder="gsk_...",
        help="Your API key is used to connect to the Groq model."
    )

    st.markdown("---")

    st.markdown("### 💡 Example Questions")
    st.markdown("""
    - What is the weather in Bengaluru?
    - Tell me the current weather in Mumbai.
    - Is it hot in Delhi today?
    - Compare the weather in London and Paris.
    """)

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("🌦️ Powered by LangChain, Groq, and wttr.in")


# ============================================================
# 7. SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# 8. WELCOME MESSAGE
# ============================================================

st.info(
    "👋 Hello! I'm your AI Weather Assistant. "
    "Ask me about the current weather in any city."
)


# ============================================================
# 9. DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# 10. CHAT INPUT AND AGENT RESPONSE
# ============================================================

user_input = st.chat_input(
    "Ask about the weather in a city..."
)

if user_input:

    if not api_key.strip():
        st.warning(
            "🔑 Please enter your Groq API key in the sidebar first."
        )
        st.stop()

    # Add user message to chat history.
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message.
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate agent response.
    with st.chat_message("assistant"):
        with st.spinner("🌤️ Checking weather and preparing response..."):

            try:
                agent = create_weather_agent(api_key.strip())

                response = agent.invoke({
                    "messages": st.session_state.messages
                })

                answer = response["messages"][-1].content

                if isinstance(answer, list):
                    answer = "\n".join(
                        str(part.get("text", part))
                        if isinstance(part, dict)
                        else str(part)
                        for part in answer
                    )

                st.markdown(answer)

                # Save assistant response.
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(
                    "❌ Something went wrong while generating "
                    "the response."
                )
                st.exception(e)

