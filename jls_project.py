from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

required_role = input("What is the role you are looking for: ")
required_location = input("What is the location you are looking for: ")

driver = webdriver.Chrome()

file_no = 0
no_of_elems = 0


for _ in range(4):
    required_role_linkedin = required_role.replace(" ", "%20")
    driver.get(f"https://www.linkedin.com/jobs/search/?geoId=102713980&keywords={required_role_linkedin}&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")
    time.sleep(4)

    try:
        element1 = driver.find_element(By.CLASS_NAME, "third-party-join__gsi-btn-container")
    except NoSuchElementException:
        element1 = None

    try:
        element2 = driver.find_element(By.CLASS_NAME, "google-auth-button__placeholder")
    except NoSuchElementException:
        element2 = None

    if element1 or element2:
        continue

    driver.implicitly_wait(5)
    for _ in range(6):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        driver.execute_script("window.scrollBy(500, 0);")
        time.sleep(5)
    driver.implicitly_wait(5)
    more_button_linkedin = driver.find_element(By.CLASS_NAME, "infinite-scroller__show-more-button")
    
    for _ in range(5):
        more_button_linkedin.click()
        driver.execute_script("window.scrollBy(0, 1500);")
        time.sleep(4)

    elems = driver.find_elements(By.CLASS_NAME , "base-search-card__info")
    no_of_elems += len(elems)

    for elem in elems:
        linkedin_data = elem.get_attribute("outerHTML")

        with open(f"jls_linkedin_database/{required_role}_{file_no}.html", "w", encoding="utf-8") as f:
            f.write(linkedin_data)
            file_no += 1
    break


try:
    for i in range(4):
        required_role_indeed = required_role.replace(" ", "+")
        driver.get(f"https://in.indeed.com/jobs?q={required_role_indeed}&l={required_location}&start={10*i}")
        time.sleep(5)
        elems = driver.find_elements(By.CLASS_NAME, "resultContent")
        no_of_elems += len(elems)

        for elem in elems:
            indeed_data = elem.get_attribute("outerHTML")

            with open(f"jls_indeed_database/{required_role}_{file_no}.html", "w", encoding="utf-8") as f:
                f.write(indeed_data)
                file_no += 1


    required_role_glassdoor = required_role.replace(" ", "-")
    driver.get(f"https://www.glassdoor.co.in/Job/{required_role_glassdoor}-jobs-SRCH_KO0,{len(required_role_glassdoor)}.htm")
    driver.implicitly_wait(5)
    more_button = driver.find_element(By.CSS_SELECTOR, '[data-test="load-more"]')
    more_button.click()
    driver.implicitly_wait(5)
    cross_button_indeed = driver.find_element(By.CLASS_NAME, "CloseButton")
    cross_button_indeed.click()
    
    for _ in range(3):
        time.sleep(5)
        more_button = driver.find_element(By.CSS_SELECTOR, '[data-test="load-more"]')
        more_button.click()
  
    elems = driver.find_elements(By.CLASS_NAME, "JobCard_jobCardContent__X81Ew")
    no_of_elems += len(elems)

    for elem in elems:
        data = elem.get_attribute("outerHTML")

        with open(f"jls_glassdoor_database/{required_role}_{file_no}.html", "w", encoding="utf-8") as f:
            f.write(data)
            file_no += 1

except IndexError:
    pass


time.sleep(2)
print(f"{no_of_elems} found")
driver.close()









# <a aria-label="Python Developer"></a>
# <div <span class="job-card-container__primary-description"

# segrigation of the data needed
