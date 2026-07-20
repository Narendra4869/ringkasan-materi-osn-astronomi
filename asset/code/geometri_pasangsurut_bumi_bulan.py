from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'geometri_pasangsurut_bumi_bulan.png'
    fig, ax = plt.subplots(figsize=(6,3))
    # Earth
    circle = plt.Circle((0,0),1,fill=False)
    ax.add_patch(circle)
    # bulges
    ax.plot([1,1.5],[0,0],color='C1',linewidth=6,alpha=0.4)
    ax.plot([-1,-1.5],[0,0],color='C1',linewidth=6,alpha=0.4)
    ax.scatter([3],[0],s=80,color='C2')
    ax.text(3,0.2,'Moon')
    ax.axis('equal'); ax.axis('off')
    fig.suptitle('Geometri Gaya Pasang Surut Bumi-Bulan (schematic)')
    fig.savefig(out,dpi=150)


if __name__=='__main__':
    main()
