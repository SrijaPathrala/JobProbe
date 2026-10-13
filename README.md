JobProbe — Recruitment Scam Detection

JobProbe is a Python-based recruitment scam detection prototype that analyzes job postings and identifies potential warning signs using rule-based checks and machine learning.

The project was developed as part of the Omnikon National Hackathon 2026. It aims to help users recognize suspicious recruitment messages before sharing personal information or responding to potentially fraudulent offers.

Problem Statement

Online job scams can mislead job seekers through unrealistic salary promises, urgent hiring messages, suspicious contact details, and requests for money or sensitive personal information.

JobProbe analyzes job posting text to highlight these warning signs and provide a risk score that helps users make more informed decisions.

Features

* Rule-Based Detection: Identifies suspicious patterns such as payment requests, unrealistic salary claims, urgency, suspicious email providers, shortened URLs, and requests for sensitive information.
* Machine Learning Classification: Uses TF-IDF text vectorization and Logistic Regression to classify job postings as potentially legitimate or suspicious.
* Risk Scoring: Combines rule-based indicators and machine learning output to generate an overall risk score.
* Risk Levels: Categorizes analyzed postings as Low, Medium, or High risk.
* Information Extraction: Extracts available email addresses, phone numbers, salary details, and URLs from the provided text.
* Recommendations: Displays warnings and suggestions to help users evaluate suspicious job postings.
* Web Interface: Provides a simple browser-based interface for submitting and analyzing job descriptions.

Tech Stack

Technology	Purpose
Python	Core application logic
FastAPI	Backend API
Scikit-learn	Machine learning model
TF-IDF	Text feature extraction
Logistic Regression	Text classification
Pandas	Dataset handling
HTML	Web page structure
CSS	User interface styling
JavaScript	Frontend and API communication
Git and GitHub	Version control and project management

How It Works

1. The user enters a job posting or recruitment message into the web interface.
2. The frontend sends the text to the FastAPI backend.
3. The information extraction module identifies available contact details, salary information, and URLs.
4. The rule-based detection module checks for predefined recruitment scam indicators.
5. The machine learning model analyzes the text using TF-IDF features and Logistic Regression.
6. The scoring module combines rule-based points with the model’s estimated scam probability.
7. The application displays the risk score, risk level, detected warning signs, extracted information, and recommendations.

Machine Learning Approach

JobProbe uses a text classification pipeline consisting of:

* TF-IDF Vectorization: Converts text into numerical features based on word importance.
* Logistic Regression: Uses the extracted text features to classify job postings.
* Training and Evaluation: The model is trained using labeled job posting examples, with a train-test split and accuracy evaluation.

The machine learning component works alongside the rule-based detection system. The rules identify explicitly defined warning signs, while the model looks for patterns learned from the training examples.

Project Structure

JobProbe/
├── backend/
│   ├── main.py
│   ├── extractor.py
│   ├── rules.py
│   └── scoring.py
├── frontend/
│   └── index.html
├── ml/
│   ├── dataset.csv
│   ├── train_model.py
│   └── predictor.py
├── tests/
│   └── .gitkeep
├── .gitignore
└── README.md

Getting Started

Prerequisites

* Python 3.10 or later
* Git
* A modern web browser

1. Clone the Repository

git clone https://github.com/SrijaPathrala/JobProbe.git
cd JobProbe

2. Create and Activate a Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install fastapi uvicorn scikit-learn pandas joblib

4. Start the Backend

Run the following command from the project root directory:

uvicorn backend.main:app --reload

The backend should be available at:

http://127.0.0.1:8000

The FastAPI interactive documentation can be accessed at:

http://127.0.0.1:8000/docs

5. Open the Frontend

Open frontend/index.html in your browser and enter a job posting to analyze it.

The frontend is configured to send requests to the local backend at http://127.0.0.1:8000/analyze.

Note: The frontend and backend must be configured correctly to communicate. If the browser blocks requests because of CORS restrictions, configure the appropriate CORS settings in the FastAPI application.

Model files: If the trained model and vectorizer files are not present, train the model using the project’s training script before running predictions. Ensure the script’s dataset and output paths are configured correctly for your environment.

Risk Score Interpretation

Risk Score	Risk Level
0–20	Low
21–50	Medium
51–100	High

The score represents the application’s assessment of potential warning signs. It is not a verified probability that a job posting is fraudulent.

Limitations

* The initial dataset is small and may not represent the variety of real-world recruitment scams.
* Model performance has not been established through extensive testing on independent real-world data.
* Rule-based checks may flag legitimate postings or miss sophisticated scams.
* Machine learning predictions depend on the examples used during training.
* A low risk score does not guarantee that a job posting is legitimate.

Users should independently verify employers, recruitment channels, and job offers before sharing sensitive information or making payments.

Future Improvements

* Expand the dataset with diverse and reliably labeled job postings.
* Evaluate the model using precision, recall, F1-score, and a confusion matrix.
* Add automated backend and model tests.
* Improve detection of contextual clues and previously unseen scam patterns.
* Strengthen input validation and frontend security.
* Improve model explainability and risk score calibration.
* Add deployment support and a more accessible user interface.

Author

Srija Pathrala

* GitHub: https://github.com/SrijaPathrala
* Project Repository: https://github.com/SrijaPathrala/JobProbe

Disclaimer

JobProbe is an educational prototype designed to demonstrate rule-based detection and machine learning for recruitment scam awareness. It is not a substitute for independent verification or professional fraud investigation.
