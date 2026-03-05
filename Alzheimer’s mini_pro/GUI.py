import tkinter as tk
from tkinter import filedialog
import pandas as pd
import pickle
from PIL import Image, ImageTk

# Load Model
with open("alzhemier_model.pkl", "rb") as f:
    model = pickle.load(f)

mri_path = ""

# Main Window
root = tk.Tk()
root.title("Alzheimer Detection System")
root.geometry("900x650")
root.config(bg="#E3F2FD")

# ================= TITLE =================
title = tk.Label(root,
                 text="Early Alzheimer Disease Detection System",
                 font=("Arial", 22, "bold"),
                 bg="#E3F2FD",
                 fg="#0D47A1")
title.pack(pady=10)

# ================= INPUT FRAME =================
input_frame = tk.LabelFrame(root,
                            text="Patient Details",
                            font=("Arial", 14, "bold"),
                            bg="#BBDEFB",
                            padx=10,
                            pady=10)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Age", bg="#BBDEFB").grid(row=0, column=0)
tk.Label(input_frame, text="Memory", bg="#BBDEFB").grid(row=1, column=0)
tk.Label(input_frame, text="Thinking", bg="#BBDEFB").grid(row=2, column=0)
tk.Label(input_frame, text="Decision", bg="#BBDEFB").grid(row=3, column=0)

age_entry = tk.Entry(input_frame)
memory_entry = tk.Entry(input_frame)
thinking_entry = tk.Entry(input_frame)
decision_entry = tk.Entry(input_frame)

age_entry.grid(row=0, column=1)
memory_entry.grid(row=1, column=1)
thinking_entry.grid(row=2, column=1)
decision_entry.grid(row=3, column=1)

# ================= MRI FRAME =================
image_frame = tk.LabelFrame(root,
                            text="MRI Scan",
                            font=("Arial", 14, "bold"),
                            bg="#E1BEE7",
                            padx=10,
                            pady=10)
image_frame.pack(pady=10)

image_label = tk.Label(image_frame, bg="#E1BEE7")
image_label.pack()

def upload_mri():
    global mri_path

    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if file_path:
        mri_path = file_path

        img = Image.open(file_path)
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)

        image_label.config(image=img)
        image_label.image = img

# ================= REPORT FRAME =================
report_frame = tk.LabelFrame(root,
                             text="Patient Report",
                             font=("Arial", 14, "bold"),
                             bg="white",
                             height=250)
report_frame.pack(pady=10, fill="x")

report_frame.pack_propagate(False)

report_text = tk.Text(report_frame,
                      height=10,
                      font=("Courier", 11),
                      wrap="word")

scrollbar = tk.Scrollbar(report_frame, command=report_text.yview)
report_text.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
report_text.pack(fill="both", expand=True)

# ================= PREDICT FUNCTION =================
def predict_patient():
    try:
        age = float(age_entry.get())
        memory = float(memory_entry.get())
        thinking = float(thinking_entry.get())
        decision = float(decision_entry.get())

        # MRI Processing
        if mri_path:
            img = Image.open(mri_path).convert("L")
            img = img.resize((50,50))
            pixels = list(img.getdata())
            mri_value = sum(pixels) / len(pixels)

            if mri_value > 120:
                mri_status = "Normal Brain Pattern"
            else:
                mri_status = "Possible Alzheimer Pattern"
        else:
            mri_status = "No MRI Uploaded"

        # Model Prediction
        data = [[age, memory, thinking, decision]]
        prediction = model.predict(data)[0]

        if prediction == 1:
            result = "Alzheimer Detected"
            risk = "HIGH"
            color = "red"
            advice = "Consult Neurologist"
        else:
            result = "Normal"
            risk = "LOW"
            color = "green"
            advice = "Healthy Lifestyle"

        report = f"""
================================
        PATIENT REPORT
================================

Age           : {age}
Memory Score  : {memory}
Thinking      : {thinking}
Decision      : {decision}

MRI Status    : {mri_status}

Risk Level    : {risk}
Prediction    : {result}

Recommendation:
{advice}

================================
"""

        report_text.delete(1.0, tk.END)
        report_text.insert(tk.END, report)
        report_text.tag_add("color", "1.0", "end")
        report_text.tag_config("color", foreground=color)

        # Save report
        with open("patient_report.txt", "w") as f:
            f.write(report)

    except:
        report_text.delete(1.0, tk.END)
        report_text.insert(tk.END, "Enter valid patient data")

# ================= DATASET FUNCTION =================
def upload_dataset():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )

    if file_path:
        df = pd.read_csv(file_path)

        X = df[['Age','Memory','Thinking','Decision']]
        predictions = model.predict(X)

        total = len(predictions)
        alz = sum(predictions)
        normal = total - alz

        report = f"""
================================
        DATASET REPORT
================================

Total Patients    : {total}
Alzheimer Cases   : {alz}
Normal Cases      : {normal}

================================
"""

        report_text.delete(1.0, tk.END)
        report_text.insert(tk.END, report)
        report_text.tag_add("color", "1.0", "end")
        report_text.tag_config("color", foreground="blue")

# ================= BUTTONS =================
button_frame = tk.Frame(root, bg="#E3F2FD")
button_frame.pack(side="bottom", pady=10)

tk.Button(button_frame,
          text="Upload MRI",
          bg="purple",
          fg="white",
          font=("Arial", 12),
          width=15,
          command=upload_mri).grid(row=0, column=0, padx=10)

tk.Button(button_frame,
          text="Predict Patient",
          bg="green",
          fg="white",
          font=("Arial", 12),
          width=15,
          command=predict_patient).grid(row=0, column=1, padx=10)

tk.Button(button_frame,
          text="Upload Dataset",
          bg="orange",
          fg="white",
          font=("Arial", 12),
          width=15,
          command=upload_dataset).grid(row=0, column=2, padx=10)

tk.Button(button_frame,
          text="Exit",
          bg="red",
          fg="white",
          font=("Arial", 12),
          width=15,
          command=root.quit).grid(row=0, column=3, padx=10)

root.mainloop()     
    