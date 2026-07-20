import math
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'bola_langit_kelima_sistem.png'
    fig, ax = plt.subplots(figsize=(6,6))
    circle = plt.Circle((0,0), 1, fill=False, color='k')
    ax.add_patch(circle)

    # equator
    ax.plot([-1,1],[0,0], color='C1', label='Ekuator')
    # horizon line (tilted)
    ax.plot([-1,1],[ -0.5,0.5], color='C2', linestyle='--', label='Horizon')
    # ecliptic tilted by obliquity
    ob = 23.5
    theta = [math.radians(t) for t in range(0,361)]
    xs = [math.cos(t) for t in theta]
    ys = [math.sin(t)*math.cos(math.radians(ob)) for t in theta]
    ax.plot(xs, ys, color='C3', label='Ekliptika (tilted)')

    ax.set_aspect('equal')
    ax.axis('off')
    fig.suptitle('Bola Langit: Lima Sistem Koordinat (schematic)')
    fig.savefig(out, dpi=150)


if __name__ == '__main__':
    main()
