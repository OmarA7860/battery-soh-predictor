# 🔋 Battery Health Prediction & AI Assistant

An intelligent machine learning system that predicts lithium-ion battery **State of Health (SOH)** using real operational battery data and provides an AI-powered assistant for battery-related insights using the **Google Gemini API**.

---

## 📌 Overview

Battery degradation is a major challenge in:

- Electric Vehicles (EVs)
- Renewable Energy Storage
- Portable Electronics
- Sustainability & Recycling Systems

This project applies **Machine Learning** to analyze battery voltage measurements and operational data in order to predict battery health and classify batteries as healthy or unhealthy.

In addition, the system integrates a conversational AI assistant powered by **Google Gemini AI** for battery-related recommendations and educational support.

---

## 🚀 Features

✅ Battery SOH Prediction using Linear Regression  
✅ Automated preprocessing and data filtering  
✅ Multiple preprocessing strategy comparison  
✅ Battery health classification system  
✅ CSV report generation and visualization outputs  
✅ AI-powered chatbot using Google Gemini API  
✅ Configurable health threshold system  
✅ Modular and scalable Python architecture

---

## 🧠 Machine Learning Pipeline

The project workflow includes:

1. Data Loading from Excel dataset
2. Data Cleaning & Filtering
3. Feature Extraction
4. Train/Test Split
5. Linear Regression Model Training
6. SOH Prediction
7. Battery Classification
8. Metrics Evaluation
9. Visualization & Reporting

---

## 📊 Model Performance

The trained Linear Regression model achieved:

| Metric | Value |
|---|---|
| R² Score | 0.6561 |
| Mean Squared Error (MSE) | 0.001498 |
| Mean Absolute Error (MAE) | 0.030275 |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Development |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-Learn | Machine Learning |
| Matplotlib | Data Visualization |
| Google Gemini API | AI Chatbot Integration |
| VS Code | Development Environment |

---

## 📂 Project Structure

```bash
SOFE3370_LinearRegressionModel/
│
├── results/
│   ├── battery_classification.csv
│   ├── metrics.txt
│   ├── pred_vs_actual.png
│   └── preprocessing_comparison.csv
│
├── PulseBat Dataset.xlsx
├── train_linear_regression.py
├── train_linear_regression_preprocessing.py
├── battery_chatbot.py
├── requirements.txt
└── README.md
```

---

## 📈 Outputs Generated

The system automatically generates:

- Battery health prediction reports
- Classification CSV files
- Performance metrics
- Prediction visualizations
- Preprocessing comparison results

---

## 🤖 AI Chatbot Integration

The project integrates the **Google Gemini API** to provide an AI-powered battery assistant capable of answering questions such as:

- “How can battery lifespan be improved?”
- “Why is battery recycling important?”
- “What causes lithium-ion battery degradation?”

---

## ▶️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/battery-health-prediction.git
cd battery-health-prediction
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Train Linear Regression Model

```bash
python train_linear_regression.py
```

### Compare Preprocessing Strategies

```bash
python train_linear_regression_preprocessing.py
```

### Run Gemini AI Chatbot

```bash
python battery_chatbot.py
```

---

## 🔑 Gemini API Setup

1. Create an API key from Google AI Studio
2. Set your environment variable:

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### Mac/Linux

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

---

## 📚 Future Improvements

- Deep Learning Models
- Real-time Battery Monitoring
- Web Dashboard Integration
- Mobile Application Support
- IoT Sensor Connectivity
- Advanced Battery Analytics

---

## 👨‍💻 Authors

Developed as part of a Machine Learning and Software Engineering project focused on intelligent battery analytics and AI integration.

---

## 📄 License

This project is for educational and research purposes.
