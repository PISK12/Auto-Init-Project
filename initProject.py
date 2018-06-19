from sys import platform as _platform
from sys import argv
from subprocess import call
from os import listdir, system
from urllib.request import urlopen


def download_txt(adres):
    return urlopen(adres).read()


def initGit(adres):
    print("Creation of Git")
    call(["git", "init", ])
    gitignore = download_txt(adres)
    with open(".gitignore", "wb") as f:
        f.write(gitignore)
    call(["git", "add", ".gitignore"])


def initPython():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore"
    VENV = "venv"
    requirements = ["icecream", ]

    print("Creation of virtual environments")
    call(["python", "-m", "venv", VENV])
    pip = r"{}\Scripts\pip".format(VENV)
    activate = r"{}\Scripts\activate".format(VENV)
    python = r"{}\Scripts\python".format(VENV)

    initGit(GITIGNORE)

    print("Install requirements")
    call([python, "-m", "pip", "install", "--upgrade", "pip"])
    if "requirements.txt" in listdir():
        call([pip, "install", "-r", "requirements.txt"])
    else:
        for module in requirements:
            call([pip, "install", "--no-cache-dir", module])
    system("{} freeze > requirements.txt".format(pip))

    with open("activate.bat", "w") as f:
        f.write(activate)


def initC():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/C.gitignore"
    initGit(GITIGNORE)


def initCpp():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/C%2B%2B.gitignore"
    initGit(GITIGNORE)


def initJava():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/Java.gitignore"
    initGit(GITIGNORE)


def main():
    dictFunction = {"python": initPython,
                    "java": initJava, "c": initC, "cpp": initCpp}
    if len(argv) == 1:
        print("run init python")
        initPython()

    elif argv[1].lower() in dictFunction:
        dictFunction[argv[1].lower()]()

    else:
        print(dictFunction)


if __name__ == '__main__':
    main()
