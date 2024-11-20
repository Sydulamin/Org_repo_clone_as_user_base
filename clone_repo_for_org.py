import os
import subprocess
import requests
import black

def format_code_with_black(file_path):
    try:
        with open(file_path, "r") as file:
            source_code = file.read()

        formatted_code = black.format_file_contents(
            source_code, fast=False, mode=black.Mode()
        )

        with open(file_path, "w") as file:
            file.write(formatted_code)

        print(f"Formatted {file_path} using Black.")
    except Exception as e:
        print(f"Error formatting the file with Black: {e}")


def clone_repositories(github_user_or_org, target_directory="cloned_repos", token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"

    api_url = f"https://api.github.com/users/{github_user_or_org}/repos"
    params = {"per_page": 100}
    repos = []

    while api_url:
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: Unable to fetch repositories ({response.status_code}).")
            print(response.json().get("message", "Unknown error"))
            return

        repos.extend(response.json())
        api_url = response.links.get("next", {}).get("url")

    if not repos:
        print("No repositories found for the specified user/organization.")
        return

    os.makedirs(target_directory, exist_ok=True)

    for repo in repos:
        repo_name = repo["name"]
        clone_url = repo["clone_url"]
        repo_path = os.path.join(target_directory, repo_name)

        if os.path.exists(repo_path):
            print(f"Repository {repo_name} already exists. Skipping.")
            continue

        print(f"Cloning {repo_name}...")
        subprocess.run(["git", "clone", clone_url, repo_path])

    print("All repositories have been cloned.")


github_user_or_org = "Sydulamin"

personal_access_token = None

target_directory = "cloned_repos"

clone_repositories(github_user_or_org, target_directory, personal_access_token)

script_file_path = __file__ 
format_code_with_black(clone_repo_for_org.py)
