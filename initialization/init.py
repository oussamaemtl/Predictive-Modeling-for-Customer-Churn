import os
import pathlib


def init_project():
    os.system('cmd /c "pip install pipenv"')
    os.system('cmd /c "pipenv install -r requirements.txt"')


if __name__ == "__main__":
    init_project()
