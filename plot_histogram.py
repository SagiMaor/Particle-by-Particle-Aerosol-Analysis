import pandas as pd
import matplotlib.pyplot as plt

# === CATEGORY SETUP ===

available_categories = ['All', 'Fluorescent', 'A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC']

category_colors = {
    'All': 'gray',
    'Fluorescent': 'green',
    'NonFluorescent': 'red',
    'A': '#1f77b4',
    'B': '#ff7f0e',
    'C': '#2ca02c',
    'AB': '#d62728',
    'AC': '#8c564b',
    'BC': '#9467bd',
    'ABC': '#e377c2'
}

# === HELPER FUNCTION ===

def smart_xticks(ax, x_vals):
    max_labels = 15
    step = max(1, len(x_vals) // max_labels)
    xtick_locs = x_vals[::step]
    xtick_labels = [f"{x:.1f}" for x in xtick_locs]
    ax.set_xticks(xtick_locs)
    ax.set_xticklabels(xtick_labels, rotation=45)

# === MAIN FUNCTION ===

def plot_histogram(filepath):
    print("Available categories to plot:")
    print(", ".join(available_categories))
    user_input = input("Enter the categories you want to plot (comma-separated): ")

    categories_to_plot = [cat.strip() for cat in user_input.split(',') if cat.strip() in available_categories]

    if not categories_to_plot:
        print("No valid categories selected. Exiting.")
        return

    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()

    if 'Diameter_Bin_Center' not in df.columns and 'Dp_Lower_Limit_um' in df.columns:
        df['Diameter_Bin_Center'] = (df['Dp_Lower_Limit_um'] + df['Dp_Upper_Limit_um']) / 2

    df = df.sort_values('Diameter_Bin_Center')

    plt.figure(figsize=(12, 6))
    bin_width = 0.15

    for cat in categories_to_plot:
        col = f'AvgConc_cm3_{cat}'
        if col in df.columns:
            plt.bar(
                df['Diameter_Bin_Center'],
                df[col],
                width=bin_width,
                label=cat,
                color=category_colors.get(cat, None),
                alpha=0.75,
                edgecolor='black',
                linewidth=0.5
            )
        else:
            print(f"Warning: Column '{col}' not found in file.")

    plt.yscale('log')
    plt.xlabel('Particle Diameter (µm)', fontsize=14, weight='bold')
    plt.ylabel('Concentration (#/cm³)', fontsize=14, weight='bold')
    plt.title('Particle Size Distribution Histogram', fontsize=16, weight='bold')
    smart_xticks(plt.gca(), df['Diameter_Bin_Center'].values)
    plt.legend(title='Category', fontsize=12, title_fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
