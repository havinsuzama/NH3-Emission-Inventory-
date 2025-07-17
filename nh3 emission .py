import pandas as pd
import matplotlib.pyplot as plt



-
emission_factors = {
    "Cattle": 20.0,  # Büyükbaş hayvanlar
    "Sheep": 1.5,    # Koyun
    "Goat": 1.0      # Keçi
}


df = pd.read_csv("data/animal_counts.csv")

for animal, ef in emission_factors.items():
    df[f"{animal}_NH3"] = df[animal] * ef  # Örn: Cattle_NH3 = Cattle * 20


df["Total_NH3_Emission"] = df[[f"{a}_NH3" for a in emission_factors]].sum(axis=1)


df.to_csv("outputs/nh3_emissions_by_province.csv", index=False)


plt.figure(figsize=(10, 6))
plt.bar(df["Province"], df["Total_NH3_Emission"], edgecolor="black")
plt.xlabel("İl", fontsize=12)
plt.ylabel("Toplam NH₃ Emisyonu (kg/yıl)", fontsize=12)
plt.title("İl Bazında Tarımsal NH₃ Emisyonları", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("outputs/emissions_bar_chart.png", dpi=300)
plt.show()


