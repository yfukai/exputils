import itertools

def iget(it,index):
    return itertools.islice(it,index,index+1).next()
