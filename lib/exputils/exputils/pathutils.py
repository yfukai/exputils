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

def get_abs_path(p):
    if path.isabs(p):
        return p
    else:
        return path.abspath(path.join(os.getcwd(),p))

def makedirs(p,check=False):
    if not check:
        if not os.path.exists(p):
            os.makedirs(p)
    else:
        os.makedirs(p)
