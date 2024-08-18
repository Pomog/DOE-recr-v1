import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data as a DataFrame with mock
data = {
    'Solvent Volume': [3, 3, 3, 6, 6, 6, 9, 9, 9],
    'Temperature': [-20, 2-8, -20, 2-8, -20, 2-8, -20, 2-8, -20],
    'Tartaric Acid': [0.5, 0.75, 1.0, 0.5, 0.75, 1.0, 0.5, 0.75, 1.0],
    'Yield': [45, 50, 55, 47, 52, 58, 63, 60, 65],
    'Chiral Purity': [85, 87, 90, 88, 91, 93, 84, 86, 89]  # Mock chiral purity data
}

# Data setup as previously described
df = pd.DataFrame(data)

# Prepare data for plotting
solvent_volume = df['Solvent Volume'].unique()
tartaric_acid = df['Tartaric Acid'].unique()
yield_percentage = df.pivot(index='Tartaric Acid', columns='Solvent Volume', values='Yield').values
chiral_purity = df.pivot(index='Tartaric Acid', columns='Solvent Volume', values='Chiral Purity').values

# Prepare data for contour plotting
X, Y = np.meshgrid(solvent_volume, tartaric_acid)
Z_yield = yield_percentage
Z_purity = chiral_purity

# Create contour plots
fig, axs = plt.subplots(1, 2, figsize=(16, 6))

# Contour plot for Yield
contour1 = axs[0].contourf(X, Y, Z_yield, cmap='viridis')
axs[0].set_xlabel('Solvent Volume (EtOH 96%)')
axs[0].set_ylabel('Tartaric Acid (equivalents)')
axs[0].set_title('Yield Contour Plot')
fig.colorbar(contour1, ax=axs[0], label='Yield (%)')

# Contour plot for Chiral Purity
contour2 = axs[1].contourf(X, Y, Z_purity, cmap='plasma')
axs[1].set_xlabel('Solvent Volume (EtOH 96%)')
axs[1].set_ylabel('Tartaric Acid (equivalents)')
axs[1].set_title('Chiral Purity Contour Plot')
fig.colorbar(contour2, ax=axs[1], label='Chiral Purity (%)')

plt.tight_layout()
plt.show()
