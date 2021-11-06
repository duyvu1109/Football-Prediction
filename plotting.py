import pandas as pd
import matplotlib.pyplot as plt

def show1Chart(win, draw, lose):
    df = pd.DataFrame([['win','c1',win],['draw','c1',draw],['lose','c1',lose]],columns=['detail','season','val'])
    df.pivot("season", "detail", "val").plot(kind='bar')
    plt.show()
