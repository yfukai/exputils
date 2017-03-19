import itertools

def iget(it,index):
    return itertools.islice(it,index,index+1).next()

def skip_comment(f, commentstart="#"):
    return itertools.ifilter(lambda row : row[0] != commentstart, f)
