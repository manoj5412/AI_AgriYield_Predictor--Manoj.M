AI AgriYield Predictor
======================

Overview
--------

This repository contains code and datasets for a machine learning project that predicts crop yield and recommends crops based on input features such as region, soil, and historical production data. The project includes cleaned CSV datasets and a Jupyter notebook for preprocessing and experimentation.

Repository structure
--------------------

- `pre.ipynb` - Jupyter notebook with data exploration, preprocessing, and model experiments.
- `data/` - directory containing source and cleaned CSV datasets used by the notebooks and scripts.
	- `Crop_Production_Cleaned.csv`
	- `crop_production.csv`
	- `Crop_recommendation_Cleaned.csv`
	- `Crop_recommendation.csv`
	- `Crop_Yield_Final.csv`
- `Results/` - folder where experiment outputs, model files, and result artifacts can be stored.

Getting started
---------------

Prerequisites
1. Python 3.8+ (recommended)
2. Jupyter or JupyterLab to run the notebook

Install dependencies (recommended to use a virtual environment):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
```

If there is no `requirements.txt`, install commonly used packages for this type of project:

```powershell
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

Running the notebook
--------------------

Start Jupyter and open `pre.ipynb`:

```powershell
jupyter notebook pre.ipynb
```

Notes
-----

- The `data/` directory contains both raw and cleaned datasets. Use the cleaned CSVs for modeling experiments.
- If you add or change datasets, please include a short note in this README describing the change and the date.

Contributing
------------

Contributions are welcome. Please open an issue describing the change you want to make, or submit a pull request with a clear description of the changes and why they're needed.

License
-------

Specify a license for your project here (for example, MIT). If you don't want to add a license yet, delete this section.

Contact
-------
Overview
--------

This repository implements data cleaning, model training, and a small Streamlit app for predicting crop yield and recommending crops based on soil, weather and regional data. The project contains raw and cleaned CSV datasets, two notebooks for preprocessing and training, a Streamlit frontend (`app.py`), and a pre-trained model in `models/`.

What I found in this workspace
------------------------------

- Top-level files:
	- `app.py` — Streamlit app to run predictions from a saved model.
	- `pre.ipynb` — preprocessing notebook (loads `crop_production.csv`, cleans it and writes `Crop_Production_Cleaned.csv`).
	- `training.ipynb` — training and model comparison (LinearRegression, RandomForest, XGBoost) using `Crop_Yield_Final.csv`.
	- `README.md` — this file (updated).
	- `Results/` — (empty or used for artifacts/results).
- `models/` contains:
	- `xgb_yield_model.pkl` — XGBoost model used by the Streamlit app.
- `data/` contains these CSVs (sizes are approximate based on file):
	- `crop_production.csv` — raw production data (≈246k rows). Columns: State_Name, District_Name, Crop_Year, Season, Crop, Area, Production
	- `Crop_Production_Cleaned.csv` — cleaned production data (≈206k rows). Columns: State, District, Year, Season, Crop, Area, Production, Yield
	- `Crop_recommendation.csv` — features + label for crop recommendation (≈2.2k rows). Columns: N,P,K,temperature,humidity,ph,rainfall,label
	- `Crop_recommendation_Cleaned.csv` — cleaned recommendation dataset (≈2.2k rows). Columns: N,P,K,temperature,humidity,ph,rainfall,crop
	- `Crop_Yield_Final.csv` — combined dataset used for yield modeling (≈22.7k rows). Columns include State, District, Year, Season, Crop, Area, Production, Yield, crop, N,P,K,temperature,humidity,ph,rainfall

Recommended project contract (short)
-----------------------------------

- Inputs: CSV data in `data/` (see column lists above). For predictions, `app.py` accepts user inputs for state, district, season, crop, year, area, production, N,P,K,temperature, humidity, ph, rainfall.
- Outputs: Predicted yield (tons/hectare) and model artifacts saved under `models/` or `Results/`.
- Error modes: missing model file, missing data files, mismatched feature ordering when predicting. The Streamlit app stops if the model fails to load.

How to run
----------

1) (Optional) Create & activate a virtual environment (PowerShell):

```powershell
python -m venv .venv; .\\.venv\\Scripts\\Activate.ps1
```

2) Install dependencies. If there's a `requirements.txt` add it; otherwise install common packages:

```powershell
pip install pandas numpy scikit-learn xgboost streamlit matplotlib seaborn jupyter
```

3) Run the Streamlit app:

```powershell
streamlit run app.py
```

This should open a browser UI that loads the model from `models/xgb_yield_model.pkl` and lets you enter inputs to get a yield prediction.

4) Reproduce training/experiments

- Open `training.ipynb` in JupyterLab/Notebook to inspect the training pipeline. The notebook trains multiple regressors and uses XGBoost with n_estimators=200 in the provided code. It saves the best model (example: `best_yield_xgboost_model.pkl` or `xgb_yield_model.pkl`).
- `pre.ipynb` shows the preprocessing steps used to create `Crop_Production_Cleaned.csv` (drop duplicates, fill medians, create `Yield`, encode categories, drop outliers, etc.).

Datasets (quick summary)
------------------------

- `crop_production.csv` (raw): national/state/district level production entries. Columns: State_Name, District_Name, Crop_Year, Season, Crop, Area, Production. Use this for custom preprocessing if you want the original raw fields.
- `Crop_Production_Cleaned.csv`: cleaned production with numeric `State` and `District` encodings and a computed `Yield` column. ~206k rows.
- `Crop_Yield_Final.csv`: final dataset used for model training with agronomic features added (N,P,K,temperature,humidity,ph,rainfall) and `Yield`. ~22.7k rows.
- `Crop_recommendation*.csv`: small dataset (~2.2k rows) used for crop recommendation experiments. `Crop_recommendation.csv` includes a `label` column, the cleaned version uses `crop` as the label column name.

Notes and caveats
-----------------

- The Streamlit UI in `app.py` assumes the model expects encoded categorical columns and a specific ordering of features. If you retrain a model, ensure the feature engineering is applied the same way at prediction time.
- Some code in the notebooks references absolute paths like `A:\Agri yield prediction\data\...`. If you move the project folder or run locally, update file paths or use relative paths.
- There is no `requirements.txt` in the repository yet; consider adding one to lock dependencies.

Contributing
------------

Contributions are welcome. Please open an issue for proposed changes or submit a pull request with clear details.

License
-------

Add a license (for example, MIT) by creating a `LICENSE` file. If you prefer, I can add an MIT license for you.

Contact
-------

Owner: Manoj.M
Email: manojmanoj4624@gmail.com