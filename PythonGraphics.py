import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv("driving_simulator.csv")


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.suptitle("График эффективности и пользы ODS(игры)", fontsize=15, fontweight="bold")



ax1 = axes[0, 0]
df1 = df[df["chart_id"] == 1]

ax1.plot(df1["category"], df1["value_1"], color="green", marker="o", linewidth=2, label="Желание просто играть")
ax1.plot(df1["category"], df1["value_2"], color="red", marker="o", linewidth=2, label="Стимул кодить / создавать свое")

ax1.set_title("1) Эволюция игрока: от игры к кодингу", fontsize=11, fontweight="bold")
ax1.set_xlabel("Часы в симуляторе")
ax1.set_ylabel("Уровень мотивации (%)")
ax1.legend(loc="center right")



ax2 = axes[0, 1]
df2 = df[df["chart_id"] == 2]

topics = df2["category"].values
x2 = np.arange(len(topics))
width = 0.35

ax2.bar(x2 - width/2, df2["value_1"], width, label="Сухая теория", color="grey")
ax2.bar(x2 + width/2, df2["value_2"], width, label="Обучение в симуляторе", color="purple")

ax2.set_title("2) Скорость усвоения тем Python", fontsize=11, fontweight="bold")
ax2.set_xticks(x2)
ax2.set_xticklabels(topics, rotation=25, ha="right", fontsize=9)
ax2.set_ylabel("Уровень усвоения (%)")
ax2.legend(loc="upper right")




ax3 = axes[1, 0]
df3 = df[df["chart_id"] == 3]

metrics = df3["category"].values
x3 = np.arange(len(metrics))

ax3.bar(x3 - width/2, df3["value_1"], width, label="Реальный полигон", color="red")
ax3.bar(x3 + width/2, df3["value_2"], width, label="2D-Симулятор", color="blue")

ax3.set_title("3) Сравнение издержек и рисков", fontsize=11, fontweight="bold")
ax3.set_xticks(x3)
ax3.set_xticklabels(metrics, rotation=15, ha="right", fontsize=9)
ax3.set_ylabel("Масштаб издержек (%)")
ax3.legend(loc="upper right")

ax4 = axes[1, 1]
df4 = df[df["chart_id"] == 4]

genres = df4["category"].values
retention = df4["value_1"].values

colors = ["black", "black", "grey", "black", "grey", "green"]

bars = ax4.bar(genres, retention, color=colors, width=0.55)

ax4.set_title("4) Индекс развлечения (D7 Retention)", fontsize=11, fontweight="bold")
ax4.set_xticklabels(genres, rotation=20, ha="right", fontsize=9)
ax4.set_ylabel("Удержание D7 (%)")

for bar in bars:
    h = bar.get_height()
    ax4.annotate(f"{int(h)}%", xy=(bar.get_x() + bar.get_width()/2, h),
                 xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9, fontweight="bold")

plt.savefig("simulator_analytics.png", dpi=300)
plt.show()
