# Medical-Insurance-Price-Prediction

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
- **Source:** [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Rows:** 1,338  
- **Columns:** 7  

### Features:
| Feature | Description |
|----------|--------------|
| age | Age of the individual |
| sex | Gender (male/female) |
| bmi | Body Mass Index — ideal range 18.5 to 24.9 |
| children | Number of dependents |
| smoker | Smoking status (yes/no) |
| region | Residential area in the US (northeast, southeast, etc.) |
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
| Model | R² Score | MAE | RMSE |
|--------|-----------|------|------|
| Linear Regression | 0.74 | 4200.35 | 6000.23 |
| Random Forest Regressor | 0.86 | 2700.41 | 4800.10 |
| Gradient Boosting | 0.88 | 2500.32 | 4500.21 |

*(Values are indicative — replace with your actual results)*

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/username/medical-insurance-prediction.git
cd medical-insurance-prediction
