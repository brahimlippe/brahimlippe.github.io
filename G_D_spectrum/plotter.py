import matplotlib;
import matplotlib.pyplot as plt;
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
    xticks=np.arange(389, 8000, step=389)
    plt.xticks(xticks, labels=None, fontSize="xx-small")
    yticks=np.arange(-100, 0, step=15)
    plt.yticks(yticks, [i for i in yticks], fontSize="xx-small")
    plt.ylim(bottom=-100, top=-20)
    plt.grid(True, 'major', linewidth='1.5')
    plt.grid(True, 'minor')
    plt.gca().set_xlabel(arabic(u'حدة الصوت (هرتز)'))
    plt.gca().set_ylabel(arabic(u'شدة الصوت (دسيبال)'))
    plt.gca().get_yaxis().set_minor_locator(matplotlib.ticker.AutoMinorLocator(5))
    plt.gca().get_xaxis().grid(True, linestyle='--', linewidth='1')
    plt.plot(X, Y, ",-", color=color, linestyle='-', label=label, alpha=0.5)
    if not annotation:
        annotation = True
        plt.annotate(arabic(u"إئتلاف"), (X[1734], Y[1734]), arrowprops={"arrowstyle":"->"}, xytext=(X[1734]+1000, Y[1734]+10))
        plt.annotate(arabic(u"إئتلاف"), (X[3468], Y[3468]), arrowprops={"arrowstyle":"->"}, xytext=(X[3468]+1000, Y[3468]+10))
        plt.annotate(arabic(u"إئتلاف"), (X[5202], Y[5202]), arrowprops={"arrowstyle":"->"}, xytext=(X[5202]+1000, Y[5202]+10))
        plt.annotate(arabic(u"إئتلاف"), (X[6937], Y[6937]), arrowprops={"arrowstyle":"->"}, xytext=(X[6937]+1000, Y[6937]+10))
        plt.annotate(arabic(u"إئتلاف"), (X[8670], Y[8670]), arrowprops={"arrowstyle":"->"}, xytext=(X[8670]+1000, Y[8670]+10))
    plt.legend()

plot('violin_G_spectrum.txt', 'blue', arabic(u'نوى'))
plot('violin_D_spectrum.txt', 'magenta', arabic(u'محير'))
plt.savefig(os.path.dirname(os.path.realpath(__file__)) + '/plot.png')
