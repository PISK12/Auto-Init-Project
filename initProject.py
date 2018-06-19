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
        print("commit Git")
        call(["git", "commit", "--all"])

    def addToGit(self, someThink):
        print("Add to git {}".format(someThink))
        call(["git", "add", someThink])

    def addGitignore(self,):
        if Git.FILE_GITIGNORE not in listdir():
            if self.adres:
                print("Download .gitignore")
                gitignore = urlopen(self.adres).read()
            else:
                print("Gitignore is empty")
                gitignore = ""
            with open(Git.FILE_GITIGNORE, "wb") as f:
                f.write(gitignore)
                f.write(str.encode("\n"))
        self.addToGit(Git.FILE_GITIGNORE)

    def addToGitignore(self, someThink):
        with open(Git.FILE_GITIGNORE, "ab") as f:
            f.write(str.encode(someThink + "\n"))
        self.addToGit(Git.FILE_GITIGNORE)


def initPython(argv):
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore"
    VENV = "venv"
    FILE_REQUIREMENTS = "requirements.txt"

    requirements = ["icecream", "pyinstaller"]

    if VENV not in listdir():
        print("Creation of virtual environments")
        call(["python", "-m", "venv", VENV])

    pip = join(VENV, "Scripts", "pip")
    activate = join(VENV, "Scripts", "activate")
    python = join(VENV, "Scripts", "python")

    print("Install requirements")
    call([python, "-m", "pip", "install", "--upgrade", "pip"])
    if "requirements.txt" in listdir():
        call([pip, "install", "-r", "requirements.txt"])
    else:
        for module in requirements:
            call([pip, "install", "--no-cache-dir", module])

    system("{} freeze > {}".format(pip, FILE_REQUIREMENTS))

    with open("activate.bat", "w") as f:
        f.write(activate)

    git = Git(GITIGNORE)
    git.addToGit(FILE_REQUIREMENTS)
    git.addGitignore()
    git.addToGitignore("activate.bat")
    git.commitGit()


def initC(argv):
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/C.gitignore"
    git = Git(GITIGNORE)
    git.addGitignore()
    git.commitGit()


def initCpp(argv):
    ic(argv)
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/C%2B%2B.gitignore"
    git = Git(GITIGNORE)
    git.addGitignore()
    git.commitGit()


def initJava(argv):
    GITIGNORE = "https://raw.githubusercontent.com/github/gitignore/master/Java.gitignore"
    git = Git(GITIGNORE)
    git.addGitignore()
    git.commitGit()


def help(argv):
    if not argv:
        for func in dictFunction:
            print(func)


dictFunction = {"python": initPython,
                "java": initJava, "c": initC, "cpp": initCpp}


def main():
    if len(argv) == 1:
        print("add some think like")
        help()

    elif argv[1].lower() in dictFunction:
        dictFunction[argv[1].lower()](argv[2:])

    else:
        print(dictFunction)


if __name__ == '__main__':
    main()
