# AI Blog Generator (BlogCraft)

## Overview

AI Blog Generator (BlogCraft) is a **Streamlit-based web application** that helps users create high-quality blog content using **OpenAI's GPT model (DALL·E for images)** and **Google's Gemini model**. Users can input a blog title, relevant keywords, and word count to generate a well-structured blog with AI-generated images.

## Features

- **AI-Powered Blog Writing**: Generates blog content based on title and keywords.
- **Image Generation**: Uses OpenAI’s DALL·E to generate relevant images for the blog.
- **Customizable Word Limit**: Users can specify the desired length of the blog (250-1000 words).
- **User-Friendly Interface**: Built with Streamlit for easy interaction.

## Installation

### Prerequisites

Ensure you have **Python 3.8+** installed and the following dependencies:

```sh
pip install streamlit openai google-generativeai
```

### Clone the Repository

```sh
git clone https://github.com/suryansh2004/AI_Blog_Comapanian
cd AI_Blog_Companian
```

### Set Up API Keys

Create an `apikey.py` file in the root directory and add your API keys:

```python
# apikey.py
google_gemini_api_key = "your-google-gemini-api-key"
openai_api_key = "your-openai-api-key"
```

Replace `your-google-gemini-api-key` and `your-openai-api-key` with your actual API keys.

## Running the Application

Run the Streamlit app with:

```sh
streamlit run app.py
```

## Usage

1. Enter a **Blog Title**.
2. Provide **Keywords** (comma-separated).
3. Set the **Word Count**.
4. Choose the **Number of Images**.
5. Click **Generate Blog**.
6. View the AI-generated blog with images.

## Technologies Used

- **Python**
- **Streamlit** (for UI)
- **OpenAI API** (for text and image generation)
- **Google Gemini API** (for blog content generation)

## Possible Issues & Fixes

1. **Invalid API Key**: Check if API keys in `apikey.py` are correct.
2. **Billing Limit Reached**: Ensure your OpenAI and Google accounts have enough quota.
3. **ModuleNotFoundError**: Run `pip install -r requirements.txt` to install dependencies.

## Contributing

Pull requests are welcome! Feel free to fork the repository and submit enhancements.
