🔋 Battery Health Prediction & AI Assistant

An intelligent battery analytics system that predicts lithium-ion battery health using Machine Learning and provides an AI-powered assistant for battery-related insights using the Gemini API.

Built with Python, Scikit-Learn, and Google Gemini AI.

🚀 Project Highlights
Developed a Machine Learning pipeline for predicting battery State of Health (SOH)
Implemented Linear Regression using Scikit-Learn
Compared multiple preprocessing strategies for performance evaluation
Generated automated metrics, visualizations, and CSV reports
Integrated Google Gemini API for an AI-powered battery assistant
Structured outputs for analytics and future scalability
🧠 Problem Statement

Battery degradation directly impacts:

Electric vehicles
Energy storage systems
Portable electronics
Sustainability and recycling initiatives

This project explores how Machine Learning can estimate battery health using voltage measurements and operational data.

The system predicts the State of Health (SOH) of lithium-ion batteries and classifies them based on configurable health thresholds.

⚙️ Tech Stack
Technology	Purpose
Python	Core development
Pandas	Data analysis
NumPy	Numerical operations
Scikit-Learn	Machine Learning
Matplotlib	Data visualization
Gemini API	AI chatbot integration
VS Code	Development environment
🏗️ System Architecture
Battery Dataset
       ↓
Data Filtering & Preprocessing
       ↓
Feature Extraction (Voltage Cells U1-U21)
       ↓
Linear Regression Model
       ↓
SOH Prediction
       ↓
Battery Classification
       ↓
Visualization & CSV Reports
       ↓
Gemini AI Chatbot Assistant
📊 Machine Learning Pipeline
Data Processing

The system:

Loads battery data from Excel
Filters operating conditions
Extracts voltage cell measurements
Splits data into training and testing sets
Model

The project uses:

Linear Regression

Implemented using:

sklearn.linear_model.LinearRegression

The model predicts:

Battery State of Health (SOH)

Using:

Voltage measurements from 21 battery cells
Evaluation Metrics

The model is evaluated using:

Metric	Description
R² Score	Prediction accuracy
MSE	Mean Squared Error
MAE	Mean Absolute Error
📈 Output & Analytics

The system automatically generates:

File	Purpose
metrics.txt	Model evaluation metrics
battery_classification.csv	Predicted battery conditions
pred_vs_actual.png	Visualization of predictions
preprocessing_comparison.csv	Comparison of preprocessing methods
🤖 AI Battery Assistant

The project integrates the Google Gemini API to provide an intelligent chatbot capable of answering battery-related questions.

Example Queries
“How can I improve battery lifespan?”
“Why is battery recycling important?”
“What causes lithium-ion batteries to degrade?”
“How does temperature affect battery health?”
📂 Project Structure
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
▶️ Getting Started
1️⃣ Clone the Repository
git clone <repository-url>
cd SOFE3370_LinearRegressionModel
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Environment
Windows PowerShell
.\venv\Scripts\Activate.ps1
4️⃣ Install Dependencies
pip install -r requirements.txt
🧪 Running the Machine Learning Model
python train_linear_regression.py

The program will:

Train the model
Predict battery SOH
Generate metrics
Save reports and visualizations
🔬 Running Preprocessing Comparisons
python train_linear_regression_preprocessing.py

This compares different preprocessing strategies to evaluate their impact on model performance.

💬 Running the AI Chatbot
Configure Gemini API Key
$env:GEMINI_API_KEY="YOUR_API_KEY"
Start Chatbot
python battery_chatbot.py
📌 Example Results
R² Score: 0.6561
MSE: 0.001498
MAE: 0.030275

The model successfully predicts battery SOH with relatively low prediction error.

🌱 Future Improvements

Potential future enhancements include:

Deep Learning models
Real-time battery monitoring
Web dashboard deployment
IoT integration
Expanded battery datasets
Advanced anomaly detection
🎯 Key Takeaways

This project demonstrates:

Applied Machine Learning workflows
Data preprocessing experimentation
Predictive analytics
AI API integration
Automation of analytical outputs
End-to-end Python development
👨‍💻 Author

Developed as part of advanced algorithm and Machine Learning exploration using Python and AI technologies.

📄 License

This project is intended for educational, research, and portfolio purposes.
