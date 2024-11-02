import requests
import pandas as pd

# GitHub API settings
GITHUB_API_URL = "https://api.github.com"
TOKEN = "XXXXX"  # GitHub personal access token

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Step 1: Fetching up to 500 repositories for each user collected in users.csv
def fetch_repos(username, max_repos=500):
    url = f"{GITHUB_API_URL}/users/{username}/repos?per_page=100"
    repos = []
    page = 1

    while len(repos) < max_repos:
        paginated_url = f"{url}&page={page}"
        response = requests.get(paginated_url, headers=headers)
        response.raise_for_status()
        repo_page = response.json()

        if not repo_page:
            break  # if there are no more repos

        repos.extend(repo_page)
        page += 1

    # Limiting to the max_repos specified
    return repos[:max_repos]

# Step 2: Reading users from users.csv and fetch their repositories
users_df = pd.read_csv("users.csv")
repo_data = []

for index, user in users_df.iterrows():
    username = user["login"]
    print(f"Fetching repositories for user: {username}")
    repos = fetch_repos(username, max_repos=500)
    
    for repo in repos:
        repo_data.append({
            "login": username,  # The login of the repository owner
            "full_name": repo.get("full_name"),
            "created_at": repo.get("created_at"),
            "stargazers_count": repo.get("stargazers_count", 0),
            "watchers_count": repo.get("watchers_count", 0),
            "language": repo.get("language", ""),
            "has_projects": repo.get("has_projects", False),
            "has_wiki": repo.get("has_wiki", False),
            "license_name": repo.get("license", {}).get("key", "") if repo.get("license") else ""
        })

# Saving repository data to CSV
pd.DataFrame(repo_data).to_csv("repositories.csv", index=False)
print("Repository data saved to repositories.csv.")
