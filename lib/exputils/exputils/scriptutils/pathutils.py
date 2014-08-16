import os
import os.path as path

def getfiles(directory,extension=None):
    if not os.path.isdir(directory):
        raise StandardError("not valid dir")
    files = []
    for f in os.listdir(directory):
        if extension == None or f.endswith(extension):
            files.append(path.abspath(path.join(directory,f)))
    return files

