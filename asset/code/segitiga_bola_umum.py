import math
from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'segitiga_bola_umum.png'
    fig, ax = plt.subplots(figsize=(6,6))
    circle = plt.Circle((0,0), 1, fill=False, color='k')
    ax.add_patch(circle)

    # three points on the circle
    angles = [30, 160, 280]
    pts = [(math.cos(math.radians(a)), math.sin(math.radians(a))) for a in angles]
    labels = ['A', 'B', 'C']
    for p,l,a in zip(pts, labels, angles):
        ax.plot(p[0], p[1], 'o', color='C0')
        ax.text(p[0]*1.08, p[1]*1.08, l)

    # draw great-circle arcs (as straight circular arcs approximated)
    for i in range(3):
        a1 = angles[i]
        a2 = angles[(i+1)%3]
        theta = list(range(int(a1), int(a2), 1)) if a2>a1 else list(range(int(a1), int(a2+360),1))
        xs = [math.cos(math.radians(t%360)) for t in theta]
        ys = [math.sin(math.radians(t%360)) for t in theta]
        ax.plot(xs, ys, color='C1')

    ax.set_aspect('equal')
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)
    ax.axis('off')
    fig.suptitle('Segitiga Bola Umum')
    fig.savefig(out, dpi=150)


if __name__ == '__main__':
    main()
