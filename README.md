


AI AgriYield Predictor
======================

**Overview**
------------

AI AgriYield Predictor is a small research & demo repository that demonstrates data preprocessing, model training, and a Streamlit-based inference app for agricultural crop yield prediction and crop recommendation. The code and notebooks walk through cleaning production datasets, engineering a target `Yield`, training several models (Linear Regression, RandomForest, XGBoost), and packaging the best model for inference.

**Key Features**
- **End-to-end notebooks**: preprocessing (`pre.ipynb`) and training/evaluation (`training.ipynb`).
- **Inference app**: a Streamlit app (`app.py`) to run yield predictions using saved models.
- **Multiple datasets**: cleaned and raw CSV files under `data/` to reproduce experiments.
- **Model persistence**: trained model artifacts saved under `models/` for quick inference.

Repository Layout
-----------------
- `app.py` — Streamlit application to run yield predictions using the saved model in `models/`.
- `pre.ipynb` — data preprocessing notebook that reads raw production data, cleans it, computes a `Yield` column, and writes `Crop_Production_Cleaned.csv`.
- `training.ipynb` — model training and evaluation (compares LinearRegression, RandomForest, XGBoost) and saves the best model.
- `data/` — CSV datasets used by the notebooks and app:
  - `crop_production.csv` — raw production data.
  - `Crop_Production_Cleaned.csv` — cleaned production data used for analysis.
  - `Crop_recommendation.csv` / `Crop_recommendation_Cleaned.csv` — datasets for crop recommendation tasks.
  - `Crop_Yield_Final.csv` — final dataset used to train yield models.
- `models/` — directory where trained model files (e.g. `xgb_yield_model.pkl`) can be stored for inference.
- `requirements.txt` — Python dependencies required to run the notebooks and app (project root `requirements.txt` exists).

Getting Started
---------------
1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the Streamlit app (from the repository root):

```powershell
streamlit run app.py
```

Notes
-----
- Some notebooks may contain absolute paths. If you run them locally, update dataset paths or set a root data variable at the top of the notebook.
- If you retrain models, ensure the same feature engineering (scaling, encoding) is applied before inference.

How to Reproduce Training
-------------------------
1. Open `pre.ipynb` and run the cells to generate cleaned datasets (for example `Crop_Production_Cleaned.csv`).
2. Open `training.ipynb` and run the training pipeline; notebooks compare several algorithms and save the chosen model in `models/`.
3. If you change features or target calculation, re-run the preprocessing before training.

Deployment
----------
This repo includes a Streamlit app (`app.py`) that can be deployed to any service that supports Python web apps (Streamlit Cloud, Heroku, Azure App Service, etc.). The app expects the trained model file to be present in `models/` (or adjust the app code to load the model from another location).

**Live deployment**: replace the placeholder URL below with your actual app URL once deployed.

- Deployment URL: http://ai-agri-yieldpredictor.streamlit.app/  

Contact
-------

Owner: Manoj M
Email: manojmanoj4624@gmail.com



