from sys import platform as _platform
from sys import argv
from subprocess import call
from os import listdir, system
from os.path import join
from urllib.request import urlopen

from icecream import ic


class Git:
    FILE_GITIGNORE = ".gitignore"
    FILE_GIT = ".git"

    def __init__(self, adres=""):
        if Git.FILE_GIT not in listdir():
            print("Creation of Git")
            call(["git", "init", ])
        self.adres = adres

    def commitGit(self):
        ic()
        print("commit Git")
        call(["git", "commit", "--all"])

    def addToGit(self, someThink):
        ic()
        print("Add to git {}".format(someThink))
        call(["git", "add", someThink])

    def addGitignore(self,):
        ic()
        if Git.FILE_GITIGNORE not in listdir():
            if self.adres:
                print("Download .gitignore")
                gitignore = urlopen(self.adres).read()
            else:
                print("Gitignore is empty")
                gitignore = ""
            with open(Git.FILE_GITIGNORE, "wb") as f:
                f.write(gitignore)
        self.addToGit(Git.FILE_GITIGNORE)

    def addToGitignore(self, someThink):
        ic()
        with open(Git.FILE_GITIGNORE, "ab") as f:
            f.write(str.encode(someThink))
        self.addToGit(Git.FILE_GITIGNORE)


def initPython():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore"
    VENV = "venv"
    FILE_REQUIREMENTS = "requirements.txt"

    requirements = ["icecream", "pyinstaller"]
    requirements = []

    if VENV not in listdir():
        print("Creation of virtual environments")
        call(["python", "-m", "venv", VENV])
    #pip = r"{}\Scripts\pip".format(VENV)
    pip = join(VENV, "Scripts", "pip")
    #activate = r"{}\Scripts\activate".format(VENV)
    activate = join(VENV, "Scripts", "activate")
    #python = r"{}\Scripts\python".format(VENV)
    python = join(VENV, "Scripts", "python")

    print("Install requirements")
    #call([python, "-m", "pip", "install", "--upgrade", "pip"])
    if "requirements.txt" in listdir():
        call([pip, "install", "-r", "requirements.txt"])
    else:
        for module in requirements:
            call([pip, "install", "--no-cache-dir", module])

    call([pip, "freeze", ">", FILE_REQUIREMENTS])

    with open("activate.bat", "w") as f:
        f.write(activate)

    git = Git(GITIGNORE)
    git.addToGit(FILE_REQUIREMENTS)
    git.addGitignore()
    git.addToGitignore("activate.bat")
    git.commitGit()


def initC():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/C.gitignore"
    git = Git(GITIGNORE)
    git.addGitignore()
    git.commitGit()


def initCpp():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/C%2B%2B.gitignore"
    git = Git(GITIGNORE)
    git.addGitignore()
    git.commitGit()


def initJava():
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/Java.gitignore"
    git = Git(GITIGNORE)
    git.addGitignore()
    git.commitGit()


def main():
    dictFunction = {"python": initPython,
                    "java": initJava, "c": initC, "cpp": initCpp}
    if len(argv) == 1:
        print("add some think like")
        for fun in dictFunction:
            print(fun)

    elif argv[1].lower() in dictFunction:
        dictFunction[argv[1].lower()]()
        ic()
        ic(argv)
        ic(argv[2])

    else:
        print(dictFunction)


if __name__ == '__main__':
    main()
