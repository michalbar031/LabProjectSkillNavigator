# Lab Project Skill Navigator
Welcome to The Skills Navigator README.
This document provides a detailed overview of our project including how to get started, use the project, and where to find additional support.

## Introduction
Our project follows several key steps: analyzing the user's current profile, finding the relevant existing jobs personalized for the user, identifying the job projected to have the highest demand in the next year, and extracting the necessary skills for that job. We then recommend these skills to the user, advising them to acquire or enhance these competencies during the upcoming period. This approach ensures that the user remains aligned with emerging trends and demands in their field.

## Get started

to install

Add gemini API key in the first cell in LLM Skills Extraction section.
```bash
GOOGLE_API_KEY = ''
```


Dependencies: You need to have a gemini API key to get Recommendation .

Installation: Add jobs_scraped_path table path in the first cell in NLP preprocessing section.
Dependencies: jobs_scraped table is needed to get Recommendation.


## How to add user to get recommendation:
Run cell below
Input User Details: You'll need to type in the details requested by the function. For example, when prompted for the user ID, you'll input a number to uniquely identify the user. Similarly, you'll input the industry and preferences of the user as requested. This function requires four things:

user_id: A unique identifier for the new user.
user_industry: The industry or field the user belongs to.
user_preferences: A description of the user's preferences or skills.
df_users: The DataFrame where we want to add the new user.
Provide User Details: When you call the function, you'll provide the details of the new user as arguments. For example:

user_id: You'll assign a unique number to identify this user.
user_industry: You'll specify the industry the user belongs to (e.g., "Data Science", "Software Development").
user_preferences: You'll describe the user's preferences or skills (e.g., "Passionate about data analysis and machine learning.").
View the Updated DataFrame: After calling the function, the new user will be added to the DataFrame. You can then view the DataFrame to confirm that the user has been successfully added.

Remember, each user should have a unique user ID to distinguish them from one another. Also, make sure to provide accurate details for the new user to ensure the integrity of the data.
