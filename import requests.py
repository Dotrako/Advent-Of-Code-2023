import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.ukud.co.uk/faqs"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the FAQ section (you may need to inspect the HTML structure of the page to find the appropriate elements)
    faq_section = soup.find("section", class_="ukud-faq")

    # Extract the questions and answers
    if faq_section:
        questions = faq_section.find_all("h2")  # Assuming questions are wrapped in <h2> tags
        answers = faq_section.find_all("div", class_="ukud-faq-answer")  # Assuming answers are wrapped in <div> tags with class "ukud-faq-answer"

        # Print the questions and answers
        for question, answer in zip(questions, answers):
            print("Question:", question.get_text(strip=True))
            print("Answer:", answer.get_text(strip=True))
            print("="*50)
    else:
        print("FAQ section not found on the page.")
else:
    print("Failed to fetch the webpage:", response.status_code)

