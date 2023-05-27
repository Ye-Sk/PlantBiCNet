import scipy
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

gt = \
    [2, 16, 20, 3, 20, 5, 5, 13, 4, 29, 13, 4, 16, 5, 11, 6, 9, 13, 17, 18, 18, 7, 10, 8, 18, 21, 23, 10, 23, 6]

pd = \
    [1, 19, 19, 3, 27, 11, 5, 15, 3, 25, 13, 4, 15, 5, 13, 10, 15, 12, 16, 15, 17, 9, 9, 8, 16, 16, 20, 18, 25, 6]

pdv2 = \
    [2, 19, 21, 1, 27, 8, 3, 12, 2, 27, 8, 0, 14, 4, 13, 9, 11, 8, 18, 16, 14, 8, 9, 5, 17, 15, 19, 18, 19, 6]


def rsquared(pd, gt):
    """ Return R^2 where x and y are array-like."""
    pd, gt = np.array(pd), np.array(gt)
    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(pd, gt)
    return r_value**2


def plot_r2(gt, pd, gtv2, pdv2):

    r2 = rsquared(pd,gt)
    r2v2 = rsquared(pdv2,gtv2)

    pd, gt = np.array(pd).reshape(-1, 1), np.array(gt).reshape(-1, 1)
    pdv2, gtv2 = np.array(pdv2).reshape(-1, 1), np.array(gtv2).reshape(-1, 1)

    upper = int(max(max(pd), max(gt)))
    lower = int(min(max(pd), min(gt)))
    ww=list(range(lower, upper+5, 3))
    ww = np.array(ww).reshape(-1, 1)
    # ww = np.append(ww, [[101]], axis=0)
    LR=linear_model.LinearRegression()
    LR.fit(gt,pd)
    predictions = LR.predict(ww)

    LRv2=linear_model.LinearRegression()
    LRv2.fit(gtv2, pdv2)
    predictionsv2 = LRv2.predict(ww)

    cv1 = np.array([255, 94, 0]) / 255.
    cv2 = 'c'

    plt.figure(dpi=300)
    plt.ylim(min(ww), max(ww))
    plt.xlim(min(ww), max(ww))

    # point
    plt.plot(ww, predictions, color=cv1)
    plt.plot(ww, predictionsv2, color=cv2, linestyle='--')
    plt.scatter(gt, pd, color=cv1, marker = '.', alpha=0.5, edgecolors='none', s=40)
    plt.scatter(gtv2, pdv2, color=cv2, marker = '^', alpha=0.8, edgecolors='none', s=15)

    # plt.plot(ww, ww, color='black',  linestyle=':') # baseline

    legend = plt.legend(labels=(r"PlantBiCNet: $R^2={0:.4f}$".format(r2),
                       r"PlantBiCNet-Lite: $R^2={0:.4f}$".format(r2v2)),
               loc=(0.04, 0.77),
               fancybox=True, borderpad=0.8, fontsize=11, labelspacing=0.65)

    for line in legend.get_lines():
        line.set_linewidth(2)

    plt.title('CBD', fontsize=16)
    plt.ylabel('Prediction', fontsize=14)
    plt.xlabel('Ground Truth', fontsize=14)

    plt.tight_layout()
    plt.savefig('CBD.png')
    # plt.show()


plot_r2(gt, pd, gt, pdv2)
