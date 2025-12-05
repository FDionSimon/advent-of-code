import importlib, os, requests

def which_folder(day, year):
    if int(day) < 10:
        project = "0" + day
    root = "AOC_" + year
    return root, project

def pull_input(day, year):
    print(f"Fetching input for day: {day}")

    # Call Prep --> env:SESSIONID is needed!
    session = os.getenv("SESSIONID")
    if session == 'None':
        print('Get your Session ID Token!')
        exit(1)

    headers = {'cookie': f'session={session}'}
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    # FIRE!
    response = requests.get(url, headers=headers)

    # Write input in Root, Easy to clean up as it should not be added to git
    with open(f'input.txt', 'w') as file:
        file.write(response.text)
    print("Done!")

def run_script(root, project):
    # Pulling script to root
    try:
        module = importlib.import_module(f"{root}.{project}.main")
        module.main()
    except ModuleNotFoundError as e:
        print(f"Folder {root}/{project} not found: {e}")
    except AttributeError as e:
        print(f"No main() function found: {e}")