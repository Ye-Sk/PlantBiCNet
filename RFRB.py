import scipy
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

gt = \
    [469, 120, 343, 119, 383, 330, 289, 629, 323, 549, 290, 471, 396, 247, 69, 141, 485, 227, 404, 265, 43, 255, 255,
     27]

pd = \
    [410, 127, 335, 108, 368, 371, 287, 573, 353, 601, 320, 486, 398, 301, 76, 184, 504, 231, 441, 281, 42, 197, 222,
     19]

pdv2 = \
    [390, 123, 334, 119, 351, 355, 290, 475, 354, 536, 313, 463, 380, 298, 87, 181, 460, 231, 432, 287, 39, 199, 217,
     16]


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
    ww = list(range(60, upper+60, 60))
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

    plt.title('RFRB', fontsize=16)
    plt.ylabel('Prediction', fontsize=14)
    plt.xlabel('Ground Truth', fontsize=14)

    plt.tight_layout()
    plt.savefig('RFRB.png')
    # plt.show()


plot_r2(gt, pd, gt, pdv2)
