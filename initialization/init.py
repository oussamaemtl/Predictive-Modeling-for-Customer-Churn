import os
def init_project():
    print(os.getcwd())
    os.system('cmd /c "cd .."')
    os.system('cmd /c "pip install pipenv"')
    os.system('cmd /c "pipenv install -r requirements.txt"')


if __name__ == "__main__":
    init_project()
