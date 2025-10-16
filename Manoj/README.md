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

Owner: Manoj.M
Email: manojmanoj4624@gmail.com


