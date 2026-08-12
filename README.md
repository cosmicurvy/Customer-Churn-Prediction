# Customer Churn Prediction

Predicting Customer Churn (whether a customer will stop using a service or product) is essential for businesses, epecially in telecom, where retaining customers is often more cost-effective than acquiring new ones. 

This repository demonstrates a complete machine learning workflow to build and evaluate a churn prediction model using the Telco Customer Churn dataset. 

Check out the live Tableau visualization [here](https://public.tableau.com/app/profile/urvashi.sahu6283/viz/CustomerChurnAnalysis_17797140159470/Dashboard1)

## Dataset
This project uses the Telco Customer Churn dataset from Kaggle:<br>
👉 [https://www.kaggle.com/datasets/blastchar/telco-customer-churn]

The dataset includes information about:
* Customers who left(Churn)
* Services signed up for - phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and streaming movies
* Account details - tenure(how long they’ve been a customer), contract, payment method, paperless billing, monthly charges, and total charges
* Demographic info - gender, age range, partners and dependents

## Objective 

The goal is to build a model that can predict whether a customer will churn or not based on historical data.<br>
This includes:

1. Data Cleaning and Preprocessing
2. Exploratory Data Analysis (EDA)
3. Handling Imbalanced Data
3. Model Training and Evaluation
4. Interpretation of Results
5. Performance Comparison


## Tools And Technologies
| Category | Tools |
|---|---|
| Langauge | Python |
| Libraries | Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn Imbalanced-learn and SHAP|
| Envinronment | VS code and Jupyter Notebook|

## Steps In The Project

### Data Loading
Load the dataset into a Pandas Dataframe and inspect basic properties such as shape, columns, missing values and duplicates.

### Exploratory Data Analysis (EDA)
Visualize key relationships, feature distributions and class distributions.

### Handle class Imbalance
Address the class imbalance present in the dataset using the SMOTE technique. 

### Model Training
Train multiple models (Logistic Regression, Decision Tree, Random Forest, XGBoost, and Gradient Boosting) using Stratified K-Fold Cross-Validation and compares them. 

### Model Evaluation
Evaluate the performance of the model using recall as False negatives are more costly in customer churn analysis. 

### Conclusion and insights
Summarize key findings and actionable insights at each step. 


