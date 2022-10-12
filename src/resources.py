import os

f = {}

def getRootPath() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def resourcePath(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    joins = []
    newPath = relative_path
    while ('/' in newPath):
        loc = newPath.find('/')
        joins.append(newPath[0:loc])
        newPath = newPath[loc+1:]
    joins.append(newPath)

    PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    return os.path.join(PATH, *joins)