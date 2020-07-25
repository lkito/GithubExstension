from analyzer import Fetcher, RepoAnalyzer, Homepage
import sys
sys.path.append("./PyGithub")
from github import Github
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
repo = fetcher.get_repository()
homepage = Homepage(repo)

print(homepage.get_commits())


analyzer = RepoAnalyzer(repo)

# analyzer.weekly_code_frequency()
# analyzer.language_distribution()
# analyzer.weekly_commit_frequency()
# analyzer.top_contributors_monthly()