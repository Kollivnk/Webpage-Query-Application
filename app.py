import openai
import streamlit as st
import requests
from bs4 import BeautifulSoup
import os



#set the API key from the environment variable (more secure)
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        st.error(f"Error fetching the webpage: {e}")
        return None

def parse_webpage(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text()

def query_openai(document_text, user_query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{document_text}\n\n{user_query}"}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def main():
    st.title("Webpage Query Application")
    
    url = st.text_input("Enter the URL of the webpage:")
    
    if st.button("Fetch and Process"):
        if url:
            html_content = fetch_webpage(url)
            if html_content:
                document_text = parse_webpage(html_content)
                st.write("Webpage content fetched and processed.")
                st.session_state['document_text'] = document_text
        else:
            st.error("Please enter a valid URL.")
    
    if 'document_text' in st.session_state:
        user_query = st.text_input("Enter your query:")
        if st.button("Query Document"):
            response = query_openai(st.session_state['document_text'], user_query)
            st.write(response)

if __name__ == "__main__":
    main()
