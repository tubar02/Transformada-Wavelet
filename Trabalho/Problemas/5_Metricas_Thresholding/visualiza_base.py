import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("snr_results.csv")
df["delta_snr"] = df["output_snr_db"] - df["input_snr_db"]

sns.set_theme(style="whitegrid", context="paper")
plt.rcParams.update({
    "font.size": 10,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 8,
    "pdf.fonttype": 42,  # mantém o texto do PDF editável
})

# 1. Melhora da SNR
fig, ax = plt.subplots(figsize=(6.3, 3.8))

sns.boxplot(
    data=df,
    x="wavelet_family",
    y="delta_snr",
    hue="threshold",
    palette="colorblind",
    ax=ax
)

ax.set_xlabel("Família wavelet")
ax.set_ylabel(r"$\Delta$SNR (dB)")
ax.legend(title="Thresholding", frameon=False)

fig.tight_layout()
fig.savefig("delta_snr_wavelets.pdf", bbox_inches="tight")
plt.show()

# 2. SNR inicial versus final
fig, ax = plt.subplots(figsize=(6.3, 3.8))

sns.scatterplot(
    data=df,
    x="input_snr_db",
    y="output_snr_db",
    hue="threshold",
    style="wavelet_family",
    palette="colorblind",
    s=35,
    alpha=0.75,
    ax=ax
)

limite_min = min(df["input_snr_db"].min(), df["output_snr_db"].min())
limite_max = max(df["input_snr_db"].max(), df["output_snr_db"].max())

ax.plot(
    [limite_min, limite_max],
    [limite_min, limite_max],
    "--",
    color="black",
    linewidth=0.8,
    label="Sem alteração"
)

ax.set_xlabel("SNR da imagem ruidosa (dB)")
ax.set_ylabel("SNR da imagem filtrada (dB)")
ax.legend(frameon=False, fontsize=7)

fig.tight_layout()
fig.savefig("snr_antes_depois.pdf", bbox_inches="tight")
plt.show()