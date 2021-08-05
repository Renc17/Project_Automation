# Project Initialization Automation

Run the script on your terminal and initialize a new project with a readme locally in /Documents/MyProjects and
remotely on your GitHub account create a new repository with the same name (using GitHub API) then push first commit (README).

## Install
```bash
git clone https://github.com/Renc17/Project_Automation.git
cd Project_Automation

intall requirements below
```

## Requirements
Inside your cloned repo run :
```bash
pip install python-dotenv
python -m pip install requests
```

## How to
1. Create a Personal Token on your GitHub account
2. Create a .env file in your cloned repo
3. Add your personal token as:

```bash
PERSONAL_ACCESS_TOKEN=Your-Personal-Token
```
4. Run
```bash
./init-project.sh <your project name>
```
