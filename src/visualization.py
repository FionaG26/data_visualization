# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns


def plot_icu_beds(data):
    plt.figure(figsize=(15, 8))
    sns.barplot(x='Number of beds', y='Hospital', data=data, palette='viridis')
    plt.title('Number of ICU Beds per Hospital')
    plt.xlabel('Number of Beds')
    plt.ylabel('Hospital')
    plt.show()
