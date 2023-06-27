import numpy as np
from method import PolicyTest, Reward
import sys

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
nn = 1000
oldpolicy = 0
noise = 0.1
rewardnoise = 3
rc = 0
if (len(sys.argv) == 2):
    nn = (int)(sys.argv[1])
elif (len(sys.argv) == 3):
    nn = (int)(sys.argv[1])
    oldpolicy = (int)(sys.argv[2])
elif (len(sys.argv) == 4):
    nn = (int)(sys.argv[1])
    oldpolicy = (int)(sys.argv[2])
    noise = (float)(sys.argv[3])
elif (len(sys.argv) == 5):
    nn = (int)(sys.argv[1])
    oldpolicy = (int)(sys.argv[2])
    noise = (float)(sys.argv[3])
    rewardnoise = (float)(sys.argv[4])
elif (len(sys.argv) == 6):
    nn = (int)(sys.argv[1])
    oldpolicy = (int)(sys.argv[2])
    noise = (float)(sys.argv[3])
    rewardnoise = (float)(sys.argv[4])
    rc = (int)(sys.argv[5])
xlist = np.random.choice(n, nn, False)
ff = open('data.txt', 'w')
ff.write('%d %d\n' % (nn, m))
for i in range(nn):
    for j in range(m):
        if j > 0:
            ff.write(' ')
        ff.write('%f' % x[xlist[i]][j])
    ff.write('\n')

for i in range(nn):
    prob = PolicyTest(x[xlist[i]], oldpolicy) + np.random.normal(scale=noise)
    if (prob < 0.001):
        prob = 0.001
    elif (prob > 0.999):
        prob = 0.999
    y = np.random.binomial(1, prob)
    r = Reward(x[xlist[i]], y, rc) + np.random.normal(scale=rewardnoise)
    ff.write('%d %f\n' % (y, r))

ff.close()