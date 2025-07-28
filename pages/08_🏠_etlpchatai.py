import streamlit as st
import requests
import json
import base64
from datetime import datetime

# Set the page configuration
st.set_page_config(page_title="ETLP Chat AI", page_icon="🤖", layout="wide")

# Background image URL
background_image_url = "https://raw.githubusercontent.com/Natsnet/WS_Back_img/main/WonderScribe_bk_blue_page_1.jpg"

background_css = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{background_image_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: #f0f4ff;
}}

.custom-box {{
    background-color: rgba(255, 255, 255, 0.8);
    border-radius: 10px;
    padding: 20px;
    margin: 20px auto;
    max-width: 800px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    font-family: Arial, sans-serif;
    color: #5481c4;
    line-height: 1.6;
}}

.chat-container {{
    max-height: 500px;
    overflow-y: auto;
    padding: 15px;
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
}}

.user-message {{
    background-color: #e3f2fd;
    padding: 10px;
    border-radius: 10px;
    margin: 10px 0;
    border-left: 4px solid #2196f3;
}}

.bot-message {{
    background-color: #f1f8e9;
    padding: 10px;
    border-radius: 10px;
    margin: 10px 0;
    border-left: 4px solid #4caf50;
}}

.timestamp {{
    font-size: 0.8em;
    color: #666;
    text-align: right;
}}

/* Sidebar customization */
[data-testid="stSidebar"] {{
    background-color: #f0f4ff;
    color: #5481c4;
    font-family: Arial, sans-serif;
    font-size: 18px;
}}
[data-testid="stSidebar"] * {{
    color: #5481c4;
}}
[data-testid="stSidebar"] .stMarkdown {{
    text-align: center;
}}
</style>
"""

# Apply CSS styles
st.markdown(background_css, unsafe_allow_html=True)

# Function to add the logo to the top of the sidebar
def add_logo_to_sidebar_top(logo_path, width="250px"):
    with open(logo_path, "rb") as f:
        encoded_logo = base64.b64encode(f.read()).decode("utf-8")
    st.sidebar.markdown(
        f"""
        <style>
            [data-testid="stSidebar"]::before {{
                content: '';
                display: block;
                background-image: url("data:image/png;base64,{encoded_logo}");
                background-size: contain;
                background-repeat: no-repeat;
                background-position: top center;
                height: 250px;
                padding-top: 20px;
                margin-bottom: 20px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Add the WonderScribe logo to the top of the sidebar
add_logo_to_sidebar_top("pages/images/Updated_WonderS_logo.png", width="250px")

def query_knowledge_base(user_question):
# Function to query the knowledge base using existing lambda infrastructure
    """
    Use existing getStory endpoint to query knowledge base - no lambda changes needed!
    """
    try:
        AWS_API_URL = "https://wacnqhon34.execute-api.us-east-1.amazonaws.com/dev/"
        headers = {"Content-Type": "application/json"}
        
        # Use the existing getStory endpoint but with Q&A focused parameters
        payload = {
            "character_type": "Human-Centric Stories",
            "age": "25",
            "height": "normal",
            "hair_color": "brown",
            "eye_color": "brown",
            "audience": "Adult",
            "story_type": "informational",
            "main_character": "Assistant",
            "story_theme": user_question,  # This becomes the knowledge base query
            "moral_lesson": "provide accurate information",
            "setting": "question and answer context",
            "word_count": "300",
            "story_lang": "English",
            "api_Path": "getStory"
        }
        
        response = requests.post(AWS_API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            story_texts = data.get("story_texts", [])
            
            if story_texts:
                # Combine all story parts and clean up for chatbot response
                full_response = " ".join(story_texts)
                
                # Clean up the response to be more chatbot-like
                cleaned_response = clean_story_response(full_response, user_question)
                return cleaned_response
            else:
                return "Sorry, I couldn't find relevant information to answer your question."
        else:
            return f"I'm having trouble accessing the information right now. Please try again later. (Status: {response.status_code})"
            
    except Exception as e:
        return f"I encountered an error while searching for information: {str(e)}"

def clean_story_response(story_text, original_question):
    """
    Clean up the story response to make it more suitable for a chatbot
    """
    try:
        # Remove obvious story elements and make it more conversational
        cleaned = story_text
        
        # Remove common story beginnings
        story_starters = [
            "Once upon a time", "In the", "There lived", "In a", "Long ago",
            "It was", "One day", "Assistant was", "The Assistant"
        ]
        
        for starter in story_starters:
            if cleaned.startswith(starter):
                # Find the first sentence end and start from there
                first_period = cleaned.find('. ')
                if first_period > 0:
                    cleaned = cleaned[first_period + 2:]
                break
        
        # Replace character names with more appropriate terms
        cleaned = cleaned.replace("Assistant", "the information")
        cleaned = cleaned.replace("The Assistant", "The information")
        
        # Make it more direct and Q&A focused
        sentences = cleaned.split('. ')
        
        # Try to find the most relevant sentences that directly answer the question
        relevant_sentences = []
        question_keywords = set(original_question.lower().split())
        
        for sentence in sentences:
            sentence_words = set(sentence.lower().split())
            # Check if sentence has good overlap with question keywords
            overlap = len(question_keywords.intersection(sentence_words))
            if overlap > 0 or len(sentence.strip()) > 20:  # Keep substantial sentences
                relevant_sentences.append(sentence.strip())
        
        if relevant_sentences:
            # Take the first few most relevant sentences
            result = '. '.join(relevant_sentences[:3])
            if not result.endswith('.'):
                result += '.'
            return result
        else:
            # Fallback to first part of original response
            return '. '.join(sentences[:2]) + '.'
            
    except Exception:
        # If cleaning fails, return original but truncated
        return story_text[:500] + "..." if len(story_text) > 500 else story_text

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

def add_to_chat_history(user_msg, bot_msg):
    """Add messages to chat history with timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.chat_history.append({
        "user": user_msg,
        "bot": bot_msg,
        "timestamp": timestamp
    })

def clear_chat_history():
    """Clear the chat history"""
    st.session_state.chat_history = []
    st.session_state.user_input = ""

def main():
    # Header
    st.markdown("<h1 style='text-align: center; color: #5481c4;'>🤖 ETLP Chat AI Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #5481c4;'>Ask me anything! I'll search through our knowledge base to help you.</p>", unsafe_allow_html=True)
    
    # Sidebar with chat controls
    st.sidebar.markdown("### Chat Controls")
    if st.sidebar.button("🗑️ Clear Chat History"):
        clear_chat_history()
        st.rerun()
    
    st.sidebar.markdown("### Tips")
    st.sidebar.markdown("""
    - Ask specific questions for better results
    - I can help with information from our knowledge base
    - Try rephrasing if you don't get the expected answer
    """)
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown("### Chat History")
        chat_container = st.container()
        
        with chat_container:
            for chat in st.session_state.chat_history:
                # User message
                st.markdown(f"""
                <div class="user-message">
                    <strong>You:</strong> {chat['user']}
                    <div class="timestamp">{chat['timestamp']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Bot message
                st.markdown(f"""
                <div class="bot-message">
                    <strong>AI Assistant:</strong> {chat['bot']}
                    <div class="timestamp">{chat['timestamp']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Input form
    st.markdown("### Ask a Question")
    with st.form("chat_form", clear_on_submit=True):
        user_question = st.text_area(
            "Your Question:",
            placeholder="Ask me anything about our knowledge base...",
            height=100,
            key="question_input"
        )
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submitted = st.form_submit_button("🚀 Send Question", use_container_width=True)
    
    # Process the question when submitted
    if submitted and user_question.strip():
        # Show loading spinner
        with st.spinner("🔍 Searching knowledge base..."):
            # Get response from knowledge base using existing lambda
            bot_response = query_knowledge_base(user_question.strip())
        
        # Add to chat history
        add_to_chat_history(user_question.strip(), bot_response)
        
        # Rerun to update the display
        st.rerun()
    
    elif submitted and not user_question.strip():
        st.warning("Please enter a question before submitting.")
    
    # Sample questions
    st.markdown("### Sample Questions")
    sample_questions = [
        "What is ETLP?",
        "What is Exercise #1 about?"
    ]
    
    cols = st.columns(len(sample_questions))
    for i, question in enumerate(sample_questions):
        with cols[i]:
            if st.button(f"💡 {question}", key=f"sample_{i}"):
                # Simulate form submission with sample question
                with st.spinner("🔍 Searching knowledge base..."):
                    bot_response = query_knowledge_base(question)
                add_to_chat_history(question, bot_response)
                st.rerun()

if __name__ == "__main__":
    main()