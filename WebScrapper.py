import requests
from bs4 import BeautifulSoup
import time
import json
import re
#Retry mechanism and data scrapoing function

def fetch_data_with_retries(url,retries=3,delay=2):
    """
        Fetches data from a URL with retries in case of failure
    """
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1} failed {e}")   
            if attempt < retries -1:
                time.sleep(delay* (attempt+1)) #Exponential backoff
            else:
                raise
#Function to extract data using the beautifulsoup and regular expression

def extract_data_from_html(html_content):
    """
        Extracting the relevant data (Links containing 'Python') from the HTML content
    """
    if not html_content:
        raise ValueError("HTML content is invalid or empty!!!")
    
    soup = BeautifulSoup(html_content,'html.parser')
    titles=[]

    #Regular expression to find all the links witht teh specific texxt (python)
    for link in soup.find_all('a', href=True):
        title= link.get_text(strip=True)
        if re.match(r'python*',title,re.IGNORECASE): #Looking for the links containing python
            titles.append(title)
        
    return titles
    
#Function to save the data in the json file

def save_data_to_json(data,filename="scraped_data.json"):
    """
    Saves the extracted data to a json file
    """
    try:
        with open(filename,'w') as file:
            json.dump(data,file,indent=4)
        print(f"Data has beeen save to {filename}")
    except Exception as e:
        print(f"Error savinig thr data to the file {e}")


#URL to scrape

url="https://docs.python.org/3/"

html_content = fetch_data_with_retries(url)
extract_data=extract_data_from_html(html_content)
save_data_to_json(extract_data)