from pathlib import Path
import sys
import os
import requests
import json
from dotenv import load_dotenv


def init_project(params):
    # CREATE DIR
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    else:
        print("Project already exists")
        exit()

    # CREATE README
    readme_path = os.path.join(path, "README.md")
    readme = open(readme_path, "w")
    readme.write("# " + params)
    readme.close()

    # PREPARE REQUEST
    automation_path = os.getcwd()
    load_dotenv(os.path.join(automation_path, '.env'))
    PERSONAL_ACCESS_TOKEN = os.getenv("PERSONAL_ACCESS_TOKEN")

    baseURL = 'https://api.github.com/'
    url = 'user/repos'
    headers = {
        "Authorization": "token " + PERSONAL_ACCESS_TOKEN,
        "Accept"       : "application/vnd.github.v3+json"
    }
    data = {
        'name': project_name,
        'private': True
    }

    # MAKE API REQUEST
    response = requests.post(baseURL+url, data=json.dumps(data), headers=headers)
    json_data = json.loads(response.text)

    f = open(".env", "a")
    f.write("\nCLONE_URL="+json_data['clone_url'])
    f.write("\nWORKING_DIR=" + path)
    f.close()


if __name__ == '__main__':
    project_name = sys.argv[1]
    path = str(Path.home()) + "/Documents/MyProjects/" + project_name

    init_project(project_name)
