# Lab Project Skill Navigator
Welcome to The Skills Navigator README.
This document provides a detailed overview of our project including how to get started, use the project, and where to find additional support.

## Introduction
Our project follows several key steps: analyzing the user's current profile, finding the relevant existing jobs personalized for the user, identifying the job projected to have the highest demand in the next year, and extracting the necessary skills for that job. We then recommend these skills to the user, advising them to acquire or enhance these competencies during the upcoming period. This approach ensures that the user remains aligned with emerging trends and demands in their field.
## Files
Project_211624788_302342498_212673784_graphs.ipynb

## Installation

```bash
!pip install --upgrade numpy
!pip install numpy==1.21
!pip install prophet
!pip install spacy
!pip install sentence-transformers
!pip install langchain
!pip install langchain_google_genai 
```
in the file 
Add gemini API key in the first cell in LLM Skills Extraction section.
```bash
GOOGLE_API_KEY = ''
```
## Example
We will demonstrate a show case:
```bash
"Hi! I'm Alex and I am a software engineer with two years of experience. My architecture background bolsters my design skills and now, I specialize in frontend development. I create mobile first, responsive web applications that are highly efficient and scalable. I am always looking to learn new skills and work with new technologies. My main languages and technologies are HTML, CSS, Javascript, Typescript, Vue, and React. I also currently use AWS and noSQL databases at my current company.",

```
![image](https://github.com/michalbar031/LabProjectSkillNavigator/assets/81368958/cd9b669e-dce3-4425-a526-4af0907086b3)

After analyzing the best job in demand (Prophet) we use LLM and resive:
```bash
-------------------------------
Dear User 3,
Based on a careful analysis of your preferences and our predictive modeling, we anticipate that the following skill set will be highly sought after in your field. Acquiring these competencies will position you advantageously in the evolving job market.

We recommend that you acquire the following skill set:
- **Software Testing:** Experience with designing test plans, test cases, and preparing test data.
- **Database Concepts:** Familiarity with database concepts and how to write and perform queries to ensure data integrity, particularly with MongoDB and ElasticSearch.
- **Test Automation:** Foundational coding skills for test automation, particularly using TypeScript and Playwright.
- **Pipeline Concepts:** A foundational understanding of pipeline concepts, preferably GitLab.
- **Logging Tools:** Familiarity with logging tools, preferably DataDog.
- **Third-Party Integrations:** Exposure to third-party integrations such as Shopify, Magento, Segment, etc.
-------------------------------


```


## How to add user to get your recommendation:
Input User Details: You'll need to type in the details requested by the function. 

```bash
user_id
```
user_id: A unique identifier for the new user.
```bash
user_industry
```
user_industry: The industry or field the user belongs to.
```bash
user_preferences
```
user_preferences: A description of the user's preferences or skills.

Remember, each user should have a unique user ID to distinguish them from one another. Also, make sure to provide accurate details for the new user to ensure the integrity of the data.
## How to scrape
In the jobs_scraper.py you will find a list:
```bash
positions=[
     "Information Security Engineer", "SecOps Engineer"]
```
you can add all the jobs titles you want to scrape
