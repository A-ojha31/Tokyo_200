import requests
import pandas as pd
import re

# GitHub API settings
GITHUB_API_URL = "https://api.github.com"
TOKEN = "XXXXXXXXXXXX"  # GitHub personal access token

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Step 1: Fetching detailed user information for users in Tokyo with over 200 followers
def fetch_users(location="Tokyo", min_followers=200):
    url = f"{GITHUB_API_URL}/search/users?q=location:{location}+followers:>{min_followers}&per_page=100"
    users = []
    page = 1

    while True:
        paginated_url = f"{url}&page={page}"
        response = requests.get(paginated_url, headers=headers)
        response.raise_for_status()
        user_page = response.json().get("items", [])

        if not user_page:
            break  # if there are no more users

        for user in user_page:
            # Fetching individual user details
            user_url = f"{GITHUB_API_URL}/users/{user['login']}"
            user_response = requests.get(user_url, headers=headers)
            user_response.raise_for_status()
            user_data = user_response.json()

            # Cleaning up the company name as per guidelines
            company_name = user_data.get("company", "")
            if company_name:
                company_name = re.sub(r"^@+", "", company_name).strip().upper()

            # Adding cleaned and detailed user information to the list
            users.append({
                "login": user_data.get("login"),
                "name": user_data.get("name", ""),
                "company": company_name,
                "location": user_data.get("location", ""),
                "email": user_data.get("email", ""),
                "hireable": user_data.get("hireable", ""),
                "bio": user_data.get("bio", ""),
                "public_repos": user_data.get("public_repos", ""),
                "followers": user_data.get("followers", ""),
                "following": user_data.get("following", ""),
                "created_at": user_data.get("created_at", ""),
            })

        page += 1  # Move to the next page

    return users

# Collect user data and save to CSV
users = fetch_users()
pd.DataFrame(users).to_csv("users.csv", index=False)
print("User data saved to users.csv.")
