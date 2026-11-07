#!/usr/bin/env python3
"""Render the preserved AA snapshot; optional local matplotlib, never a build dependency."""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "assets/data/huangdao/aa-november-2026.json").read_text())
rows = data["rows"]
font = FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc")
plt.rcParams.update({"font.family": font.get_name(), "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.unicode_minus": False})
out = ROOT / "assets/img/huangdao"
out.mkdir(parents=True, exist_ok=True)
note = "2026-11-05 · AA v5.0.1 · Current 列表中的 8 个观察样本，非全榜前八"

fig, ax = plt.subplots(figsize=(11, 7.4), layout="constrained")
labels = [r["name"] + ("\n" + r["configurationNote"] if r["configurationNote"] else "") for r in rows]
bars = ax.barh(labels, [r["displayScore"] for r in rows], color=[r["color"] for r in rows], height=.56)
ax.invert_yaxis()
ax.set_xlim(0, data["scoreScaleMax"])
ax.set_xlabel("智能指数（官方显示整数，分数越高越好）", fontproperties=font)
ax.set_title("11 月智能指数：8 个观察样本", fontproperties=font, fontsize=17, pad=18)
ax.bar_label(bars, padding=6)
ax.grid(axis="x", alpha=.16)
ax.set_axisbelow(True)
fig.text(.5, -.015, note, ha="center", fontproperties=font, fontsize=10)
fig.savefig(out / "aa-intelligence-2026-11-05.png", dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)

fig, ax = plt.subplots(figsize=(10.4, 6.8), layout="constrained")
ax.set_xscale("log")
ax.set_xlim(.4, 12)
ax.set_ylim(0, 65)
ax.set_xticks([.5, 1, 2, 5, 10], ["$0.5", "$1", "$2", "$5", "$10"])
ax.set_yticks([0, 20, 40, 60])
offsets = [(-2, 22), (7, 8), (-30, 16), (-35, -30), (22, -5), (6, 12), (-10, -22), (12, 8)]
for i, (r, offset) in enumerate(zip(rows, offsets), 1):
    xy = (r["costUsd"], r["displayScore"])
    ax.scatter(*xy, color=r["color"], s=65, zorder=3)
    ax.annotate(str(i), xy, xytext=offset, textcoords="offset points", ha="center",
                arrowprops={"arrowstyle": "-", "color": "#777", "lw": .7})
ax.set_title("智能指数与任务成本", fontproperties=font, fontsize=17, pad=18)
ax.set_xlabel("每项指数任务的加权成本（美元，对数刻度）", fontproperties=font)
ax.set_ylabel("智能指数（官方显示整数）", fontproperties=font)
ax.grid(alpha=.16)
fig.text(.5, -.12, note + "\n点旁数字对应正文完整数据表；越靠左成本越低，越靠上分数越高。",
         ha="center", fontproperties=font, fontsize=10, linespacing=1.8)
fig.savefig(out / "aa-cost-2026-11-05.png", dpi=180, bbox_inches="tight", facecolor="white")
plt.close(fig)
