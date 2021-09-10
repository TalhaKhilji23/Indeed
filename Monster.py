import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from common.constants import job_tiles_with_categories, keywordfilter
from common.logger import logger
# from common.common import process_job

driver = webdriver.Chrome()
wait = WebDriverWait(driver=driver, timeout=10)


def read_by_category(Country, Category):
    # job_filter = keywordfilter.get('keyword_filter', None)
    job_tiles = job_tiles_with_categories.get(Category, None)
    for job_key in job_tiles:
        print('Scrapping Keyword: ' + job_key)
        try:
            driver.get(
                "https://www.monster.com/jobs/search?q=" + job_key.lower() + "&where=" + Country)
            count = 0
            try:
                WebDriverWait(driver, 2).until(
                    ec.presence_of_element_located(
                        (By.CSS_SELECTOR, '.f-l.col-9')))
                print(job_key + 'Properly Empty')
            except:
                prev_height = driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                while True:
                    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                    new_height = driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
                    if new_height == prev_height:
                        break
                    prev_height = new_height
                page = 1
                Found = True
                while Found:
                    jobs = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, '.title-company-location ')))

                    for job in jobs:
                        job_title = job.find_element_by_class_name('.card-title')
                        # lentitle = (len(job_title))
                        # if (lentitle > 0):
                        print('==================Title : ', job_title, ' ====================')
                        job_url = job.get_attribute('href')
                        company_name = job.find_element_by_css_selector(".card-company-name").text.replace(",", "")
                        company_location = job.find_element_by_css_selector(".card-job-location").text.replace(",","")
                        print(f"Company NAme : {company_name}")
                        print(f"Job URL : {job_url}")
                        print(f"Company Location : {company_location}")
                        # process_job("Indeed", job_title, Category, job_url, company_location, company_name, job_key)
                        # else:
                        #     continue
                    # Changing page Number by the addition of "Start=" and multiple of 10s in the link
                    # try:
                    #     count += 10
                    #     driver.get("https://www.indeed.com/jobs?q=" + job_key.lower().replace(" ","%20") + "&l=" + Country.replace(" ", "%20") + "&start={}".format(count))
                    #     page2 = int(wait.until(
                    #         ec.presence_of_element_located((By.ID, 'searchCountPages'))).text.strip().split(' ')[1])
                    #     print(type(page2))
                    #     if (page2 > page):
                    #         print('new page')
                    #     else:
                    #         print('Was last page')
                    #         Found = False
                    #     page = page2
                    # except:
                    #     print('shouldn"t come here')

        except Exception as error:
            print("Error: ", error)
        finally:
            # driver.quit()
            pass


if __name__ == '__main__':
    code = "us"
    read_by_category('California', 'Engineering')

    # read_by_category('United States', 'Engineering')

    # read_by_category('United States', 'Salesforce')
    # read_by_category('United States', 'Sales')

    # read_by_category('United States', 'Advertising')
    # read_by_category('United States', 'Design')
    #
    # read_by_category('United States', 'Customer Service')
    # read_by_category('United States', 'Staffing')
    # read_by_category('United States', 'AWS')
    #
    # read_by_category('United States', 'Google Cloud')
    # read_by_category('United States', 'ArtificialIntelligence')
    # read_by_category('United States', 'Shopify')
