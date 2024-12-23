import streamlit as st
from main import chatbot_response

# CSS for both dark and light modes
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff;
    }

    /* Dark Mode Styles */
    body[data-theme="dark"] {
        background-color: #333333;
        color: #ffffff;
    }
    
    /* Light Mode Styles */
    body[data-theme="light"] {
        background-color: #f0f8ff;
        color: #000000;
    }

    .title {
        font-size: 32px;
        font-family: 'Arial', sans-serif;
        text-align: center;
        padding: 20px;
    }

    /* Bot response styling */
    .bot-response {
        color: #4CAF50;
        font-weight: bold;
    }

    /* User input styling */
    .user-input {
        color: #007bff;
        font-weight: bold;
    }

    /* Dark Mode Color Adjustments */
    body[data-theme="dark"] .bot-response {
        color: #81C784; /* lighter green for dark mode */
    }
    body[data-theme="dark"] .user-input {
        color: #64B5F6; /* lighter blue for dark mode */
    }
    </style>
    """, unsafe_allow_html=True
)

# Title of the app with custom style
st.markdown('<h1 class="title">Fiqih - Solusi Ibadah</h1>', unsafe_allow_html=True)

# Add an image (if you have one) for visual appeal
st.image("https://your-image-url.com/image.jpg", use_container_width=True)  # Updated here

# User input field
user_input = st.text_input("Anda:", "")

# When the user presses the 'Kirim' button
if st.button("Kirim"):
    if user_input:
        # Get the chatbot's response
        response = chatbot_response(user_input)
        
        # Display the user's input and bot's response in different colors
        st.markdown(f"<p class='user-input'>Anda: {user_input}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='bot-response'>Bot: {response}</p>", unsafe_allow_html=True)
    else:
        # If user input is empty, prompt for input
        st.warning("Mohon masukkan pertanyaan atau pernyataan Anda.")
