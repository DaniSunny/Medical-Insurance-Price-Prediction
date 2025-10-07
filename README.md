
# 🏥 Medical Insurance Price Prediction

## 📘 Overview
This project aims to predict **medical insurance costs** based on various personal and lifestyle attributes such as age, BMI, smoking habits, gender, and region.  
Using **Machine Learning**, the model helps insurance companies and individuals estimate charges more accurately and transparently.

---

## 🎯 Objective
To build a predictive model that estimates medical insurance charges using regression techniques.

---

## 🧠 Problem Statement
Health insurance cost prediction is crucial for understanding how demographic and lifestyle factors affect medical expenses.  
By analyzing these relationships, we can build an efficient model to predict future charges and support better financial planning.

---

## 📊 Dataset
- [📂 Download Dataset](insurance.csv)
- **Rows:** 1,338  
- **Columns:** 7  

### Features:
| Feature | Description |
|----------|--------------|
| age | Age of the individual |
| sex | Gender (male/female) |
| bmi | Body Mass Index  |
| children | Number of dependents |
| smoker | Smoking status (yes/no) |
| region | Residential area in the US (northeast, southeast, southwest, northwest) |
| charges | Target variable — individual medical costs billed by health insurance |

---

## ⚙️ Technologies Used
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **IDE/Tools:** Jupyter Notebook, VS Code  
- **Deployment:** Streamlit  

---

## 🧩 Workflow
1. **Data Collection & Exploration** – Load and analyze the dataset.  
2. **Data Preprocessing** – Handle missing values, encoding categorical variables, and feature scaling.  
3. **Exploratory Data Analysis (EDA)** – Visualize relationships and distributions.  
4. **Model Building** – Train regression models such as Linear Regression, Random Forest, etc.  
5. **Model Evaluation** – Compare performance using metrics like MAE, MSE, and R² Score.  
6. **Deployment** – Build an interactive Streamlit web app for real-time prediction.

---

## 📈 Model Performance

| Model                           | R² Score | MAPE   | RMSE    |
|----------------------------------|-----------|--------|---------|
| Linear Regression                | 0.76      | 0.4358 | 5812.10 |
| Decision Tree Regressor          | 0.71      | 0.3666 | 6460.63 |
| Random Forest Regressor          | 0.85      | 0.3200 | 4566.90 |
| Gradient Boosting Regressor      | 0.86      | 0.2869 | 4445.71 |
| Extra Gradient Boosting Regressor| 0.83      | 0.3572 | 4941.76 |

*( gradient boosting have high r2 score compared to others so use gradient boosting regressor for rest of model prediction
)*

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash

git clone https://github.com/DaniSunny/Medical-Insurance-Price-Prediction.git
cd medical-insurance-prediction
```

### 2️⃣ Run the Streamlit App
```bash

streamlit run app.py
```
- Open your brower and navigate to the url shown in the terminal
