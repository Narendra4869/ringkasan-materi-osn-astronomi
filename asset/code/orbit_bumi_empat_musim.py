import math
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'orbit_bumi_empat_musim.png'
    fig, ax = plt.subplots(figsize=(8,5))
    # Sun at origin
    ax.scatter(0,0, s=800, color='orange', label='Sun')
    # circular orbit
    th = [math.radians(t) for t in range(0,361)]
    xs = [math.cos(t) for t in th]
    ys = [math.sin(t) for t in th]
    ax.plot(xs, ys, color='C0')

    # four positions
    months = ['Mar (Vernal)','Jun (Summer)','Sep (Autumn)','Dec (Winter)']
    angles = [0, 90, 180, 270]
    for a,m in zip(angles, months):
        x = math.cos(math.radians(a))
        y = math.sin(math.radians(a))
        ax.plot(x,y,'o'); ax.text(x*1.05, y*1.05, m)

    ax.set_aspect('equal'); ax.axis('off')
    fig.suptitle('Orbit Bumi dengan 4 Titik Musim (schematic)')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
