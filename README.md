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

Users can filter by specific date ranges and particle types, enabling targeted, high-resolution views of aerosol behavior under different environmental conditions.

---

## 📥 Input & Output

- **Input**:  
  A `.csv` file generated by the WIBS Igor toolkit, containing particle-level time-series data and fluorescence signals.

- **Output**:  
  - Time series plots (displayed or saved)  
  - Fluorescence heatmaps across particle sizes  
  - Particle size distribution histograms  
  - Optional summary statistics or filtered views

---

## ⚙️ Technical Implementation

This project is implemented in Python. To run it, you will need access to a Python console and the following libraries installed:  
`pandas`, `matplotlib`, `numpy`, `re`, and `pathlib`.

You will also need a `.csv` file generated by the WIBS Igor toolkit. Once the script is opened, simply insert the path to your file and run the program. The tool will interactively guide you through selecting the analysis type, date range, and particle category.

---

## ✅ Conclusion

This project offers an accessible and modular tool for exploring biological aerosol data from WIBS instruments. It simplifies and enhances the way researchers visualize and interpret marine aerosol measurements by providing clear, interactive access to particle-level fluorescence and size distribution data. As ocean-atmosphere interactions grow in importance within climate science, tools like this are essential for translating raw instrumentation output into scientifically actionable insights.

This project was written as part of the [WIS Python Course – March 2025](https://github.com/code-Maven/wis-python-course-2025-03).
