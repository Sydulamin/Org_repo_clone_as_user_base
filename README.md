# GitHub Repository Cloner with Role-Based Permissions

This Python script allows you to clone repositories from a GitHub user or organization, while incorporating a role-based permission system. Users with different roles (Admin, Contributor, Viewer) can access repositories based on their permissions. Additionally, the script integrates **Black**, a Python code formatter, which formats the script automatically after it runs.

---

## Features

- Fetch all repositories of a specified GitHub user or organization.
- Supports role-based permissions:
  - **Admin**: Access to all repositories (public and private).
  - **Contributor**: Access to public and contributed repositories.
  - **Viewer**: Access to public repositories only.
- Handles pagination for large repositories.
- Automatically skips cloning repositories that already exist locally.
- **Black Integration**: Automatically formats the Python script using Black after it runs.

---

## Prerequisites

1. **Python 3.x**: Ensure you have Python installed.
2. **Git**: The script uses `git` for cloning repositories.
3. **Libraries**: Install the required Python libraries by running:
   ```bash
   pip install requests black

## Usage
1. Clone the Repository
Download or clone this script to your local machine:

## bash
Copy code
  ```bash
  git clone https://github.com/Sydulamin/repository-cloner.git
  cd repository-cloner

2. Update the Script
Edit the script to configure the following variables:

## GitHub Username or Organization: Replace github_user_or_org with the desired GitHub username or organization.
Your GitHub Username: Replace github_username with your GitHub username.
Role: Set user_role to one of the roles (Admin, Contributor, or Viewer).
Personal Access Token (Optional): Replace personal_access_token with your GitHub token if private repositories need to be accessed.

3. Run the Script
Run the script to clone repositories based on your role:
Copy code

  ```bash
  python repository_cloner.py

After the script runs, it will automatically format the code using Black.

## Example Configuration
![image](https://github.com/user-attachments/assets/ac6c7200-b280-443d-a685-a7b808a5854d)


## Admin Role
python
Copy code

  ```bash
  github_user_or_org = "octocat"
  github_username = "your-username"
  user_role = "Admin"
  personal_access_token = "your-personal-access-token"


## Contributor Role
python
Copy code

  ```bash
  github_user_or_org = "octocat"
  github_username = "your-username"
  user_role = "Contributor"
  personal_access_token = None


## Viewer Role
python
Copy code

  ```bash
  github_user_or_org = "octocat"
  github_username = "your-username"
  user_role = "Viewer"
  personal_access_token = None

## Output
The script will create a directory named cloned_repos (default) in the current working directory.
Each repository will be cloned into a subdirectory within cloned_repos.

## Notes
Private Repositories: A Personal Access Token (PAT) is required to access private repositories. You can generate a token here.
Existing Repositories: The script skips cloning repositories that already exist in the target directory.
Black Formatting: The script automatically formats itself using Black after it completes its operations. Ensure that you have Black installed to use this feature.


## Repository Owner
This repository is maintained by SYDUL AMIN. You can find more of my projects on my GitHub Profile.

markdown
Copy code

### Changes Made:
- Added your name, **SYDUL AMIN**, as the repository owner.
- Included a link to your GitHub profile at the end of the README for easy access.

This should be ready to go for your project!
