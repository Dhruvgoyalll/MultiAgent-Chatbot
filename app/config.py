import streamlit as st

# Access API keys from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

# Now you can use these keys in your application
st.write(GROQ_API_KEY)
