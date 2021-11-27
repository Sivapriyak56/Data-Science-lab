from collections import Counter

def wd_c(fname):
    with open(fname) as f:
        return Counter(f.read().split())
print("number: ",wd_c("text.txt"))