import math
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'segitiga_pzx.png'
    fig, ax = plt.subplots(figsize=(6,6))
    circle = plt.Circle((0,0), 1, fill=False, color='k')
    ax.add_patch(circle)

    # Points P (pole), Z (zenith), X (star)
    P = (0,1)
    Z = (0.5,0.2)
    X = (-0.6,-0.3)
    ax.plot(*P,'o'); ax.text(P[0]+0.03,P[1]+0.03,'P')
    ax.plot(*Z,'o'); ax.text(Z[0]+0.03,Z[1]+0.03,'Z')
    ax.plot(*X,'o'); ax.text(X[0]+0.03,X[1]+0.03,'X')

    # arcs representing sides
    ax.plot([P[0],Z[0]],[P[1],Z[1]], color='C1')
    ax.plot([Z[0],X[0]],[Z[1],X[1]], color='C1')
    ax.plot([X[0],P[0]],[X[1],P[1]], color='C1')

    ax.set_aspect('equal'); ax.axis('off')
    fig.suptitle('Segitiga Bola PZX (schematic)')
    fig.savefig(out, dpi=150)


if __name__ == '__main__':
    main()
