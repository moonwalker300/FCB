import numpy as np
import sys
from method import Reward, PolicyNew, PolicyTest
from balance import Balance
from sklearn.linear_model.logistic import LogisticRegression

n = 0
m = 0
x = np.zeros([1,1])
y = np.zeros(1)
reward = np.zeros(1)

oldpolicy = 5
newpolicy = 1
rkind = 0
if (len(sys.argv) == 2):
    newpolicy = (int)(sys.argv[1])
elif (len(sys.argv) == 3):
    oldpolicy = (int)(sys.argv[1])
    newpolicy = (int)(sys.argv[2])
elif (len(sys.argv) == 4):
    oldpolicy = (int)(sys.argv[1])
    newpolicy = (int)(sys.argv[2])
    rkind = (int)(sys.argv[3])

with open('data.txt') as f:
    titleflag = True
    cnt = 0
    for line in f:
        t = line[:-1].split(' ')
        if titleflag:
            titleflag = False
            n = int(t[0])
            m = int(t[1])
            x = np.zeros([n, m])
            y = np.zeros(n)
            reward = np.zeros(n)
        else:
            if (cnt < n):
                x[cnt] = map(lambda x:float(x), t)
            elif (cnt < 2 * n):
                y[cnt - n] = int(t[0])
                reward[cnt - n] = (float)(t[1])
            cnt += 1
    x_t = x[y == 1]
    x_c = x[y == 0]
    avg_x = np.mean(x, axis=0)
    w_t = np.zeros(x_t.shape)
    w_c = np.zeros(x_c.shape)

    r_t = reward[y == 1]
    r_c = reward[y == 0]

    xfort = x.copy()
    xforc = x.copy()
    for i in range(x.shape[0]):
        xfort[i] = PolicyNew(x[i], newpolicy) * x[i]
        xforc[i] = (1 - PolicyNew(x[i], newpolicy)) * x[i]
    x_t_cal = x_t.copy()
    x_c_cal = x_c.copy()
    for i in range(x_t.shape[0]):
        x_t_cal[i] = PolicyNew(x_t[i], newpolicy) * x_t[i]
    for i in range(x_c.shape[0]):
        x_c_cal[i] = (1 - PolicyNew(x_c[i], newpolicy)) * x_c[i]
    avg_xt = np.mean(xfort, axis=0)
    avg_xc = np.mean(xforc, axis=0)
    w_t, Loss_t = Balance(x_t_cal, avg_xt)
    w_c, Loss_c = Balance(x_c_cal, avg_xc)
    w_t = np.squeeze(w_t)
    w_c = np.squeeze(w_c)
    newans = 0
    varlist = []
    for i in range(w_t.shape[0]):
        newans += w_t[i] * r_t[i] * PolicyNew(x_t[i], newpolicy)
        varlist.append(r_t[i] * PolicyNew(x_t[i], newpolicy))
    for i in range(w_c.shape[0]):
        newans += w_c[i] * r_c[i] * (1 - PolicyNew(x_c[i], newpolicy))
        varlist.append(r_c[i] * (1 - PolicyNew(x_c[i], newpolicy)))
    print 'Utility:', newans
