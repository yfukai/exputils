import os
import os.path as path

def getfiles(path,extension=None):
    if not os.path.isdir(path):
        raise StandardError("not valid dir")
    files = []
    for f in os.listdir(path):
        if extension == None or f.endswith(extension):
            files.append(f)
    return files

