import matplotlib.pyplot as plt
import pandas as pd

def plot_comparison(hotspot, control, feature, out_path):
    plt.figure()
    plt.boxplot([hotspot, control], labels=["Hotspot", "Control"])
    plt.title(f"{feature} comparison")
    plt.ylabel(feature)
    plt.savefig(out_path)
    plt.close()

def save_table(results, path):
    df = pd.DataFrame(results)
    df.to_csv(path, index=False)
