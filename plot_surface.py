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

df = pd.DataFrame(data)

# Prepare data for plotting
solvent_volume = df['Solvent Volume'].unique()
tartaric_acid = df['Tartaric Acid'].unique()
yield_percentage = df.pivot(index='Tartaric Acid', columns='Solvent Volume', values='Yield').values
chiral_purity = df.pivot(index='Tartaric Acid', columns='Solvent Volume', values='Chiral Purity').values

X, Y = np.meshgrid(solvent_volume, tartaric_acid)
Z_yield = yield_percentage
Z_purity = chiral_purity

# Create a 3D surface plot for Yield
fig = plt.figure(figsize=(16, 8))

# Plot Yield
ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X, Y, Z_yield, cmap='viridis')
ax1.set_xlabel('Solvent Volume (EtOH 96%)')
ax1.set_ylabel('Tartaric Acid (equivalents)')
ax1.set_zlabel('Yield (%)')
ax1.set_title('Yield Surface Plot')

# Plot Chiral Purity
ax2 = fig.add_subplot(222, projection='3d')
ax2.plot_surface(X, Y, Z_purity, cmap='plasma')
ax2.set_xlabel('Solvent Volume (EtOH 96%)')
ax2.set_ylabel('Tartaric Acid (equivalents)')
ax2.set_zlabel('Chiral Purity (%)')
ax2.set_title('Chiral Purity Surface Plot')

# Show the plot
plt.tight_layout()
plt.show()
