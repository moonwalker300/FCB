import numpy as np
import sys
from method import RewardLinear, PolicyTest

if (len(sys.argv) == 4):
    n = (int)(sys.argv[1])
    m = (int)(sys.argv[2])
    if (sys.argv[3] == 'b'):
        x = np.random.randint(2, size=[n, m])
    else:
        x = np.random.normal(size=[n, m])
else:
    n = 500000
    m = 50
    x = np.random.randint(2, size=[n, m])
    #x = np.random.normal(size=[n, m])
f = open('featuredata.txt', 'w')
f.write('%d %d\n' % (n, m))
for i in range(n):
    for j in range(m):
        if j > 0:
            f.write(' ')
        f.write('%f' % x[i][j])
    f.write('\n')
f.close()
ff = open('Dimension' + str(m) + '.txt', 'w')
for i in range(n):
    for j in range(m):
        if j > 0:
            ff.write(' ')
        ff.write('%f' % x[i][j])
    ff.write('\n')
ff.close()
'''
for i in range(n):
    prob = PolicyTest(x[i])
    y = np.random.binomial(1, prob)
    r = RewardLinear(x[i], y)
    f.write('%d %f\n' % (y, r))
'''

