Diabetes Prediction and Hospital Patient Records App

This project is a desktop application built using Python and Tkinter. It is designed for hospital use to predict whether a patient is diabetic based on input parameters and to maintain a record of predictions made.

Features:

1. Diabetes Prediction:
   - Users enter values such as glucose, blood pressure, BMI, insulin, age, etc.
   - A machine learning model (SVM) is used to predict if the patient is diabetic or not.

2. Record Keeping:
   - Each prediction is saved to a file named patients.csv.
   - Stored information includes the patient's name, input values, prediction result, and date/time.

Files:

- hospital_app.py: The main application GUI with options to launch the predictor or view past records.
- diabeties.py: The diabetes prediction form and machine learning logic.
- patients.csv: This file is automatically created and stores patient data.
- requirements.txt: A list of Python packages required to run the application.
- hospital.png: Optional image logo for branding in the GUI.
- ALGORITHMS.md: Optional file with different machine learning models you can use.

How to Run:

1. Install the required libraries:
   pip install -r requirements.txt

2. Run the main application:
   python hospital_app.py

About the Machine Learning Model:

- Dataset: Pima Indians Diabetes Dataset
- Algorithm: Support Vector Machine (SVM)
- Preprocessing: StandardScaler used for normalization
- You can switch to other models like RandomForest, LogisticRegression, or XGBoost by editing the model code in diabeties.py.

Customization:

- You can change the hospital logo by replacing hospital.png with your own image.
- You can manually edit or open patients.csv in Excel or any spreadsheet software.

Author: Harshal Patil
