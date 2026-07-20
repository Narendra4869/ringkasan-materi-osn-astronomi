import math
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'tiga_anomali.png'
    a=1.0; e=0.5
    b = a*math.sqrt(1-e*e)
    fig, ax = plt.subplots(figsize=(6,4))
    thetas = [i*math.pi/180 for i in range(0,361)]
    xs = [a*math.cos(t) for t in thetas]
    ys = [b*math.sin(t) for t in thetas]
    ax.plot(xs, ys)
    # pick a point and project
    tpt = math.radians(50)
    xpt = a*math.cos(tpt); ypt = b*math.sin(tpt)
    ax.plot([xpt], [ypt], 'o')
    # projection to circle center
    ax.plot([xpt, xpt/a], [ypt, 0], '--', color='gray')
    ax.text(xpt+0.02, ypt+0.02, 'X (true anomaly f)')
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title('Tiga Anomali: E, f, M (schematic)')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
