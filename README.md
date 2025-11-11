````markdown
# 🌞 MoonLight Solar Analysis

A data-driven analysis project for **MoonLight Energy Solutions**, focused on evaluating solar potential across multiple African regions using exploratory data analysis, cleaning workflows, statistical comparisons, and reproducible pipelines.

---

## ✅ Quick Start Guide

### 1. Clone the repository

```bash
git clone https://github.com/dawit-hopes/solar-challenge-.git
cd solar-challenge-
````

### 2. Create & activate the environment

```bash
conda create -n moonlight python=3.13
conda activate moonlight
pip install -r requirements.txt
```

### 3. Launch notebooks

```bash
jupyter lab
```

Open any notebook inside the `notebooks/` directory such as:

* `eda-benin-malanville.ipynb`
* `eda-sierraleone-bumbuna.ipynb`
* `eda_togo_dapaong_qc.ipynb`
* `compare_countries.ipynb`

---

## ✅ Usage Examples

### **Run a script to clean data**

```bash
python scripts/clean_data.py --input data/benin-malanville.csv --output data/benin-malanville_clean.csv
```

### **Run a script to generate correlations**

```bash
python scripts/plot_correlations.py --country benin
```

### **Compare across all countries**

```bash
python scripts/compare_countries.py
```

---

## 📂 Folder Structure

```
.
├── data/
│   ├── benin-malanville.csv
│   ├── benin-malanville_clean.csv
│   ├── sierraleone-bumbuna.csv
│   ├── sierraleone-bumbuna_clean.csv
│   ├── togo-dapaong_qc.csv
│   └── togo-dapaong_qc_clean.csv
│
├── notebooks/
│   ├── compare_countries.ipynb
│   ├── eda-benin-malanville.ipynb
│   ├── eda-sierraleone-bumbuna.ipynb
│   ├── eda_togo_dapaong_qc.ipynb
│   ├── utils.py
│   ├── README.md
│   ├── __init__.py
│   └── __pycache__/
│       └── utils.cpython-313.pyc
│
├── scripts/
│   ├── README.md
│   └── __init__.py
│
├── src/
│
├── tests/
│   └── __init__.py
│
├── requirements.txt
└── README.md
```

---

## 📂 Dataset Overview

The dataset contains time-series solar radiation and environmental sensor measurements.
Main fields include:

* **Timestamp** – date/time of observation
* **GHI / DNI / DHI** – solar irradiance values
* **ModA / ModB** – sensor/module performance readings
* **Tamb / TModA / TModB** – temperatures
* **RH** – relative humidity
* **WS / WSgust / WD** – wind speed, gust, and direction
* **BP** – barometric pressure
* **Cleaning** – cleaning events
* **Precipitation** – rainfall rate
* **Comments** – extra notes

---

