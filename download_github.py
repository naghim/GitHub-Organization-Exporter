import json
import os
import subprocess
import requests

with open('github.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

for i, org in enumerate(config):
    print(f'{i + 1}. {org["organization"]}')

org = config[int(input('Please choose an organization: ')) - 1]
token = org['token']
org_name = org['organization']
headers = {'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {token}', 'X-GitHub-Api-Version': '2022-11-28'}

page = 1
repos = []

while True:
    print(f'Requesting page {page}...')

    repo_link = f'https://api.github.com/orgs/{org_name}/repos?per_page=100&page={page}'
    current_repos = requests.get(repo_link, headers=headers).json()

    repos.extend(current_repos)

    if (not current_repos) or len(current_repos) != 100:
        break

    page += 1

folder = f'repositories-{org_name}'

if not os.path.exists(folder):
    os.makedirs(folder)

os.chdir(folder)

for repo in repos:
    name = repo['name']

    if os.path.exists(name):
        continue

    link = repo['html_url']
    subprocess.call(['git', 'clone', link])