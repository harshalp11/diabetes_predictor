import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv", header=None)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = SVC(kernel="linear")
model.fit(X_scaled, y)

def predict():
    try:
        name = entry_name.get()
        features = [float(entry.get()) for entry in entries]
        input_scaled = scaler.transform([features])
        result = model.predict(input_scaled)[0]

        result_text = "Diabetic" if result == 1 else "Not Diabetic"
        messagebox.showinfo("Prediction Result", f"{name} is {result_text}")

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")

        record = [name] + features + [result_text, date_str, time_str]

        file_exists = os.path.exists("patients.csv")
        with open("patients.csv", "a") as f:
            if not file_exists:
                headers = ["Name", "Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Result", "Date", "Time"]
                f.write(",".join(headers) + "\n")
            f.write(",".join(map(str, record)) + "\n")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in all fields.")

app = tk.Tk()
app.title("Diabetes Predictor")
app.geometry("400x700")
app.configure(bg="white")

tk.Label(app, text="Patient Name", font=("Helvetica", 12), bg="white").pack()
entry_name = tk.Entry(app, font=("Helvetica", 12))
entry_name.pack(pady=5)

labels = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
entries = []

for label in labels:
    tk.Label(app, text=label, font=("Helvetica", 12), bg="white").pack()
    entry = tk.Entry(app, font=("Helvetica", 12))
    entry.pack(pady=5)
    entries.append(entry)

btn = tk.Button(app, text="Predict Diabetes", font=("Helvetica", 14), command=predict, bg="blue", fg="white")
btn.pack(pady=20)

app.mainloop()