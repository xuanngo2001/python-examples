#!/usr/bin/python3
import matplotlib
matplotlib.use('Agg') # Bypass the need to install Tkinter GUI framework
import matplotlib.pyplot as plt

# Draw a simple red line at y=0.5.
plt.axhline(y=0.5, color='r', linestyle='-')


# Draw a line between x-axis 0.25 and 0.8.
green_fluorescent='#83f52c'
plt.axhline(y=0.2, xmin=0.25, xmax=0.8, color=green_fluorescent, linestyle='--', linewidth=2)

# Save graph to file.
plt.savefig('horizontal-lines.png')