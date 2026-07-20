import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'kurva_analemma.png'
    t = np.linspace(0, 2*np.pi, 400)
    # simple parametric approx for figure-eight analemma
    x = np.sin(t*2) * 0.6
    y = 0.5*np.sin(t) + 0.1*np.cos(t*2)
    fig, ax = plt.subplots(figsize=(5,7))
    ax.plot(x,y,'-')
    ax.scatter(x[0],y[0], color='red')
    ax.set_title('Kurva Analemma (schematic)')
    ax.axis('off')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
