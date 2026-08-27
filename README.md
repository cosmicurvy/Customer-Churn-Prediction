# Customer Churn Prediction

Customer churn prediction helps businesses identify customers who are likely to stop using their services. In industries such as telecommunications, identifying potential churners can help businesses take preventive actions and improve customer retention.

This project uses the Telco Customer Churn dataset to build and evaluate machine learning models for predicting whether a customer is likely to churn.

Check out the live Tableau visualization [here](https://public.tableau.com/app/profile/urvashi.sahu6283/viz/CustomerChurnAnalysis_17797140159470/Dashboard1)

## Dataset
The dataset used in this project is the Telco Customer Churn dataset from Kaggle:<br>
👉 [https://www.kaggle.com/datasets/blastchar/telco-customer-churn]

The dataset includes information about:
- **Churn:**: Whether the customer left the service
- **Services:** Phone service, multiple lines, internet service, online security, online backup, device protection, technical support, streaming TV, and streaming movies
- **Account information**: Tenure, contract type, payment method, paperless billing, monthly charges, and total charges
- **Demographic information:** Gender, senior citizen status, partner, and dependents

## Objective 

The objective is to predict whether a customer will churn based on their historical service, account, and demographic information.<br>

Since failing to identify a customer who is likely to churn can be costly for a business, recall for the churn class was used as the primary evaluation metric.

The project covers:

1. Data cleaning and preprocessing
2. Exploratory data analysis (EDA)
3. Feature engineering 
4. Handling class imbalance
5. Model training and comparison
6. Model evaluation


## Tools And Technologies
| Category | Tools |
|---|---|
| Langauge | Python |
| Libraries | Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn Imbalanced-learn, SHAP and Streamlit|
| Envinronment | VS code and Jupyter Notebook|

## Project Workflow

### 1. Data Preparation

Cleaned the dataset, handled missing values, created a new feature, removed highly correlated features, encoded categorical variables, and split the data into training and test sets.

### 2. Exploratory Data Analysis

Analyzed customer characteristics, feature distributions, and relationships with churn to identify patterns in the data.

### 3. Model Training & Evaluation

Used Stratified K-Fold Cross-Validation and SMOTE to handle class imbalance. Compared Logistic Regression, Decision Tree, Random Forest, XGBoost, and Gradient Boosting using precision, recall, and accuracy.

### 4. Model Selection & Interpretation

Selected Logistic Regression based on its recall performance and its simplicity. Used SHAP to understand feature contributions to the model's predictions.

### 5. Deployment & Visualization

Saved the trained model and encoder, built an interactive Streamlit application, deployed it on Streamlit Cloud, and created a Tableau dashboard for exploring churn patterns.
--- 

## Key Takeaways

- Customer churn is influenced by a combination of service, account, and customer characteristics.
- Class imbalance can make accuracy alone insufficient for evaluating churn models.
- Recall was prioritized to reduce the number of actual churners missed by the model.
- Logistic Regression provided a suitable balance between churn detection, interpretability, and simplicity.
- SHAP was used to understand the features contributing to the model's predictions.