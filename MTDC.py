import scipy
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

gt = \
    [3, 4, 11, 11, 18, 19, 19, 31, 31, 46, 45, 41, 46, 54, 54, 50, 54, 54, 56, 1, 2, 5, 4, 5, 14, 18, 21, 26, 39,
     42, 49, 51, 47, 51, 49, 49, 52, 52, 50, 49, 51, 55, 0, 0, 2, 3, 8, 39, 45, 52, 21, 25, 47, 45, 58, 58, 58, 71,
     68, 67, 67, 61, 58, 71, 69, 69, 68, 70, 65, 70, 68, 74, 79, 77, 77, 79, 78, 79, 80, 81, 81, 79, 1, 1, 1, 1, 1,
     1, 5, 6, 13, 13, 13, 14, 13, 22, 27, 35, 40, 41, 42, 39, 40, 42, 41, 44, 3, 3, 3, 3, 2, 2, 2, 2, 2, 6, 6, 7, 7,
     7, 10, 11, 12, 12, 13, 16, 15, 15, 20, 21, 19, 22, 20, 19, 20, 21, 21, 20, 21, 20, 19, 21, 21, 21, 22, 22, 22,
     22, 22, 22, 22, 10, 18, 25, 30, 32, 35, 36, 39, 42, 43, 44, 48, 2, 10, 28, 43, 56, 71, 92, 93, 97, 103, 103,
     107]

pd = \
    [4, 5, 11, 11, 19, 21, 23, 32, 31, 42, 40, 39, 42, 49, 48, 49, 52, 51, 53, 0, 0, 3, 3, 3, 17, 22, 18, 31, 41, 45,
     47, 52, 47, 51, 46, 49, 52, 51, 53, 54, 56, 57, 0, 0, 1, 2, 10, 39, 42, 43, 16, 19, 42, 49, 61, 56, 60, 75, 74, 69,
     67, 63, 60, 70, 72, 72, 70, 72, 73, 73, 67, 76, 77, 75, 75, 79, 75, 77, 75, 79, 79, 78, 1, 2, 1, 1, 1, 1, 2, 6, 11,
     11, 13, 12, 13, 18, 23, 38, 40, 41, 44, 43, 43, 50, 49, 45, 2, 3, 3, 3, 5, 3, 4, 7, 5, 7, 4, 3, 5, 10, 8, 10, 11,
     9, 15, 16, 14, 14, 18, 20, 17, 22, 21, 18, 15, 23, 14, 20, 20, 16, 19, 20, 23, 21, 22, 21, 24, 22, 23, 22, 22, 3,
     13, 20, 22, 18, 29, 32, 32, 29, 36, 28, 36, 3, 17, 32, 43, 41, 66, 79, 74, 74, 89, 85, 99]

pdv2 = \
    [4, 5, 11, 12, 21, 22, 23, 32, 32, 40, 40, 42, 43, 50, 49, 50, 56, 56, 56, 0, 0, 5, 2, 4, 17, 25, 20, 29, 43, 45,
     52, 54, 48, 53, 49, 53, 53, 55, 57, 56, 58, 60, 2, 0, 1, 3, 12, 40, 46, 45, 20, 23, 50, 51, 63, 60, 63, 72, 73, 72,
     69, 63, 62, 82, 75, 74, 76, 72, 70, 81, 71, 77, 79, 79, 74, 77, 79, 80, 76, 78, 83, 79, 1, 1, 1, 1, 1, 1, 5, 6, 12,
     13, 13, 13, 14, 20, 24, 42, 41, 45, 43, 46, 45, 50, 52, 50, 4, 5, 3, 5, 5, 4, 7, 5, 4, 10, 6, 3, 8, 10, 7, 10, 13,
     11, 15, 20, 21, 14, 23, 20, 18, 24, 21, 21, 23, 26, 22, 23, 27, 25, 25, 21, 23, 24, 23, 20, 25, 25, 24, 21, 24, 4,
     11, 9, 16, 20, 23, 22, 27, 29, 28, 25, 33, 4, 21, 31, 43, 46, 69, 70, 69, 87, 74, 71, 93]

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
    ww=list(range(25, upper+25, 25))
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

    plt.title('MTDC', fontsize=16)
    plt.ylabel('Prediction', fontsize=14)
    plt.xlabel('Ground Truth', fontsize=14)

    plt.tight_layout()
    plt.savefig('MTDC.png')
    # plt.show()


plot_r2(gt, pd, gt, pdv2)
