import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import pandas as pd
from datetime import datetime

def open_predictor():
    subprocess.Popen(["python", "diabeties.py"])

def show_records():
    if not os.path.exists("patients.csv"):
        messagebox.showinfo("Info", "No records found yet.")
        return

    records_window = tk.Toplevel()
    records_window.title("Stored Patient Records")
    records_window.geometry("800x400")

    df = pd.read_csv("patients.csv")

    text = tk.Text(records_window, wrap="none")
    text.pack(fill="both", expand=True)

    header = "\t".join(df.columns) + "\n" + "-"*100 + "\n"
    text.insert("end", header)

    for index, row in df.iterrows():
        line = "\t".join(str(x) for x in row)
        text.insert("end", line + "\n")

    scroll_y = tk.Scrollbar(records_window, orient="vertical", command=text.yview)
    scroll_y.pack(side="right", fill="y")
    text.configure(yscrollcommand=scroll_y.set)

window = tk.Tk()
window.title("Hospital Dashboard")
window.geometry("500x300")
window.configure(bg="white")

try:
    from PIL import Image, ImageTk
    img = Image.open("hospital.png")
    img = img.resize((100, 100))
    img = ImageTk.PhotoImage(img)
    label_img = tk.Label(window, image=img, bg="white")
    label_img.pack(pady=10)
except:
    pass

title = tk.Label(window, text="Hospital App", font=("Helvetica", 20, "bold"), bg="white", fg="blue")
title.pack(pady=10)

predict_btn = tk.Button(window, text="Launch Diabetes Predictor", font=("Helvetica", 14), command=open_predictor, width=25)
predict_btn.pack(pady=10)

record_btn = tk.Button(window, text="View Patient Records", font=("Helvetica", 14), command=show_records, width=25)
record_btn.pack(pady=10)

window.mainloop()