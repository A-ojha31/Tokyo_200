**Data Scraping Process:** We used the GitHub API to collect user data for developers in Tokyo with over 200 followers, along with repository information, splitting the task into separate scripts to optimize efficiency and avoid rate limits.

**Interesting Finding:** Our analysis revealed that JavaScript is the most commonly used language, yet Python repositories tend to have higher average star counts, highlighting its popularity and community engagement among followers.

**Recommendation for Developers:** Developers in Tokyo aiming for visibility should consider contributing to Python projects, as repositories in this language have a higher chance of engagement, which may help increase their follower count.

Project Overview
This project uses GitHub’s REST API to scrape user and repository data for developers based in Tokyo with a follower count exceeding 200. The goal is to analyze trends in programming languages, engagement metrics, and company affiliations.

Files
users.csv: Contains detailed information on each user, including their GitHub ID, name, company (cleaned for consistency), follower and following counts, bio, and GitHub join date.
repositories.csv: Includes data on each user’s public repositories (up to 500), covering details like the repository’s name, star count, primary language, and other settings (e.g., projects, wikis).
Data Collection Approach
User Data Extraction: A script (fetch_users) was created to gather user details and save them in users.csv. It uses pagination to capture multiple pages of users.

Repository Data Extraction: The second script (fetch_repos) reads users.csv to fetch repositories for each user, saving the data in repositories.csv. This split approach avoids redundant requests and ensures efficiency.

Key Analysis Findings
Top Languages: JavaScript, Python, and Ruby are the most popular languages among Tokyo developers in our dataset.
Engagement Patterns: Python repositories, on average, have a higher star count per repository, indicating greater community interest.
Company Affiliations: Most users are affiliated with tech giants and leading startups, with open-source projects showing a strong presence among individual developers.
Recommendations
Based on our analysis, developers in Tokyo looking to increase engagement could focus on popular languages like Python or JavaScript and consider affiliating with companies that have a visible GitHub presence.
