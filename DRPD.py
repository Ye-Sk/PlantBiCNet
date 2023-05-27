import scipy
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

gt = \
    [8, 10, 28, 25, 16, 18, 45, 34, 22, 9, 13, 10, 15, 15, 12, 18, 31, 22, 19, 14, 17, 7, 11, 26, 25, 19, 12, 8, 21, 13,
     31, 16, 11, 16, 27, 24, 14, 10, 31, 12, 21, 11, 15, 26, 12, 25, 16, 29, 30, 19, 7, 30, 14, 5, 31, 20, 26, 18, 16,
     37, 39, 22, 21, 25, 25, 20, 32, 22, 23, 16, 14, 19, 35, 23, 14, 26, 21, 23, 21, 20, 16, 27, 16, 17, 24, 14, 18, 19,
     21, 36, 28, 31, 16, 22, 20, 40, 21, 16, 19, 26, 31, 25, 20, 19, 21, 26, 24, 20, 20, 22, 22, 31, 26, 31, 36, 25, 30,
     25, 15, 33, 32, 29, 42, 27, 42, 33, 35, 24, 29, 31, 32, 30, 25, 20, 14, 26, 25, 26, 19, 23, 37, 29, 32, 24, 20, 23,
     27, 22, 27, 22, 21, 19, 30, 20, 22, 27, 31, 32, 17, 35, 20, 31, 22, 25, 23, 16, 21, 18, 28, 28, 19, 34, 22, 24, 25,
     18, 20, 13, 30, 25, 29, 26, 16, 22, 29, 22, 19, 16, 10, 24, 16, 22, 24, 16, 36, 23, 13, 35, 19, 25, 33, 26, 37, 32,
     32, 13, 27, 51, 43, 46, 9, 26, 25, 25, 40, 13, 28, 21, 38, 27]

pd = \
    [12, 11, 30, 26, 16, 18, 45, 39, 21, 11, 11, 8, 16, 11, 15, 21, 25, 17, 20, 13, 18, 8, 14, 27, 22, 25, 13, 8, 20,
     13, 33, 15, 11, 13, 31, 30, 14, 11, 34, 11, 22, 12, 15, 26, 17, 26, 14, 29, 30, 20, 6, 30, 17, 6, 35, 20, 27, 18,
     16, 38, 40, 24, 25, 26, 27, 22, 32, 21, 22, 16, 13, 20, 36, 25, 15, 21, 20, 24, 22, 20, 15, 28, 15, 18, 25, 14, 20,
     19, 22, 39, 27, 30, 15, 20, 19, 42, 20, 18, 19, 25, 31, 25, 16, 21, 20, 25, 24, 21, 21, 20, 22, 35, 26, 31, 34, 26,
     29, 24, 14, 32, 30, 27, 42, 33, 44, 32, 37, 23, 26, 30, 32, 29, 26, 21, 12, 25, 22, 24, 18, 22, 35, 30, 34, 21, 20,
     25, 29, 23, 27, 26, 22, 19, 30, 20, 21, 26, 30, 34, 17, 38, 20, 32, 21, 25, 22, 16, 20, 18, 28, 26, 17, 31, 23, 21,
     23, 21, 20, 12, 28, 22, 28, 25, 13, 26, 37, 17, 22, 19, 12, 24, 17, 21, 19, 20, 37, 26, 9, 33, 16, 21, 33, 27, 34,
     32, 29, 11, 24, 52, 39, 42, 10, 26, 27, 21, 35, 15, 28, 22, 35, 25]

pdv2 = \
    [11, 12, 26, 22, 16, 18, 40, 38, 23, 11, 14, 15, 19, 10, 9, 26, 20, 18, 16, 12, 15, 8, 12, 26, 22, 22, 12, 9, 19,
     12, 32, 13, 8, 11, 30, 29, 16, 13, 26, 9, 19, 11, 14, 27, 14, 25, 14, 28, 31, 18, 6, 30, 16, 6, 37, 20, 28, 19, 17,
     39, 39, 26, 23, 24, 26, 19, 30, 22, 23, 16, 15, 21, 35, 23, 15, 22, 20, 23, 24, 21, 14, 28, 17, 17, 27, 14, 22, 18,
     19, 37, 29, 29, 14, 21, 18, 41, 19, 15, 19, 26, 28, 25, 17, 18, 17, 22, 24, 20, 21, 20, 21, 33, 26, 28, 34, 23, 28,
     23, 15, 31, 31, 27, 40, 30, 42, 31, 35, 24, 26, 27, 30, 27, 26, 21, 13, 26, 21, 24, 17, 22, 32, 28, 34, 20, 19, 23,
     29, 25, 27, 20, 21, 17, 29, 20, 20, 24, 33, 30, 17, 34, 17, 28, 22, 23, 22, 16, 20, 18, 21, 23, 17, 35, 22, 22, 24,
     19, 22, 10, 30, 24, 32, 24, 14, 28, 32, 22, 19, 16, 10, 22, 16, 21, 19, 17, 34, 26, 9, 36, 20, 20, 32, 26, 35, 30,
     23, 11, 29, 52, 42, 42, 10, 26, 24, 22, 37, 15, 27, 24, 36, 27]


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
    ww=list(range(1, upper+25, 25))
    ww = np.array(ww).reshape(-1, 1)
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

    plt.title('DRPD', fontsize=16)
    plt.ylabel('Prediction', fontsize=14)
    plt.xlabel('Ground Truth', fontsize=14)

    plt.tight_layout()
    plt.savefig('DRPD.png')
    # plt.show()


plot_r2(gt, pd, gt, pdv2)
