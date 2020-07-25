from fetching import Fetcher
import sys
sys.path.append("./PyGithub");
from github import Github
import json
import getpass


username = input("Github Username: ")
password = getpass.getpass()
account = Github(username, password)
repo_name = input("Name of Repository: ")
repository = None
for repo in account.get_user().get_repos():
        if repo.name == repo_name:
            repository = repo

fetcher = Fetcher(repository)
contributors = fetcher.get_contributors()
metadata = fetcher.get_metadata()
contributor_stats = fetcher.get_contributor_stats()
commit_stats = fetcher.get_commit_stats()
code_freq = fetcher.get_code_frequency()
print(contributors, metadata, contributor_stats, commit_stats, code_freq)