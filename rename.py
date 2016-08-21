import os
path = '/Volumes/Macintosh HD/Users/ray_liu/Documents/movie/series/ts/'
nms = os.listdir(path)
ansming = []
for s in nms:
    if s.startswith('.')==False:
        ansming.append(s)
ansming = sorted(ansming)
with open('names.txt','w') as of:
    for s in ansming:
        of.write(s+'\n')