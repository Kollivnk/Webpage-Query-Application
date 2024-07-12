# Webpage Query Application

This application allows users to fetch content from a webpage, process it, and query the content using OpenAI's GPT-3.5-turbo model. Built with Streamlit, it provides an interactive interface for users to input a URL and ask questions about the webpage content.

## Features

- Fetch content from any webpage.
- Process and extract text content using BeautifulSoup.
- Query the extracted content using OpenAI's GPT-3.5-turbo model.
- Interactive web interface built with Streamlit.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/webpage-query-app.git
    cd webpage-query-app
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\\Scripts\\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up OpenAI API key:
    You can set your OpenAI API key in the environment variables for better security. Create a `.env` file and add your key:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Use the application:
    - Enter the URL of the webpage you want to fetch.
    - Click on "Fetch and Process" to retrieve and process the webpage content.
    - Enter your query in the provided input box.
    - Click on "Query Document" to get the response from the GPT-3.5-turbo model based on the webpage content.

## Project Context

This application is part of a Langchain-based AI project that takes a webpage as a document and allows users to query content within the webpage using OpenAI. The project includes several components such as web scraping, natural language processing, and interactive web applications. For more information, visit the project repository on [GitHub](https://github.com/Kollivnk/Webpage-Query-Application).

## Acknowledgements

- Streamlit for the web application framework.
- OpenAI for the GPT-3.5-turbo model.
- BeautifulSoup for HTML parsing.
