import numpy as np

hi=np.array([1,2])
def do_this(li,a):
    if a==6:
        return np.append(li,8)
    else:
        return li
print(hi)
hi=do_this(hi, 7)
print(hi)
hi=do_this(hi,6)
print(hi)
print(np.linspace(0,10,11))