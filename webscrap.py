import requests
from bs4 import BeautifulSoup

URL = 'https://jobsinkenya.net/Kenya/Software%20Developing'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='jobs-container')

job_elems = results.find_all('div', class_='job-wrapper')

#python_jobs = results.find_all('div', string=lambda text: 'python' in text.lower())

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    title_elem = job_elem.find('span', class_='job-name-span')
    company_elem = job_elem.find('div', class_='job-company')
    location_elem = job_elem.find('div', class_='job-location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()

