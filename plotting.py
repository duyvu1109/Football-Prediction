import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def show1Chart(win, draw, lose):
    df = pd.DataFrame([['win','c1',win],['draw','c1',draw],['lose','c1',lose]],columns=['detail','season','val'])
    df.pivot("season", "detail", "val").plot(kind='bar')
    plt.show()



def showCharts(_win, _draw, _lose):
    x = np.arange(3)
    width = 0.2
    # plot data in grouped manner of bar type
    plt.bar(x-0.2, _win, width, color='cyan')
    plt.bar(x, _draw, width, color='orange')
    plt.bar(x+0.2, _lose, width, color='green')
    plt.xticks(x, ['21-22', '20-21', '19-20'])
    plt.xlabel("Season")
    plt.ylabel("Match")
    plt.legend(["WIN", "DRAW", "LOSE"])
    plt.show()