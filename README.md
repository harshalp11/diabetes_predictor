# Diabetes Prediction & Hospital Patient Records App

This is a simple desktop hospital GUI application built with Python and Tkinter. It allows medical staff to:

- Predict if a patient is diabetic based on their medical attributes
- Automatically store patient records with date and time
- View all past predictions in a scrollable report

---

## Features

### 1. Diabetes Predictor
- Input: Glucose, Blood Pressure, Age, BMI, etc.
- Output: "Diabetic" or "Not Diabetic"
- Machine Learning: SVM (Support Vector Machine) trained on Pima Indians Diabetes dataset

### 2. Patient Record Viewer
- Stores name, prediction, input values, date, and time
- Data saved in `patients.csv`
- Viewable through a clean GUI

---

## File Structure

| File            | Description                                        |
|-----------------|----------------------------------------------------|
| `hospital_app.py` | Main dashboard with two buttons: Predictor and Records |
| `diabeties.py`    | Standalone diabetes prediction logic and GUI        |
| `patients.csv`    | Automatically created, stores patient history       |
| `requirements.txt`| List of Python libraries required to run the app    |
| `hospital.png`    | Optional hospital logo for branding in the GUI      |
| `ALGORITHMS.md`   | List of alternative ML models with code             |

---

## How to Run

### 1. Install Dependencies
Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
