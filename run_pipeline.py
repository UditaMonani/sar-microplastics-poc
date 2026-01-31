from src.preprocess import preprocess_sar
from src.features import basic_stats, texture_features
from src.analysis import plot_comparison, save_table
import glob

hotspot_files = glob.glob("data/sar/hotspot/*.tif")
control_files = glob.glob("data/sar/control/*.tif")

hotspot_vals, control_vals = [], []

for f in hotspot_files:
    img, _ = preprocess_sar(f)
    feat = basic_stats(img)
    hotspot_vals.append(feat["mean"])

for f in control_files:
    img, _ = preprocess_sar(f)
    feat = basic_stats(img)
    control_vals.append(feat["mean"])

plot_comparison(
    hotspot_vals,
    control_vals,
    "Mean σ⁰ (normalized)",
    "results/plots/mean_backscatter.png"
)

save_table(
    {"hotspot_mean": hotspot_vals, "control_mean": control_vals},
    "results/tables/statistics.csv"
)
