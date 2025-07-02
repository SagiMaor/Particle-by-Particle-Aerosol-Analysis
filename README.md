# 🌬️ Particle-by-Particle Aerosol Analysis

Marine biological aerosols—also known as bioaerosols—are microscopic particles like bacteria, viruses, phytoplankton fragments, and organic matter that are ejected into the atmosphere via wave breaking and bubble bursting at the ocean surface. These particles play critical roles in cloud formation, climate regulation, atmospheric chemistry, and the global transport of microorganisms. To investigate them, the **Wideband Integrated Bioaerosol Sensor (WIBS)** provides a cutting-edge method for real-time detection and classification of fluorescent biological particles, using size, morphology, and fluorescence signals across multiple spectral channels.

This project introduces a flexible and user-friendly analysis tool for handling WIBS data, aimed at deepening our understanding of how marine aerosols are generated, transformed, and transported. It provides customizable options for exploring time-resolved and size-resolved patterns in fluorescent particle concentrations—helping researchers bridge the gap between raw instrument output and meaningful atmospheric insights.

---

## 🔍 What Does This Project Do?

This tool processes and analyzes `.csv` files exported by the stock Igor toolkit that comes bundled with the WIBS instrument. While Igor handles basic formatting and raw signal extraction, this Python-based tool provides an intuitive interface for in-depth exploratory analysis.

Upon loading a WIBS CSV file, the script parses and organizes the data, then prompts the user to choose the type of output they’d like to generate. Options include:

- Time series plots of total or category-specific particle concentrations  
- Heatmaps showing fluorescence intensities across size bins and channels  
- Size distribution histograms grouped by particle category

Users can filter by specific particle types and categories, enabling targeted, high-resolution views of aerosol behavior under different environmental conditions.

---

## 📥 Input & Output

- **Input**:  
  A **merged `.csv` file** produced by the WIBS Igor toolkit, either for:
  - Time-series data 
  - Histogram-style size distributions 
  - Fluorescence-resolved size bins 

- **Output**:  
  - Time series line plots with optional error bars  
  - Size-binned histograms with smart binning and log-scale  
  - Vertical heatmaps showing particle concentration across size bins over time  
  - All plots displayed interactively (can be saved manually)

---

## ⚙️ Technical Implementation

This project is implemented in **Python** using modular scripts. You will need the following Python packages:

```bash
pip install pandas matplotlib numpy

---

## ▶️ How to Run

1. Open a terminal and navigate to the project folder.
2. Run the main script:

```bash
python run.py


