# 🧠 Alzheimer Detection System

### AI-Based Early Screening Tool for Cognitive Disorders

🚀 The **Alzheimer Detection System** is an AI-powered healthcare application designed to assist in the **early screening of Alzheimer’s disease** using patient cognitive scores and MRI brain scan images.

This system combines **Machine Learning, medical data analysis, and image processing** to identify potential abnormal brain patterns and generate a **detailed patient diagnostic report**.

The goal of this project is to demonstrate how **Artificial Intelligence can support medical professionals in early diagnosis and decision-making.**

---

# 🌟 Key Features

🧠 **Machine Learning Prediction**
Predicts the likelihood of Alzheimer’s disease using a trained **Random Forest classifier**.

🖼 **MRI Brain Scan Analysis**
Users can upload MRI brain images to analyze potential abnormal brain patterns.

📊 **Cognitive Score Input**
Allows entry of patient cognitive test results including memory, thinking, and decision-making ability.

📄 **Automatic Patient Report Generation**
The system generates a **comprehensive patient diagnostic report** with prediction results and medical recommendations.

📁 **Dataset Analysis Support**
Works with structured patient datasets for training and prediction.

🖥 **User-Friendly GUI**
Built using **Tkinter** to provide a simple interface for doctors, students, and researchers.

---

# ⚙ System Workflow

```
Patient Cognitive Data + MRI Brain Scan
              │
              ▼
        Data Preprocessing
              │
              ▼
    Machine Learning Model
  (Random Forest Classifier)
              │
              ▼
          Prediction
              │
              ▼
     Patient Report Generation
```

---

# 🛠 Technologies Used

| Technology       | Purpose                                 |
| ---------------- | --------------------------------------- |
| 🐍 Python        | Core programming language               |
| 🤖 Scikit-learn  | Machine learning model development      |
| 🌳 Random Forest | Classification algorithm                |
| 🖥 Tkinter       | Graphical User Interface (GUI)          |
| 📊 Pandas        | Data preprocessing and dataset handling |
| 🖼 Pillow        | MRI image processing                    |

---

# 📂 Project Structure

```
Alzheimer-Detection-System
│
├── GUI.py                     # Main GUI application
├── train_model.py             # Machine learning training script
├── alzhemier_model.pkl        # Trained ML model
├── alzheimers_dataset.csv     # Dataset used for prediction
├── patient_report.txt         # Generated patient report
├── README.md                  # Project documentation
│
├── images
│   └── mri_sample.jpg         # Sample MRI brain image
│
└── outputs
    └── patient_report.txt     # Generated diagnostic report
```

---

# 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/alzheimer-detection-system.git
cd alzheimer-detection-system
```

---

### 2️⃣ Install Required Libraries

```
pip install pandas scikit-learn pillow
```

---

### 3️⃣ Train the Machine Learning Model

```
python train_model.py
```

This will generate the trained model file:

```
alzhemier_model.pkl
```

---

### 4️⃣ Launch the GUI Application

```
python GUI.py
```

The graphical interface will open where you can:

* Enter patient details
* Upload MRI brain scans
* Generate prediction reports

---

# 📊 Sample Patient Report

The system automatically generates a **diagnostic report** based on the input data.

Example output:

```
PATIENT REPORT

Age : 77
Memory Score : 4
Thinking Score : 5
Decision Score : 1

MRI Status : Possible Alzheimer Pattern
Risk Level : LOW
Prediction : Normal

Recommendation : Maintain a healthy lifestyle and regular cognitive monitoring.
```

---

# 🎯 Applications

🏥 **Early Alzheimer Disease Screening**
Helps identify potential risk at an early stage.

🧪 **Healthcare AI Research**
Useful for demonstrating machine learning applications in medical diagnosis.

💻 **Medical Decision Support Systems**
Can assist healthcare professionals in evaluating patient conditions.

🎓 **Educational Machine Learning Projects**
Great for students learning AI applications in healthcare.

---

# 🔮 Future Improvements

🧠 Deep Learning-based MRI analysis using **Convolutional Neural Networks (CNNs)**
📊 Training with **larger and real-world medical datasets**
🌐 Web-based interface using **Flask or Django**
☁ Cloud deployment for remote medical access
🏥 Integration with hospital medical record systems

---

# 👩‍💻 Author

**Chandana**

🎓 B.Tech Computer Science Student
🤖 Passionate about **Artificial Intelligence, Machine Learning, and Healthcare Innovation**

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
💡 Share feedback and suggestions

---

# 📜 License

This project is open-source and available under the **MIT License**.

