


AI AgriYield Predictor
======================

Overview
--------

This repository contains code, notebooks and datasets for an agricultural yield prediction and crop recommendation project. It includes preprocessing notebooks, training experiments, a Streamlit app for inference, and several cleaned datasets.

Quick project layout
--------------------

- `Manoj/` — main working folder containing the notebooks, app and data (this repository's working subfolder).
- `Manoj/app.py` — Streamlit application to run yield predictions using the saved model in `Manoj/models/`.
- `Manoj/pre.ipynb` — data preprocessing notebook (loads raw production data, cleans it, computes `Yield`, and saves `Crop_Production_Cleaned.csv`).
- `Manoj/training.ipynb` — model training and evaluation (compares LinearRegression, RandomForest, and XGBoost; saves best model).
- `Manoj/data/` — CSV datasets used by the notebooks and app:
	- `crop_production.csv` (raw)
	- `Crop_Production_Cleaned.csv` (cleaned)
	- `Crop_recommendation.csv` / `Crop_recommendation_Cleaned.csv` (crop recommendation data)
	- `Crop_Yield_Final.csv` (final dataset used to train yield models)
- `Manoj/models/` — saved model files (for example `xgb_yield_model.pkl`).
- `Manoj/requirements.txt.txt` — dependency list (install into a venv before running).
- `Manoj/CONTRIBUTING.md`, `Manoj/LICENSE` — contribution and license info.

Getting started (minimal)
-------------------------

1) Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venj\Scripts\Activate.ps1  # or: .\.venv\Scripts\Activate.ps1
```

2) Install dependencies (from the provided file in `Manoj/`):

```powershell
pip install -r Manoj\requirements.txt.txt
```

3) Run the Streamlit app from the `Manoj` folder:

```powershell
cd Manoj
streamlit run app.py
```

Notes & caveats
---------------

- Some notebooks reference absolute paths (for example `A:\Agri yield prediction\data\...`). If you run locally, either adjust those paths or open the notebooks and run the cells after setting a local data root variable.
- The Streamlit app expects the model and preprocessing logic to match the model used at training time. If you retrain the model, keep the same feature engineering steps for inference.
- If you prefer `requirements.txt` at the repository root, I can move/rename `Manoj/requirements.txt.txt` to `requirements.txt`.

Contact
-------

Owner: Manoj.M
Email: manojmanoj4624@gmail.com
