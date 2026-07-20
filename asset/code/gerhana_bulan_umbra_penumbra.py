from pathlib import Path
import matplotlib.pyplot as plt


def main():
    out = Path(__file__).parent.parent / 'images' / 'gerhana_bulan_umbra_penumbra.png'
    fig, ax = plt.subplots(figsize=(8,3))
    # Sun (left), Earth (center large), Moon (right)
    ax.scatter(0,0,s=2000,color='orange')
    ax.scatter(4,0,s=1200,color='C0')
    ax.scatter(8,0,s=200,color='gray')
    # Earth's umbra cone
    ax.plot([4,8.5],[0.2,0.8], color='k')
    ax.plot([4,8.5],[-0.2,-0.8], color='k')
    ax.plot([4,7.5],[0.1,0.6], color='k', linestyle='--')
    ax.plot([4,7.5],[-0.1,-0.6], color='k', linestyle='--')
    ax.text(3.8,-0.6,'Earth'); ax.text(7.9,-0.6,'Moon'); ax.text(-0.5,0.6,'Sun')
    ax.axis('off')
    fig.suptitle('Geometri Gerhana Bulan — Umbra & Penumbra Bumi (schematic)')
    fig.savefig(out, dpi=150)


if __name__=='__main__':
    main()
