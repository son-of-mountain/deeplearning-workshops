from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

url = "https://www.hespress.com/politique"

# Define the end time
end_time = time.time() + 60 * 1  # end time is 1 minutes from now

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the URL
driver.get(url)

# Scroll to the bottom of the page until the end time
while time.time() < end_time:
    # scroll to the bottom of the page so that posts are loaded
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for 2 seconds to load the page

soup = BeautifulSoup(driver.page_source, 'html.parser')

titles = soup.find_all('a', class_='stretched-link')

title_texts = [title.get('title') for title in titles]

# Create a DataFrame from the titles array
df = pd.DataFrame(title_texts, columns=['title'])

# Add a new column "score" and set its value to 0
df['score'] = 0

# Write the DataFrame to a CSV file
df.to_csv('news.csv', index=False)
