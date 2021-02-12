import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from bidi.algorithm import get_display
import arabic_reshaper
import os

def arabic(str):
    reshaped_text = arabic_reshaper.reshape(str)
    return get_display(reshaped_text)

def plot(filename, color, label):
    X, Y = [], []
    for line in open(filename, 'r'):
      values = [float(s) for s in line.split()]
      X.append(values[0])
      Y.append(values[1])

    plt.xlim(300, 8000)
    xticks=np.arange(389, 8000, step=389)
    plt.xticks(xticks, [i for i in xticks], fontSize="small")
    yticks=np.arange(-100, 0, step=15)
    plt.yticks(yticks, [i for i in yticks], fontSize="small")
    plt.ylim(bottom=-100, top=-20)
    plt.grid(True, 'major', linewidth='1.5')
    plt.grid(True, 'minor')
    plt.gca().set_xlabel(arabic(u'حدة الصوت (هرتز)'))
    plt.gca().set_ylabel(arabic(u'شدة الصوت (دسيبال)'))
    plt.gca().get_yaxis().set_minor_locator(matplotlib.ticker.AutoMinorLocator(5))
    plt.gca().get_xaxis().grid(True, linestyle='--', linewidth='1')
    plt.plot(X, Y,",-", color=color, label=label)
    plt.legend()

plt.figure(figsize=(13.0,6.0))
plot('violin_G_spectrum.txt', 'tab:blue', arabic(u'نوى'))
plt.savefig(os.path.dirname(os.path.realpath(__file__)) + '/violin_G_spectrum.png', transparent=True)
