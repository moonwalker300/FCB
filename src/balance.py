import numpy as np
import math

def Balance(x, avg_x, la = 1):
    n, m = x.shape
    w = np.ones([1, n]) / math.sqrt(n)
    iterNum = 30000
    absError = 0.00000000001
    lamd = la
    alpha = 10000
    lr = 0.5 / (math.sqrt(n) * np.max(abs(x)))
    Loss = []
    for i in range(iterNum):
        dw = 4 * np.dot(np.dot(w * w, x) - avg_x, x.T) * w + 4 * lamd * w * w * w #+ 4 * alpha * (np.sum(w * w) - 1) * w
        w -= lr * dw
        w /= math.sqrt(np.sum(w * w))
        tmp = np.dot(w * w, x) - avg_x
        tmpLoss = np.dot(tmp, tmp.T) + lamd * np.dot(w * w, (w * w).T)
        Loss.append((float)(tmpLoss))
        #if (i > 0):
            #if (abs(Loss[i - 1] - Loss[i]) < absError):
                #break
    return w * w, Loss