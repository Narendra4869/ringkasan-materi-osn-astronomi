from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'barycenter_bumi_bulan.png'
    fig, ax = plt.subplots(figsize=(6,3))
    # simple scale
    earth_pos = 0
    moon_pos = 10
    ax.scatter([earth_pos],[0], s=800, color='C0')
    ax.scatter([moon_pos],[0], s=200, color='C1')
    # barycenter
    bary = earth_pos + (1/81)*(moon_pos-earth_pos)
    ax.scatter([bary],[0], color='k')
    ax.text(earth_pos,0.2,'Earth'); ax.text(moon_pos,0.2,'Moon')
    ax.text(bary, -0.2, 'Barycenter')
    ax.set_ylim(-1,1); ax.axis('off')
    fig.suptitle('Barycenter Sistem Bumi-Bulan (schematic)')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
