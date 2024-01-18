# main.py
import matplotlib
matplotlib.use('agg')  # or 'Qt5Agg' depending on your environment


from data_processing import load_data, preprocess_data
from visualization import plot_icu_beds


def main():
    # Load and preprocess data
    data = load_data('data/ICU_beds_data.xlsx')
    processed_data = preprocess_data(data)

    # Visualize ICU bed data
    plot_icu_beds(processed_data)

    if __name__ == "__main__":
        main()
