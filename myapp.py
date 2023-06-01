!pip install streamlit
import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    # Create a title for your app
    st.title("Dictionary Web Scraper")

    # Add an input field to enter the word
    word = st.text_input("Enter a word", "example")

    # Create a button to initiate the scraping process
    if st.button("Scrape"):
        # Make a GET request to the online dictionary
        url = f"https://www.yourdictionary.com/{word}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Find and display the definitions on the page
        definitions = soup.find_all("div", class_="sense")
        if definitions:
            for i, definition in enumerate(definitions):
                st.write(f"Definition {i+1}: {definition.text.strip()}")
                st.write("---")
        else:
            st.write("No definitions found.")

    # Add a footer or any additional information
    st.text("Web Scraper by Your Name")

# Call the main function directly
main()
