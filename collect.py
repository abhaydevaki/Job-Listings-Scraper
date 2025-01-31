from bs4 import BeautifulSoup
import os
import pandas as pd
from jls_project import *

dict = {"company" : [], "role" : [], "location" : [], "link" : []}

# Linkedin
for file in os.listdir("jls_linkedin_database"):
    try:
        with open(f"jls_linkedin_database/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        # Extract Company Name
        c = soup.find("div", class_="artdeco-entity-lockup__subtitle")
        company = c.get_text(strip=True)

        # Extract Role
        r = soup.find("a", class_="job-card-container__link").find("strong")
        role = r.get_text(strip=True)

        # Extract Location
        loc = soup.find("div", class_="artdeco-entity-lockup__caption")
        location = loc.find("span").get_text(strip=True)

        # Extract Job URL
        l = soup.find("a", class_="job-card-container__link")
        link = "https://www.linkedin.com" + l["href"]
        
        if required_location.lower() == "bangalore":
            required_location = "bengaluru"
        if required_location.lower() in location.lower():
            dict["company"].append(company.strip())
            dict["role"].append(role.strip())
            dict["location"].append(location.strip())
            dict["link"].append(link.strip())
           
    except Exception as e:
        pass

# Indeed
for file in os.listdir("jls_indeed_database"):
    try:
        with open(f"jls_indeed_database/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        c = soup.find("span", attrs={"data-testid": "company-name"})
        company = c.get_text()

        # Extract job role
        r = soup.find("h2", attrs={"class": "jobTitle"})
        role = r.get_text()

        # Extract location
        loc = soup.find("div", attrs={"data-testid": "text-location"})
        location = loc.get_text()

        # Extract job link
        l = soup.find("a", attrs={"class": "jcs-JobTitle"})
        link = "https://in.indeed.com" + l["href"]

        dict["company"].append(company.strip())
        dict["role"].append(role.strip())
        dict["location"].append(location.strip())
        dict["link"].append(link.strip())
        
    except Exception as e:
        pass

# Glassdoor
for file in os.listdir("jls_glassdoor_database"):
    try:
        with open(f"jls_glassdoor_database/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")


        # Extract company name
        c = soup.find("span", class_="EmployerProfile_compactEmployerName__9MGcV")
        company = c.get_text(strip=True)

        # Extract job role
        r = soup.find("a", class_="JobCard_jobTitle__GLyJ1")
        role = r.get_text(strip=True)

        # Extract location
        loc = soup.find("div", class_="JobCard_location__Ds1fM")
        location = loc.get_text(strip=True)

        # Extract job link
        l = soup.find("a", class_="JobCard_jobTitle__GLyJ1")
        link = "https://" + l["href"]

        if required_location.lower() in location.lower():
            dict["company"].append(company)
            dict["role"].append(role)
            dict["location"].append(location)
            dict["link"].append(link)
        
    except Exception as e:
        pass


df = pd.DataFrame(data=dict)
df.to_csv("jls_data.csv")