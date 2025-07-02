from plot_histogram import plot_histogram
from plot_timeseries import plot_timeseries
from plot_heatmap import plot_heatmap

def main():
    print("\n📊 Select the type of plot you want to generate:")
    print("1. Histogram")
    print("2. Time Series")
    print("3. Heatmap")

    choice = input("Enter the number (1/2/3): ").strip()

    if choice not in ['1', '2', '3']:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
        return

    filepath = input("📁 Enter the full path to the merged CSV file: ").strip()

    if choice == '1':
        plot_histogram(filepath)
    elif choice == '2':
        plot_timeseries(filepath)
    elif choice == '3':
        plot_heatmap(filepath)

if __name__ == "__main__":
    main()
