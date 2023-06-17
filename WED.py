import scipy
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

gt = \
    [104, 95, 116, 116, 92, 113, 119, 113, 133, 134, 132, 127, 105, 117, 118, 148, 96, 107, 111, 117, 102, 101, 156,
     164, 180, 190, 110, 131, 208, 191, 121, 137, 163, 142, 145, 160, 120, 120, 146, 117, 118, 130, 139, 86, 92, 155,
     148, 96, 106, 106, 117, 119, 123, 177, 211, 171, 171, 132, 125, 127, 117, 127, 134, 217, 235, 129, 138, 181, 192,
     125, 122]

pd = \
    [108, 104, 119, 122, 87, 110, 111, 119, 134, 139, 128, 123, 105, 124, 126, 155, 108, 106, 110, 123, 90, 106, 166,
     173, 173, 188, 117, 134, 209, 190, 127, 145, 159, 142, 139, 160, 117, 128, 135, 118, 122, 135, 147, 90, 93, 157,
     144, 101, 104, 107, 128, 122, 118, 179, 206, 174, 172, 140, 130, 131, 123, 128, 138, 215, 228, 133, 122, 170, 174,
     109, 114]

pdv2 = \
    [112, 101, 118, 117, 92, 110, 116, 110, 134, 132, 122, 123, 114, 130, 122, 155, 106, 107, 113, 127, 90, 105,
     162, 162, 179, 178, 116, 124, 216, 179, 124, 150, 156, 137, 145, 152, 127, 133, 148, 117, 123, 136, 141, 88,
     95, 160, 142, 100, 109, 107, 131, 129, 116, 186, 214, 171, 174, 136, 128, 133, 125, 133, 151, 227, 236, 132,
     124, 169, 167, 115, 123]


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

    plt.title('WED', fontsize=16)
    plt.ylabel('Prediction', fontsize=14)
    plt.xlabel('Ground Truth', fontsize=14)

    plt.yticks(np.arange(50, upper, 25)[1:])
    plt.xticks(np.arange(50, upper, 25)[1:])

    plt.tight_layout()
    plt.savefig('WED.png')
    # plt.show()


plot_r2(gt, pd, gt, pdv2)
