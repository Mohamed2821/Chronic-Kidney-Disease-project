# House Price Prediction AI/ML Project

This project involves building a machine learning model to predict house prices based on various features. The dataset used for this project is from the Kaggle  "House Price prediction". The goal is to develop a model that accurately predicts house prices given a set of input features.

## Kaggle Competition
- Dataset: [House Prices - Advanced Regression Techniques] (https://www.kaggle.com/datasets/shree1992/housedata?resource=download&select=data.csv)
- Model Score:  0.37717843615954905% (R-squared score)

## File Structure
- `house_price_prediction.ipynb`: Jupyter Notebook containing the code for data preprocessing, exploratory data analysis (EDA), feature engineering, model training, and prediction.
- `submission.csv`: CSV file containing the predicted house prices for the test dataset.


## Libraries Used
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
  

## Data Loading and Analysis
- The training and test datasets are loaded from CSV files.
- Exploratory data analysis is performed to understand the structure and characteristics of the data.
- Data visualization techniques such as histograms, box plots, and heatmaps are used to analyze the distribution of features and identify missing values.

## Data Preprocessing
- Missing values are handled using appropriate techniques such as imputation or dropping columns.
- Categorical variables are encoded using one-hot encoding.
- Numerical features are standardized to ensure uniformity and improve model performance.

## Model Selection and Training
- Several regression models are considered, including Linear Regression, SVR, SGDRegressor, KNeighborsRegressor, DecisionTreeRegressor, RandomForestRegressor, GradientBoostingRegressor, XGBRegressor, and MLPRegressor.
- Cross-validation is used to evaluate each model's performance based on the R-squared score.
- The GradientBoostingRegressor model is selected based on its superior performance.

## Model Evaluation and Prediction
- The selected model is trained on the training dataset.
- The trained model is used to make predictions on the test dataset.
- The predictions are saved to a CSV file (`submission.csv`) for submission.

## Data Table:
date	price	bedrooms	bathrooms	sqft_living	sqft_lot	floors	waterfront	view	condition	sqft_above	sqft_basement	yr_built	yr_renovated	street	city	statezip	country
02-05-2014 00:00	313000	3	1.5	1340	7912	1.5	0	0	3	1340	0	1955	2005	18810 Densmore Ave N	Shoreline	WA 98133	USA
02-05-2014 00:00	2384000	5	2.5	3650	9050	2	0	4	5	3370	280	1921	0	709 W Blaine St	Seattle	WA 98119	USA
<img width="1153" height="61" alt="image" src="https://github.com/user-attachments/assets/780173ee-ea16-425a-9d8e-bf019e2656db" />



## Additional Notes
- The `submission.csv` file contains the predicted house prices for the test dataset.
