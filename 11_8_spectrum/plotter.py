import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from bidi.algorithm import get_display
import arabic_reshaper
import os

def arabic(str):
    reshaped_text = arabic_reshaper.reshape(str)
    return get_display(reshaped_text)

annotation = False
def plot(filename, color, label):
    global annotation
    X, Y = [], []
    for line in open(filename, 'r'):
      values = [float(s) for s in line.split()]
      X.append(values[0])
      Y.append(values[1])

    plt.xlim(right=8000)
    xticks=np.arange(291, 8000, step=291*2)
    plt.xticks(xticks, labels=None, fontSize="xx-small")
    yticks=np.arange(-100, 0, step=15)
    plt.yticks(yticks, [i for i in yticks], fontSize="xx-small")
    plt.ylim(bottom=-100, top=-20)
    plt.grid(True, 'major', linewidth='1.5')
    plt.grid(True, 'minor')
    plt.gca().set_xlabel(arabic(u'حدة الصوت (هرتز)'))
    plt.gca().set_ylabel(arabic(u'شدة الصوت (دسيبال)'))
    plt.gca().get_yaxis().set_minor_locator(matplotlib.ticker.AutoMinorLocator(5))
    plt.gca().get_xaxis().set_minor_locator(matplotlib.ticker.AutoMinorLocator(2))
    plt.gca().get_xaxis().grid(True, linestyle='--', linewidth='1')
    plt.plot(X, Y, ",-", color=color, linestyle='-', label=label, alpha=0.5)
    if not annotation:
        annotation = True
        plt.annotate(arabic(u"الإضطراب الأول"), (X[892], Y[892]), arrowprops={"arrowstyle":"->"}, xytext=(X[892]-1000, Y[892]+10))
        plt.annotate(arabic(u"الإضطراب الثاني"), (X[1487], Y[1487]), arrowprops={"arrowstyle":"->"}, xytext=(X[1487]+10, Y[1487]+5))
        plt.annotate(arabic(u"إئتلاف 11/8"), (X[2381], Y[2381]), arrowprops={"arrowstyle":"->"}, xytext=(X[2381]+10, Y[2381]+10))
    plt.legend()

plt.figure(figsize=(13.0,6.0))
plot('D_11_8_spectrum.txt', 'magenta', arabic(u'جهاركاه راست دوكاه'))
plot('violin_D_spectrum.txt', 'blue', arabic(u'دوكاه'))
plt.savefig(os.path.dirname(os.path.realpath(__file__)) + '/plot.png', transparent=True)
