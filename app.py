import streamlit as st
from openai import OpenAI
import google.generativeai as genai
from apikey import google_gemini_api_key, openai_api_key


client = OpenAI(api_key=openai_api_key)

# Configure the API key
genai.configure(api_key=google_gemini_api_key)

# Set app to wide mode
st.set_page_config(layout='wide')

# Title of the app
st.title("BlogCraft: Your AI Writing Companion")

# Subheader for the app
st.subheader("Now you can craft perfect blogs with the help of AI-BlogCraft, your new AI Blog Companion")

# Sidebar for user input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog You Want to Generate")

    # Blog title
    blog_title = st.text_input("Blog Title")

    # Keywords input
    keywords_input = st.text_area("Keywords (Comma Separated)")

    # Number of words
    num_words = st.slider("Number of Words", min_value=250, max_value=1000, step=250)

    # Number of images
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

    # Generate Blog
    gen_blog = st.button("Generate Blog")

# Define the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Generate blog content when the button is clicked
if gen_blog:
    # Generate images using DALL-E if requested
   for i in range(int(num_images)):
    try:
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=f"{blog_title} - illustration {i+1}",
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Extract image URL and display
        image_url = image_response['data'][0]['url']
        st.image(image_url, caption=f"Image {i+1}")

    except Exception as e:
        # Handle billing or other errors
        if 'billing_hard_limit_reached' in str(e):
            st.error("Billing limit reached. Unable to generate images.")
        else:
            st.error("An error occurred while generating images.")

    if blog_title and keywords_input:
        # Initialize the model and chat session
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
        )

        chat_session = model.start_chat(history=[])

        # Prepare prompt
        input_text = f"Generate a blog titled '{blog_title}' with the following keywords: {keywords_input}. The blog should be approximately {num_words} words."

        # Send message and get response
        text_response = chat_session.send_message(input_text)

        # Display the generated blog
        st.write(text_response.text)
    else:
        st.warning("Please enter both a blog title and keywords to generate a blog.")
