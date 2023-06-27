import math
import numpy as np
from scipy.stats import norm
def PolicySigmoid(x):
    rc = 1
    sc = 1
    it = 0
    sm = 0
    while (it < rc * x.shape[0]):
        sm += (x[it] - 0.5)#l or nl
        it += 1
    sm *= sc
    prob = 1 / (1 + math.exp(-sm))
    return prob
def PolicyMissp(x):
    rc = 1
    sc = 1
    it = 0
    sm = 0
    while (it < rc * x.shape[0]):
        sm += (x[it] - 0.5)
        it += 1
    sm *= sc
    return norm.cdf(sm)
def PolicyInvRatio(x):
    rc = 1
    sc = 1.0
    it = 0
    sm = 0
    while (it < rc * x.shape[0]):
        sm += abs(x[it])
        it += 1
    sm *= (sc / (rc * x.shape[0]))
    return 1.0 / (1.25 + 3 * sm)
def PolicyLinear(x):
    sc = 1.0
    it = 0
    sm = 0
    tot = 0
    while (it < x.shape[0]):
        sc /= 2
        tot += sc
        sm += abs(x[it]) * sc
        it += 1
    return 1 - (sm + 0.1) / (tot + 0.2)
def PolicyNew(x, tp):
    if (tp == 0):
        return PolicyMissp(x)
    elif (tp == 1):
        return PolicySigmoid(x)
    elif (tp == 2):
        return PolicyInvRatio(x)
    elif (tp == 3):
        return PolicyLinear(x)
    elif (tp == 4):
        return 0.5
def RewardLinear(x, y):
    dlt = 0
    for i in range(x.shape[0]):
        if (i % 2 == 0):
            dlt += (i / 2 + y) * x[i]
    dlt += y
    return dlt
def RewardNonLinear(x, y):
    dlt = 0
    for i in range(x.shape[0]):
        if (i % 2 == 0):
            dlt += (i / 2 + y) * x[i]
    for i in range(x.shape[0] - 1):
        if (i % 10 == 0):
            dlt += (i / 10 + y) * (x[i] * x[i] + x[i] * x[i + 1])
    dlt += y
    return dlt
def Reward(x, y, tp):
    if (tp == 0):
        return RewardLinear(x, y)
    else:
        return RewardNonLinear(x, y)
def PolicyUniLinear(x):
    s1 = 0
    s2 = 0
    # for binary
    for i in range(x.shape[0]):
        s2 += x[i]
    return (s2 * 1.0 + 0.1) / (x.shape[0] + 1)

def PolicyTest(x, tp):
    if (tp == 0):
        return PolicyMissp(x)
    elif (tp == 1):
        return PolicySigmoid(x)
    elif (tp == 2):
        return PolicyInvRatio(x)
    elif (tp == 3):
        return PolicyLinear(x)
    elif (tp == 4):
        return 0.5
    elif (tp == 5):
        return PolicyUniLinear(x)

   