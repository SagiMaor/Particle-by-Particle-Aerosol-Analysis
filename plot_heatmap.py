import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.cm as cm
import re

def plot_heatmap(filepath):
    y_min, y_max = 0.5, 20

    # === Step 1: Load and preprocess ===
    data = pd.read_csv(filepath)
    data.columns = data.columns.str.strip()
    data['Start_Time'] = pd.to_datetime(data['Start_Time'], errors='coerce', dayfirst=True)

    # === Step 2: Generate NonFluorescent dynamically ===
    all_cols = [col for col in data.columns if "dN_dlogDp_cm3_All_" in col]
    fluor_cols = [col for col in data.columns if "dN_dlogDp_cm3_Fluorescent_" in col]
    if len(all_cols) == len(fluor_cols):
        for all_col, fluor_col in zip(all_cols, fluor_cols):
            new_col = all_col.replace("All", "NonFluorescent")
            data[new_col] = data[all_col] - data[fluor_col]
    else:
        print("❌ Column mismatch: cannot compute NonFluorescent.")
        return

    # === Step 3: Convert units (#/cm³ → #/L) ===
    cm3_cols = [col for col in data.columns if "dN_dlogDp_cm3_" in col]
    data[cm3_cols] = data[cm3_cols] * 1000

    # === Step 4: Ask user for categories ===
    print("\nAvailable categories include: All, Fluorescent, NonFluorescent, A, B, C, AB, AC, BC, ABC, FL1, FL2, FL3")
    user_input = input("Enter the categories to plot (comma-separated): ")
    categories_to_plot = [cat.strip() for cat in user_input.split(',') if cat.strip()]

    if not categories_to_plot:
        print("❌ No valid categories entered. Exiting.")
        return

    # === Step 5: Helper to split into ≤3 per figure ===
    def chunk_categories(cat_list, chunk_size=3):
        return [cat_list[i:i + chunk_size] for i in range(0, len(cat_list), chunk_size)]

    category_groups = chunk_categories(categories_to_plot)

    # === Step 6: Plot heatmaps ===
    for group in category_groups:
        fig, axes = plt.subplots(len(group), 1, figsize=(18, 6 * len(group)), sharex=True)
        if len(group) == 1:
            axes = [axes]

        for i, particle_type in enumerate(group):
            cols = [col for col in data.columns if f"dN_dlogDp_cm3_{particle_type}_" in col]
            if not cols:
                print(f"⚠️ Skipping '{particle_type}' — no matching columns found.")
                continue

            Z = data[cols].T.to_numpy()
            Z = np.where(Z < 0, np.nan, Z)
            Z_masked = np.ma.masked_invalid(Z)

            # Extract bin centers
            bin_centers = []
            for col in cols:
                match = re.search(r"_(\d+\.?\d*)um_(\d+\.?\d*)um", col)
                if match:
                    lower = float(match.group(1))
                    upper = float(match.group(2))
                    bin_centers.append((lower + upper) / 2)
            y_bins = np.array(bin_centers)
            times = data['Start_Time'].to_numpy()

            ax = axes[i]
            cmap = cm.get_cmap('plasma').copy()
            cmap.set_bad(color=cmap(0))

            im = ax.pcolormesh(times, y_bins, Z_masked, shading='nearest', cmap=cmap,
                               norm=LogNorm(vmin=1e3, vmax=np.nanmax(Z)))
            ax.set_yscale('log')
            ax.set_ylim(y_min, y_max)
            ax.set_title(f"{particle_type} Particles", fontsize=18)
            ax.tick_params(axis="x", rotation=45, labelsize=12)
            ax.tick_params(axis="y", labelsize=12)

            tick_locs = pd.date_range(start=data['Start_Time'].min().floor('h'),
                                      end=data['Start_Time'].max().ceil('h'), freq='12h')
            ax.set_xticks(tick_locs)
            ax.set_xticklabels([t.strftime('%m-%d\n%H:%M') for t in tick_locs])

            fig.colorbar(im, ax=ax, orientation="vertical", pad=0.02)

        fig.text(0.06, 0.5, "Diameter (µm)", va='center', rotation='vertical', fontsize=18)
        fig.text(0.86, 0.5, "dN/dlogDp (#/L)", va='center', rotation='vertical', fontsize=16)
        fig.suptitle("Heatmaps", fontsize=22, weight='bold', y=0.98)
        plt.tight_layout(rect=[0.08, 0.03, 0.92, 0.97])
        plt.show()
