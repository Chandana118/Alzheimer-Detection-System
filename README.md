🧠 Early Alzheimer Disease Detection System
📖 Overview

The Early Alzheimer Disease Detection System is an AI-powered healthcare application designed to assist in the early screening of Alzheimer’s disease using patient cognitive data and MRI brain scan analysis.

Early diagnosis of Alzheimer’s disease is critical for improving treatment outcomes and slowing disease progression. This project demonstrates how Machine Learning can support medical decision-making by predicting Alzheimer’s risk based on cognitive scores and basic MRI pattern analysis.

The system uses a Random Forest Machine Learning model trained on patient data such as:

Age

Memory score

Thinking ability

Decision-making ability

Users can also upload MRI brain scan images to analyze potential abnormal brain patterns. The application then generates a detailed patient report indicating risk level and recommendations.

✨ Features

✅ Predict Alzheimer’s disease using Machine Learning
✅ Upload and analyze MRI brain scan images
✅ Input patient cognitive scores for prediction
✅ Generate automatic patient diagnostic reports
✅ Analyze datasets containing multiple patient records
✅ Easy-to-use Graphical User Interface (GUI)

🧠 System Workflow
Patient Data + MRI Image
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
🛠 Technologies Used
Technology	Purpose
Python	Core programming language
Scikit-learn	Machine learning model
Random Forest	Classification algorithm
Tkinter	GUI development
Pandas	Data handling
Pillow	MRI image processing
📂 Project Structure
Alzheimer-Detection-System
│
├── GUI.py                # Main GUI application
├── train_model.py        # Machine learning training script
├── alzhemier_model.pkl   # Trained ML model
├── alzheimers_dataset.csv # Dataset used for prediction
├── patient_report.txt     # Generated patient report
├── README.md              # Project documentation
│
├── images
│   └── mri_sample.jpg     # Sample MRI image
│
└── outputs
    └── patient_report.txt
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/alzheimer-detection-system.git
2️⃣ Install required libraries
pip install pandas scikit-learn pillow
▶️ Running the Project
Step 1 – Train the Model
python train_model.py
Step 2 – Run the Application
python GUI.py
📊 Sample Output

The system generates a patient diagnostic report including:

Patient Age

Memory Score

Thinking Score

Decision Score

MRI Scan Status

Alzheimer Risk Level

Prediction Result

Medical Recommendation

Example report:

PATIENT REPORT

Age           : 77
Memory Score  : 4
Thinking      : 5
Decision      : 1

MRI Status    : Possible Alzheimer Pattern
Risk Level    : LOW
Prediction    : Normal

Recommendation:
Healthy Lifestyle
🎯 Applications

Early Alzheimer disease screening

Healthcare AI research projects

Medical decision support systems

Educational machine learning demonstrations

🔮 Future Improvements

Deep Learning based MRI analysis (CNN)

Larger medical dataset training

Web-based interface using Flask

Cloud deployment

Real-time hospital data integration

👨‍💻 Author

Chandana
B.Tech Student | AI & Machine Learning Projects
