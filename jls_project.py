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
options.add_argument("--profile-directory=Profile 9")  # Change if needed
options.add_argument("--disable-blink-features=AutomationControlled")  # Helps bypass detection
options.add_argument("--start-maximized")  # Opens browser maximized
# print(options)


# Initialize undetected ChromeDriver
driver = uc.Chrome(options=options)
time.sleep(5)

# The below code is to start the undetected chrome driver. This provides no login features.
# driver = uc.Chrome()
# The below code is to start the web chrome driver.This also provides no login features.
# driver = webdriver.Chrome()

file_no = 0
no_of_elems = 0


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

# for _ in range(4):
#     required_role_linkedin = required_role.replace(" ", "%20")
#     driver.get(f"https://www.linkedin.com/jobs/search/?geoId=102713980&keywords={required_role_linkedin}&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")
#     time.sleep(4)
# # artdeco-icon lazy-loaded
#     # try: 
#     #     cross_button_linkedin = driver.find_element(By.CLASS_NAME, "modal__dismiss btn-tertiary h-[40px] w-[40px] p-0 rounded-full indent-0contextual-sign-in-modal__modal-dismiss absolute right-0 m-[20px] cursor-pointer")    
#     #     cross_button_linkedin.click()
#     # except NoSuchElementException:
#     #     pass
#     try:
#         element1 = driver.find_element(By.CLASS_NAME, "third-party-join__gsi-btn-container")
#     except NoSuchElementException:
#         element1 = None

#     try:
#         element2 = driver.find_element(By.CLASS_NAME, "google-auth-button__placeholder")
#     except NoSuchElementException:
#         element2 = None

#     if element1 or element2:
#         continue

#     driver.implicitly_wait(5)
#     # for _ in range(6):
#     #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     #     time.sleep(3)
#     #     driver.execute_script("window.scrollBy(500, 0);")
#     #     time.sleep(5)
#     # driver.implicitly_wait(5)
#     # more_button_linkedin = driver.find_element(By.CLASS_NAME, "infinite-scroller__show-more-button")
    
#     # for _ in range(5):
#     #     more_button_linkedin.click()
#     #     driver.execute_script("window.scrollBy(0, 1500);")
#     #     time.sleep(4)

#     elems = driver.find_elements(By.CLASS_NAME , "base-search-card__info")
#     no_of_elems += len(elems)

#     for elem in elems:
#         linkedin_data = elem.get_attribute("outerHTML")

#         with open(f"jls_linkedin_database/{required_role}_{file_no}.html", "w", encoding="utf-8") as f:
#             f.write(linkedin_data)
#             file_no += 1
#     break

# time.sleep(2)
# # print(f"{no_of_elems} found")
driver.close()









# <a aria-label="Python Developer"></a>
# <div <span class="job-card-container__primary-description"

# segrigation of the data needed