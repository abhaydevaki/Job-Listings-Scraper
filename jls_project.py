# from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc

required_role = input("What is the role you are looking for: ")
required_location = input("What is the location you are looking for: ")


# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\abhay\\AppData\\Local\\Google\\Chrome\\User Data")  # Adjust path
options.add_argument("--profile-directory=Profile 2")  # Change if needed
options.add_argument("--disable-blink-features=AutomationControlled")  # Helps bypass detection
options.add_argument("--start-maximized")  # Opens browser maximized


# Initialize undetected ChromeDriver
driver = uc.Chrome(options=options)
time.sleep(5)

# The below code is to start the undetected chrome driver. This provides no login features.
# driver = uc.Chrome()
# The below code is to start the web chrome driver.This also provides no login features.
# driver = webdriver.Chrome()

file_no = 0
no_of_elems = 0


# The below code is to get the data from LinkedIn.
for _ in range(1):
    required_role_linkedin = required_role.replace(" ", "%20")
    driver.get(f"https://www.linkedin.com/jobs/search/?geoId=102713980&keywords={required_role_linkedin}&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")
    time.sleep(5)
    
    try:
        elems = driver.find_elements(By.CSS_SELECTOR, ".flex-grow-1.artdeco-entity-lockup__content.ember-view")
        no_of_elems += len(elems)
    except NoSuchElementException:
        print("No elements found")

    for elem in elems:
        linkedin_data = elem.get_attribute("outerHTML")

        with open(f"jls_linkedin_database/{required_role}_{file_no}.html", "w", encoding="utf-8") as f:
            f.write(linkedin_data)
            file_no += 1


# The below code is to get the data from Indeed.
try:
    for i in range(3):
        required_role_indeed = required_role.replace(" ", "+")
        driver.get(f"https://in.indeed.com/jobs?q={required_role_indeed}&l={required_location}&start={i*15}")
        time.sleep(5)
        elems = driver.find_elements(By.CLASS_NAME, "resultContent")
        no_of_elems += len(elems)

        for elem in elems:
            indeed_data = elem.get_attribute("outerHTML")

            with open(f"jls_indeed_database/{required_role}_{file_no}.html", "w", encoding="utf-8") as f:
                f.write(indeed_data)
                file_no += 1


    # The below code is to get the data from Glassdoor.
    required_role_glassdoor = required_role.replace(" ", "-")
    driver.get(f"https://www.glassdoor.co.in/Job/{required_role_glassdoor}-jobs-SRCH_KO0,{len(required_role_glassdoor)}.htm")
    driver.implicitly_wait(5)
    more_button = driver.find_element(By.CSS_SELECTOR, '[data-test="load-more"]')
    more_button.click()
    driver.implicitly_wait(5)
    cross_button_indeed = driver.find_element(By.CLASS_NAME, "CloseButton")
    cross_button_indeed.click()
    
    for _ in range(5):
        time.sleep(5)
        more_button = driver.find_element(By.CSS_SELECTOR, '[data-test="load-more"]')
        more_button.click()
  
    elems = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardWrapper__vX29z")
    no_of_elems += len(elems)

    for elem in elems:
        data = elem.get_attribute("outerHTML")

        with open(f"jls_glassdoor_database/{required_role}_{file_no}.html", "w", encoding="utf-8") as f:
            f.write(data)
            file_no += 1

except IndexError:
    pass


driver.close()
