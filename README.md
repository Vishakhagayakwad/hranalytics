# HR Analytics Project

## Overview

I'm excited to share my latest HR Analytics project, where I utilized Exploratory Data Analysis (EDA) and advanced machine learning techniques to gain insights into employee data. This project involved comprehensive data analysis, visualization, and modeling to predict and understand factors influencing employee salaries and performance.

## Dataset

The HR dataset includes the following features:
- **Gender**
- **Age**
- **Salary**
- **Education**
- **Experience**
- **Other relevant factors**

## Project Steps

### 1. Data Exploration and Cleaning

- **Initial Data Analysis:** Loaded the dataset, visualized the head and tail, and reviewed basic information, shape, and null values.
- **Handling Missing Values:** Replaced null values using the KNN imputer for more accurate data filling.
- **Outlier Detection:** Identified and removed outliers using the IQR method. Validated the removal with box plots.

### 2. Data Visualization

- **Category Analysis:** Plotted counts for various categories to understand data distribution. Observed minimal gender disparity and noted that most employees are senior with a mean age of 51.
- **Distribution Analysis:** Used QQ-plot to check normality, histogram plots to assess skewness, and scatter plots to explore relationships between numerical data.
- **Impact Analysis:** Analyzed how categorical and dependent variables affect employee salaries.

### 3. Data Cleaning and Preparation

- **Outlier Removal:** Removed outliers in numerical data using the IQR method.
- **Correlation Analysis:** Applied Spearman's correlation to identify and drop highly correlated features to stabilize the model.
- **Data Normalization:** Split the data into training and testing sets and normalized it using the `StandardScaler` method.

### 4. Model Building

- **Machine Learning Techniques:** Implemented and evaluated various machine learning algorithms:
  - Linear Regression
  - Decision Trees
  - Random Forest
  - XGBoost
- **Model Evaluation:** Found that the Random Forest Algorithm achieved the highest accuracy among all models.

## Technologies and Libraries Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn (StandardScaler, KNN Imputer)
- XGBoost
  
## Results

1. **Experience and Education:** Employees with higher experience and education levels tend to contribute more significantly to company sales. It’s beneficial for the company to hire experienced candidates with advanced education.
2. **Salary Influences:** Salary is primarily influenced by age, months of experience, and education. Company sales are directly related to employee salaries.

## Impact

The insights gained from this analysis can guide HR decisions, particularly in hiring strategies. By focusing on candidates with high experience and education, companies can potentially maximize their sales performance.



