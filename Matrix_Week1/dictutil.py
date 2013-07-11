

## Task 2
def dict2list(dct, keylist):
    return [dct[key] for key in keylist]

## Task 3
def listrange2dict(L): return list2dict(L,range(len(L)))



def list2dict(L, keylist):
    return {k : v for (k, v) in zip(keylist, L)}


