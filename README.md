# Fish-Predictor-app

# 🐟 Fish Species Predictor

## 📌 Problem Statement
The goal of this project is to **classify fish species** based on their physical measurements, such as **Weight, Length, Height, and Width**. The dataset consists of multiple species, and we use **Machine Learning (Logistic Regression)** to predict the species given the input features.

---

## 📊 Dataset & Features
The dataset contains measurements for different fish species. The input features include:

- **Weight**: Fish weight in grams
- **Length1**: Vertical length of the fish (cm)
- **Length2**: Diagonal length of the fish (cm)
- **Length3**: Cross length of the fish (cm)
- **Height**: Height of the fish (cm)
- **Width**: Diagonal width of the fish (cm)

The **target variable** is the **species** of the fish.

---

## 🤖 Machine Learning Model
- **Algorithm Used**: **Logistic Regression**
- **Preprocessing**:
  - **Feature Scaling**: Used `StandardScaler` to normalize the input data.
  - **Label Encoding**: Converted species names into numeric labels using `LabelEncoder`.
- **Accuracy**:
  - Train Accuracy: **92%**
  - Test Accuracy: **89%**
- **PSI (Population Stability Index)**:
  - PSI value: **0.06** (Low drift, indicating model stability across datasets).

---

## 🛠️ Flask API
This project uses a **Flask API** to serve the model predictions. The API takes user inputs as **JSON data**, processes it, and returns the predicted species.

### **📌 API Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/` | Loads the frontend UI |
| `POST` | `/predict` | Predicts fish species from input |

### **Request Example**:
```json
{
    "features": [240, 50, 49, 60, 11, 4]
}
Response Example:
{
    "species": "Pike"
}


Frontend (HTML + Bootstrap)
Built using: HTML, CSS, Bootstrap, and JavaScript.
User inputs fish measurements, and receives predicted species.
Bootstrap for responsive UI.
Fetch API used to connect frontend with Flask.


<img width="820" alt="image" src="https://github.com/user-attachments/assets/c7513e4e-5ae8-44fb-98ab-c6bd4dfdef54" />



Project Structure:

📂 fish_species_predictor
├── app.py                # Flask API backend
├── fish_species_logreg.pkl  # Trained Logistic Regression model
├── scaler.pkl            # StandardScaler for input normalization
├── label_encoder.pkl     # LabelEncoder for species mapping
├── templates
│   └── index.html        # Frontend UI
├── requirements.txt      # Dependencies
├── Procfile              # Heroku Deployment configuration
├── test_api.py           # API testing script
└── README.md             # Project documentation

Clone:
git clone https://github.com/SMJR-GH/fish-species-predictor.git
cd fish-species-predictor

create VE:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

 Install dependencies:
pip install -r requirements.txt
Flask
Flask-CORS
numpy
pandas
scikit-learn
gunicorn


Run the Flask server:
python app.py

Heroku Deployment

Install Heroku CLI:
npm install -g heroku
heroku login

heroku create fish-species-predictor

Testing API
python test_api.py

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [240, 50, 49, 60, 11, 4]}'



