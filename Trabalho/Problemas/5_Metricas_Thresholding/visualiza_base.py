import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("snr_results.csv")

# Delta SNR
df["delta_snr"] = df["output_snr_db"] - df["input_snr_db"]

# Boxplot por família e método
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="wavelet_family", y="delta_snr", hue="threshold")
plt.title("ΔSNR por família e método (soft vs hard)")
plt.ylabel("Melhora de SNR (dB)")
plt.xlabel("Família Wavelet")
plt.show()

# Curva SNR inicial vs final
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x="input_snr_db", y="output_snr_db",
				hue="threshold", style="wavelet_family")
plt.plot([0,30],[0,30],"--",color="gray")  # linha de referência
plt.title("SNR inicial vs final")
plt.ylabel("SNR da imagem filtrada")
plt.xlabel("SNR da imagem ruidosa")
plt.show()
