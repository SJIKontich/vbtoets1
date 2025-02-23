# python
import os

# Check if the current branch is 'mijn-oplossingen'
current_branch = os.popen("git branch --show-current").read().strip()
if current_branch == "main":
    # als de branch nog niet bestaat, maak hem aan
    branches = os.popen("git branch --list").read().split()
    if "mijn-oplossingen" not in branches:
        os.system("git checkout -b mijn-oplossingen")
    else:
        os.system("git checkout mijn-oplossingen")
    current_branch = os.popen("git branch --show-current").read().strip()
if current_branch == "mijn-oplossingen":
    os.system("git add .")
    os.system("git commit -m 'commit mijn oplossingen en switch naar alle oplossingen'")
    os.system("git checkout oplossing")