import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # for modern color palettes

# --- Read your CSV files ---
try:
    df = pd.read_csv("earthquake_1995-2023.csv")
    df2 = pd.read_csv("earthquake_data.csv")
except FileNotFoundError:
    raise SystemExit("No file found, nothing to process!")

# --- Merge the two DataFrames ---
merge_df = pd.merge(df, df2)

# --- Check if magnitude column exists ---
if "magnitude" not in merge_df.columns:
    raise KeyError("No column named 'magnitude' exists!")

# --- Calculate average magnitude by continent ---
magnitude_avg = merge_df.groupby("continent")["magnitude"].mean().reset_index()

# --- Choose a clean style and color palette ---
plt.style.use("seaborn-v0_8-whitegrid")
palette = sns.color_palette("viridis", len(magnitude_avg))

# --- Create figure ---
plt.figure(figsize=(10, 6))

# --- Plot bar chart ---
bars = plt.bar(
    magnitude_avg["continent"],
    magnitude_avg["magnitude"],
    color=palette,
    edgecolor="none",
    alpha=0.9
)

# --- Add value labels above bars ---
for i, v in enumerate(magnitude_avg["magnitude"]):
    plt.text(i, v + 0.05, f"{v:.2f}", ha='center', fontsize=10, fontweight='medium')

# --- Add titles and labels ---
plt.title("Average Magnitude of Earthquakes by Continent", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Continent", fontsize=12)
plt.ylabel("Average Magnitude", fontsize=12)
plt.xticks(rotation=90, ha='right', fontsize=10)
plt.yticks(fontsize=10)

# --- Remove top and right borders for a cleaner look ---
sns.despine()

# --- Final layout and display ---
plt.tight_layout()
plt.show()
