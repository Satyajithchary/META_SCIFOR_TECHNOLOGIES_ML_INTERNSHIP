# 🏦 Loan Prediction Project

Welcome to the **Loan Prediction Project**! This repository contains the code and resources used to predict whether a loan application will be approved or not based on various features. This project is a classic example of a binary classification problem in machine learning. Let's dive into the details!

## 🚀 Project Overview

In the Loan Prediction Project, we aim to predict the likelihood of a loan application being approved by analyzing the applicant's information. The dataset includes features like income, education, employment status, and more, which are used to train the prediction model.

### 📋 Problem Statement

The goal is to create a model that can accurately predict whether a loan application will be approved (`Loan_Status = Y`) or rejected (`Loan_Status = N`). This will help financial institutions streamline their decision-making process and improve customer service.

## 📁 Dataset

- **Name:** Loan Prediction Dataset
- **Source:** loan_prediction.csv
- **Features:**
  - `ApplicantIncome`
  - `CoapplicantIncome`
  - `LoanAmount`
  - `Loan_Amount_Term`
  - `Credit_History`
  - `Gender`
  - `Married`
  - `Dependents`
  - `Education`
  - `Self_Employed`
  - `Property_Area`
  - `Loan_Status` (Target variable)

## 🛠️ Project Workflow

1. **Data Exploration and Preprocessing**
   - 🧹 Handle missing values
   - 🧮 Feature engineering
   - 🔢 Encode categorical variables
   - 🔍 Perform exploratory data analysis (EDA)

2. **Model Building**
   - 🧠 Train multiple machine learning models, including:
     - Logistic Regression
     - Decision Tree
     - Random Forest
     - Support Vector Machine (SVM)
     - XGBoost
   - ⚙️ Hyperparameter tuning to improve model performance

3. **Evaluation**
   - 📊 Evaluate models using metrics like accuracy, precision, recall, and F1-score
   - 🏆 Choose the best model based on performance



## 📊 Model Performance

- The final model achieved an **accuracy of 77%** on the test set.
- The model was evaluated using a confusion matrix, ROC curve, and classification report.

## 💻 Installation

To get started, clone this repository:

```bash
git clone https://github.com/Satyajithchary/META_SCIFOR_TECHNOLOGIES_ML_INTERNSHIP/Mini_Projects/Mini_Project_2/Loan_Prediction_Project_2.git
```

Navigate to the project directory:

```bash
cd Loan_Prediction_Project
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the Jupyter notebook to see the step-by-step process of building the model:

```bash
jupyter notebook Loan_Prediction_Project_2.ipynb
```


## 🏅 Conclusion

This project demonstrates the process of building a machine learning model for binary classification, specifically for loan prediction. The model's performance can be further improved by experimenting with different algorithms, feature selection techniques, and hyperparameter tuning.

## 🤝 Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create a pull request or open an issue.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

🎉 **Happy Coding!** 🎉
