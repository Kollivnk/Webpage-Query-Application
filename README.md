Webpage Query Application
This application allows users to fetch content from a webpage, process it, and query the content using OpenAI's GPT-3.5-turbo model. Built with Streamlit, it provides an interactive interface for users to input a URL and ask questions about the webpage content.

Features
-Fetch content from any webpage.
-Process and extract text content using BeautifulSoup.
-Query the extracted content using OpenAI's GPT-3.5-turbo model.
-Interactive web interface built with Streamlit.


Installation:
1.Clone the repository:
 git clone https://github.com/your-username/webpage-query-app.git
 cd webpage-query-app
2.Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
3.Install the required packages:
   streamlit: For building the interactive web interface.
   requests: For making HTTP requests to fetch webpage content.
   beautifulsoup4: For parsing and extracting text from HTML content.
   openai: For interacting with the OpenAI API.
4.Set up OpenAI API key:
   You can set your OpenAI API key in the environment variables for better security. Create a .env file and add your key:
   OPENAI_API_KEY=your_openai_api_key
   Alternatively, you can directly set your API key in the app.py file (less secure).

Usage:
1.Run the Streamlit application
  streamlit run app.py
2.Use the application
  Enter the URL of the webpage you want to fetch.
  Click on "Fetch and Process" to retrieve and process the webpage content.
  Enter your query in the provided input box.
  Click on "Query Document" to get the response from the GPT-3.5-turbo model based on the webpage content.

Acknowledgements:
 Streamlit for the web application framework.
 OpenAI for the GPT-3.5-turbo model.
 BeautifulSoup for HTML parsing.
