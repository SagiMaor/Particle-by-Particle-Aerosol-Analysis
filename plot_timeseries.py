import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot_timeseries(filepath):
    # === Step 1: Load data ===
    data = pd.read_csv(filepath)
    data.columns = data.columns.str.strip()
    data['Avg_StartTime'] = pd.to_datetime(data['Avg_StartTime'], errors='coerce', dayfirst=True)
    data.set_index('Avg_StartTime', inplace=True)

    # === Step 2: Prompt for parameter ===
    parameters = {
        "Asphericity": "Avg_Asphericity_",
        "Diameter": "Avg_Size_um_",
        "Concentration": "Avg_Conc_cm3_",
        "SurfaceArea": "Avg_SurArea_um2_cm3_",
        "Mass": "Avg_Mass_ug_m3_",
        "FluorFraction": "Avg_FluorFraction_",
        "FluorPeak": "Avg_FluorPeak_"
    }

    print("\nAvailable parameters:")
    for param in parameters:
        print("-", param)
    parameter = input("\nEnter the parameter you want to analyze: ").strip()

    if parameter not in parameters:
        print("❌ Invalid parameter. Exiting.")
        return

    if parameter == "FluorPeak":
        base_categories = ['FL1', 'FL2', 'FL3', 'A', 'B', 'C']
    else:
        base_categories = ['All', 'Excited', 'Fluorescent', 'FL1', 'FL2', 'FL3',
                           'A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC']

    # === Step 3: Prompt for categories ===
    print("\nAvailable fluorescence categories:")
    print(", ".join(base_categories))
    user_input = input("Enter categories to plot (comma-separated): ")
    categories_to_plot = [cat.strip() for cat in user_input.split(',') if cat.strip() in base_categories]

    if not categories_to_plot:
        print("❌ No valid categories selected. Exiting.")
        return

    # === Step 4: Build column map and plot labels ===
    prefix = parameters[parameter]
    categories = {cat: prefix + cat for cat in categories_to_plot}

    titles = {
        "Asphericity": "Average Asphericity",
        "Diameter": "Average Diameter",
        "Concentration": "Average Concentration",
        "SurfaceArea": "Average Surface Area",
        "Mass": "Average Mass",
        "FluorFraction": "Average Fluorescence Fraction",
        "FluorPeak": "Average Fluorescence Peak"
    }
    ylabels = {
        "Asphericity": "Asphericity",
        "Diameter": "Diameter (µm)",
        "Concentration": "Concentration (#/L)",
        "SurfaceArea": "Surface Area (µm²/cm³)",
        "Mass": "Mass (µg/m³)",
        "FluorFraction": "Fluorescence Fraction",
        "FluorPeak": "Fluorescence Peak"
    }

    title = titles[parameter]
    ylabel = ylabels[parameter]

    # === Step 5: Convert numeric and adjust units ===
    numeric_columns = list(categories.values())
    valid_columns = [col for col in numeric_columns if col in data.columns]
    data[valid_columns] = data[valid_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

    if parameter == "Concentration":
        data[valid_columns] *= 1000  # convert to #/L

    # === Step 6: Plot ===
    fig, ax = plt.subplots(figsize=(14, 8))
    lines = []

    for cat in categories_to_plot:
        col = categories.get(cat)
        if col in valid_columns:
            line = ax.plot(data.index, data[col], label=cat, linestyle='-', marker='.')
            lines.append(line)

    # X-axis: 1-hour data, but ticks every day
    ax.set_xlim(data.index.min(), data.index.max())
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_horizontalalignment('right')

    # Y-axis
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(bottom=min(0, ymin), top=ymax)

    # Styling
    ax.set_title(title, fontsize=26)
    ax.set_xlabel('Time', fontsize=20)
    ax.set_ylabel(ylabel, fontsize=20)
    leg = ax.legend(loc='upper left', fontsize=14, ncol=2, fancybox=True, shadow=True)
    leg.get_frame().set_alpha(0.4)
    plt.grid(True, linestyle='--', alpha=0.6, linewidth=2)
    plt.tight_layout(pad=4.0)
    plt.show()
