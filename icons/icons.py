import matplotlib.pyplot as plt

def create_posizionamento_svg():
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.6, color='lightblue'))  # Mappa
    ax.add_patch(plt.Circle((0.5, 0.4), 0.05, color='red'))  # Segnaposto
    ax.annotate('', xy=(0.5, 0.1), xytext=(0.5, 0.4),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))  # Freccia
    ax.text(0.1, 0.85, 'Posizionamento di Mercato', fontsize=10, color='black')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.savefig('posizionamento.svg', format='svg')
    plt.close()

create_posizionamento_svg()
