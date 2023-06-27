import numpy as np
import sys
from method import Reward, PolicyNew, PolicyTest
newpolicy = 0
rkind = 0
if (len(sys.argv) == 2):
    newpolicy = (int)(sys.argv[1])
elif (len(sys.argv) == 3):
    newpolicy = (int)(sys.argv[1])
    rkind = (int)(sys.argv[2])
n = 0
m = 0
x = np.zeros([1,1])
with open('featuredata.txt') as f:
    titleflag = True
    cnt = 0
    for line in f:
        t = line[:-1].split(' ')
        if titleflag:
            titleflag = False
            n = int(t[0])
            m = int(t[1])
            x = np.zeros([n, m])
        else:
            if (cnt < n):
                x[cnt] = map(lambda x:float(x), t)
            cnt += 1
gdtruth = 0
for i in range(x.shape[0]):
    gdtruth += (Reward(x[i], 1, rkind) * PolicyNew(x[i], newpolicy) + Reward(x[i], 0, rkind) * (1 - PolicyNew(x[i], newpolicy)))
print gdtruth / x.shape[0]