import matplotlib;
import matplotlib.pyplot as plt;
import numpy as np
import matplotlib
from bidi.algorithm import get_display
import arabic_reshaper
import os, math

def arabic(str):
    reshaped_text = arabic_reshaper.reshape(str)
    return get_display(reshaped_text)

def dist(x):
    return 12*math.log(x)/math.log(2)

dhil = [dist(1), dist(9.0/8), dist(1.25), dist(4.0/3), dist(1.5), dist(5.0/3), dist(15/8.), dist(2)]
equal_scale = [0, 2, 4, 5, 7, 9, 11, 12]
plt.figure(figsize=[7, 2])
plt.hlines(1,0,12)  # Draw a horizontal line
plt.plot(dhil, np.ones(np.shape(dhil)),'|',ms = 10)
yannotation_margin = 0.02
for i, txt in zip(equal_scale, [arabic("دو"), arabic("ري"), arabic("مي"), arabic("فا"), arabic("صول"), arabic("لا"), arabic("سي"), arabic("دو")]):
    plt.annotate(txt, (0, 1), xytext=(i-0.1, 1-yannotation_margin), color='magenta')
for i, txt in zip(dhil, [arabic("راست"), arabic("دوكاه"), arabic("سيكاه"), arabic("جهركاه"), arabic("نوى"), arabic("حسيني"), arabic("ماهور"), arabic("كردان")]):
    plt.annotate(txt, (0, 1), xytext=(i-0.1, 1+yannotation_margin), color='blue')
plt.plot(equal_scale, np.ones(np.shape(equal_scale)),'|',ms = 10, color='magenta')
plt.axis('off')
plt.savefig(os.path.dirname(os.path.realpath(__file__)) + '/plot.png')
