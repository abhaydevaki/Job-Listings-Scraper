from bs4 import BeautifulSoup
import os
import pandas as pd
from jls_project import *

dict = {"company" : [], "role" : [], "location" : [], "link" : []}

for file in os.listdir("jls_linkedin_database"):
    try:
        with open(f"jls_linkedin_database/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        c = soup.find("h4")
        company = c.get_text()

        r = soup.find("h3")
        role = r.get_text()

        loc = soup.find("span", attrs={"class": "job-search-card__location"})
        location = loc.get_text()

        l = soup.find("a")
        link = l["href"]
        

        if required_location.lower() in location.lower():
            dict["company"].append(company.strip())
            dict["role"].append(role.strip())
            dict["location"].append(location.strip())
            dict["link"].append(link.strip())
        
    
    except Exception as e:
        print(e)
        pass

for file in os.listdir("jls_indeed_database"):
    try:
        with open(f"jls_indeed_database/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        c = soup.find("div", attrs={"class": "css-1qv0295"})
        company = c.get_text()

        r = soup.find("h2", attrs={"class": "jobTitle"})
        role = r.get_text()

        loc = soup.find("div", attrs={"class": "css-1p0sjhy"})
        location = loc.get_text()

        l = soup.find("a")
        print(l)
        link = "https://in.indeed.com" + l["href"]
        print(link)

        dict["company"].append(company.strip())
        dict["role"].append(role.strip())
        dict["location"].append(location.strip())
        dict["link"].append(link.strip())
        
    
    except Exception as e:
        print(e)

for file in os.listdir("jls_glassdoor_database"):
    try:
        with open(f"jls_glassdoor_database/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, "html.parser")

        c = soup.find("div", attrs={"class": "EmployerProfile_compact__nP9vu"})
        company = c.get_text()

        r = soup.find("a", attrs={"class": "JobCard_jobTitle___7I6y"})
        role = r.get_text()

        loc = soup.find("div", attrs={"class": "JobCard_location__rCz3x"})
        location = loc.get_text()

        l = soup.find("a")
        link = l["href"]

        if required_location.lower() in location.lower():
            dict["company"].append(company.strip())
            dict["role"].append(role.strip())
            dict["location"].append(location.strip())
            dict["link"].append(link.strip())
        
    
    except Exception as e:
        print(e)

df = pd.DataFrame(data=dict)
df.to_csv("jls_data.csv")

