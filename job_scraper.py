# Import necessary packages for web scraping and logging
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
from urllib.parse import quote_plus
from tqdm import tqdm
import os
# Configure logging settings
logging.basicConfig(filename="scraping.log", level=logging.INFO)


def scrape_linkedin_jobs(job_title: str, location: str, pages: int = None) -> list:
    """
    Scrape job listings from LinkedIn based on job title and location.

    Parameters
    ----------
    job_title : str
        The job title to search for on LinkedIn.
    location : str
        The location to search for jobs in on LinkedIn.
    pages : int, optional
        The number of pages of job listings to scrape. If None, all available pages will be scraped.

    Returns
    -------
    list of dict
        A list of dictionaries, where each dictionary represents a job listing
        with the following keys: 'job_title', 'company_name', 'location', 'posted_date',
        and 'job_description'.
    """

    # Log a message indicating that we're starting a LinkedIn job search
    logging.info(f'Starting LinkedIn job scrape for "{job_title}" in "{location}"...')

    # Sets the pages to scrape if not provided
    pages = pages or 1

    # Set up the Selenium web driver
    # driver = webdriver.Chrome("chromedriver.exe")

    # Set up Chrome options to maximize the window
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Initialize the web driver with the Chrome options
    driver = webdriver.Chrome(options=options)

    # Navigate to the LinkedIn job search page with the given job title and location
    driver.get(
        f"https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}"
    )

    # Scroll through the first 50 pages of search results on LinkedIn
    for i in range(pages):

        # Log the current page number
        logging.info(f"Scrolling to bottom of page {i+1}...")

        # Scroll to the bottom of the page using JavaScript
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        try:
            # Wait for the "Show more" button to be present on the page
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[1]/div/main/section[2]/button")
                )
            )
            # Click on the "Show more" button
            element.click()

        # Handle any exception that may occur when locating or clicking on the button
        except Exception:
            # Log a message indicating that the button was not found and we're retrying
            logging.info("Show more button not found, retrying...")

        # Wait for a random amount of time before scrolling to the next page
        time.sleep(random.choice(list(range(3, 7))))

    # Scrape the job postings
    jobs = []
    soup = BeautifulSoup(driver.page_source, "html.parser")
    job_listings = soup.find_all(
        "div",
        class_="base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card",
    )

    try:
        for job in tqdm(job_listings):
            # Extract job details

            # job title
            job_title = job.find("h3", class_="base-search-card__title").text.strip()
            # job company
            job_company = job.find(
                "h4", class_="base-search-card__subtitle"
            ).text.strip()
            # job location
            job_location = job.find(
                "span", class_="job-search-card__location"
            ).text.strip()
            # job link
            apply_link = job.find("a", class_="base-card__full-link")["href"]

            # Navigate to the job posting page and scrape the description
            driver.get(apply_link)

            # Sleeping randomly
            time.sleep(random.choice(list(range(5, 11))))

            # Use try-except block to handle exceptions when retrieving job description
            try:
                # Create a BeautifulSoup object from the webpage source
                description_soup = BeautifulSoup(driver.page_source, "html.parser")

                # Find the job description element and extract its text
                job_description = description_soup.find(
                    "div", class_="description__text description__text--rich"
                ).text.strip()

            # Handle the AttributeError exception that may occur if the element is not found
            except AttributeError:
                # Assign None to the job_description variable to indicate that no description was found
                job_description = None

                # Write a warning message to the log file
                logging.warning(
                    "AttributeError occurred while retrieving job description."
                )

            # Add job details to the jobs list
            jobs.append(
                {
                    "title": job_title,
                    "company": job_company,
                    "location": job_location,
                    "link": apply_link,
                    "description": job_description,
                }
            )
            # Logging scrapped job with company and location information
            logging.info(f'Scraped "{job_title}" at {job_company} in {job_location}...')

    # Catching any exception that occurs in the scrapping process
    except Exception as e:
        # Log an error message with the exception details
        logging.error(f"An error occurred while scraping jobs: {str(e)}")

        # Return the jobs list that has been collected so far
        # This ensures that even if the scraping process is interrupted due to an error, we still have some data
        return jobs

    # Close the Selenium web driver
    driver.quit()

    # Return the jobs list
    return jobs


def save_job_data(data: dict) -> None:
    """
    Save job data to a CSV file, appending to it if it already exists.

    Args:
        data: A list of dictionaries containing job data.

    Returns:
        None
    """

    # Create a pandas DataFrame from the job data list
    df = pd.DataFrame(data)

    # Determine whether the file already exists
    file_exists = os.path.isfile("jobs.csv")

    # Save the DataFrame to a CSV file, appending without the header if file already exists
    df.to_csv("jobs.csv", mode='a', index=False, header=not file_exists)

    # Log a message indicating how many jobs were successfully appended to the CSV file
    logging.info(f"Successfully scraped {len(data)} jobs and appended to jobs.csv")




if __name__ == '__main__':
    positions_job_titles2 = [
     "Intern", "President", "Sales Associate", "Teacher", "Administrative Assistant", "Manager",
    "Project Manager", "Office Manager", "General Manager", "Registered Nurse", "Customer Service Representative",
    "Research Assistant", "Software Engineer", "Assistant Manager", "Consultant", "Realtor", "Server", "Cashier",
    "Account Manager", "Account Executive", "Business Owner", "owner", "CEO", "Operations Manager",
    "Sales Representative", "Associate", "Vice President", "retired", "Director", "Sales Manager", "Student",
    "Store Manager", "Executive Assistant", "RN", "Founder", "Partner", "Supervisor", "Sales", "Attorney",
    "Executive Director", "Principal", "Graphic Designer", "Summer Intern", "Real Estate Agent", "Receptionist",
    "Accountant", "Substitute Teacher", "Teaching Assistant", "Barista", "Bartender", "Instructor", "Volunteer",
    "Marketing Intern", "teacher", "Medical Assistant", "Chief Executive Officer", "Paralegal", "Legal Assistant",
    "Senior Software Engineer", "Office Assistant", "Controller", "Program Manager", "Co-Founder", "Secretary",
    "Project Engineer", "Software Developer", "Staff Accountant", "Engineer", "Branch Manager", "Adjunct Professor",
    "Business Analyst", "Board Member", "Law Clerk", "Managing Director", "Customer Service", "Crew Member",
    "Certified Nursing Assistant", "Photographer", "Marketing Manager", "Property Manager",
    "Special Education Teacher", "Pharmacy Technician", "Technician", "Member", "Designer", "Sales Consultant",
    "Senior Consultant", "Hostess", "Business Development Manager", "Security Officer", "Undergraduate Research Assistant",
    "Graduate Research Assistant", "Bookkeeper", "Legal Intern", "Analyst", "Lifeguard",
]

    positions2 =[
           "Physical Design Engineer","Carrier Certification Expert",
        "Electronic Engineering Technician","Electronics Engineering Manager","Electronics Engineering Technician","Electronics Test Technician","Verification Engineer",
        "Electronics Technician", "Physical Layer Hardware Architecture Engineer", "Embedded Engineer",
        "Embedded Software Engineer",
        "Electronics Test Engineer", "Electronics Engineer", "Electronics Design Engineer", "Electronics Hardware",
        "Senior Interconnect Hardware Test Engineer",

    ]

    positions=[
     "Information Security Engineer", "SecOps Engineer"]
    for job_title in tqdm(positions):
        print("Scraping job data for: ", job_title)
        current_job= quote_plus(job_title)
        data_current = scrape_linkedin_jobs(current_job, "US")
        save_job_data(data_current)

    # data = scrape_linkedin_jobs("Data+analyst", "US")
    # save_job_data(data)
