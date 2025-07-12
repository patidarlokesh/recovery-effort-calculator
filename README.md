# 🧮 Effort to Recover – Drawdown Recovery Calculator

A simple Tkinter-based calculator to understand **how much gain (%) is needed to recover from a capital drawdown** in trading or investing.

---

## 📌 What It Does

This tool helps you answer a very important question:

> "If I lost X% of my capital, how much % profit do I need to recover back to break-even?"

For example:
- A 25% loss needs 33.33% gain to recover.
- A 50% loss needs 100% gain to recover.


The Formula Used

Recovery% needed to regain original capital:
Recovery (%)  = ((1 / (1 - total_drawdown / 100)) - 1) * 100
Recovery% = Capital gain required to reach back to the original capital
