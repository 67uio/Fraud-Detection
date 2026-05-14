# Credit Risk Prediction - Fraud Detection

A machine learning application that predicts credit risk using an advanced XGBoost model, selected as the best performer after evaluating multiple machine learning algorithms on German credit data.

## 📋 Overview

This project predicts whether a credit application is **GOOD** (low risk) or **BAD** (high risk) based on applicant information. The model is deployed as an interactive web application using Streamlit, allowing users to input their credit details and receive instant risk predictions.

## 🎯 Features

- **XGBoost Classification Model**: High-performance gradient boosting classifier for credit risk prediction
- **Interactive Web App**: User-friendly Streamlit interface for making predictions
- **Feature Encoding**: Pre-trained label encoders for categorical variables (Sex, Housing, Saving accounts, Checking account)
- **Real-time Predictions**: Instant credit risk assessment based on user input

## 📊 Dataset

**Source**: German Credit Data (`raw data/german_credit_data.csv`)

The dataset contains applicant information including:
- **Age**: Applicant's age
- **Sex**: Gender (Male/Female)
- **Job**: Job classification (0-3)
- **Housing**: Housing situation (own, rent, free)
- **Saving accounts**: Savings level (little, moderate, rich, quite rich)
- **Checking account**: Checking account status (little, moderate, rich)
- **Credit amount**: Requested credit amount
- **Duration**: Loan duration in months

## 🏗️ Project Structure

```
Fraud Detection/
├── app/
│   └── app.py                    # Streamlit web application
├── encoders/                     # Pre-trained label encoders
│   ├── Sex_encoder.pkl
│   ├── Housing_encoder.pkl
│   ├── Saving accounts_encoder.pkl
│   └── Checking account_encoder.pkl
├── models/
│   └── Xgb_model.pkl            # Trained XGBoost model
├── notebooks/
│   └── analysis_model.ipynb      # Data analysis and model training
├── raw data/
│   └── german_credit_data.csv    # Source dataset
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. **Clone or download the project**
   ```bash
   cd "Fraud Detection"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install required packages**
   ```bash
   pip install numpy pandas matplotlib seaborn joblib scikit-learn xgboost streamlit
   ```

## 🚀 Usage

### 🌐 Live Deployment

Try the application online without any installation:
**[Credit Risk Prediction App - Live Demo](https://fraud-detection-br6cywc4gkafy9fwwyhgkg.streamlit.app/)**

### Running the Web Application Locally

Start the Streamlit app with:

```bash
streamlit run app/app.py
```

The application will open in your browser at `http://localhost:8501`

### Using the Prediction App

1. **Enter Applicant Information**:
   - Age (18-80)
   - Sex (Male/Female)
   - Job (0-3)
   - Housing status
   - Saving accounts level
   - Checking account status
   - Credit amount
   - Duration (months)

2. **Click "Predict Risk"** to get the credit risk assessment:
   - ✅ **GOOD**: Low credit risk (Predicted value = 1)
   - ❌ **BAD**: High credit risk (Predicted value = 0)

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| numpy | Numerical computing |
| pandas | Data manipulation |
| matplotlib | Visualization |
| seaborn | Statistical visualization |
| scikit-learn | Machine learning |
| xgboost | Gradient boosting classifier |
| joblib | Model and encoder serialization |
| streamlit | Web application framework |

See `requirements.txt` for specific versions.

## 🔍 Model Details

**Selected Model**: XGBoost (Extreme Gradient Boosting)

Multiple machine learning algorithms were evaluated during development, including Logistic Regression, Decision Trees, Random Forest, and Neural Networks. **XGBoost emerged as the best performer**, providing superior accuracy, better handling of mixed data types, and reduced overfitting through advanced regularization techniques.

- **Algorithm**: XGBoost (Extreme Gradient Boosting)
- **Type**: Binary Classification
- **Output**: 
  - 1 = Good (Low Risk)
  - 0 = Bad (High Risk)

## 📈 Analysis & Training

The model development and analysis can be found in `notebooks/analysis_model.ipynb`, which includes:
- Data exploration and visualization
- Feature engineering and encoding
- Model training and evaluation
- Performance metrics and analysis

## 🔐 Model & Encoder Files

Pre-trained model and encoders are stored as pickled files:
- `models/Xgb_model.pkl` - Trained XGBoost model
- `encoders/[feature]_encoder.pkl` - Label encoders for categorical features

**Note**: Ensure these files are in the correct directory paths as specified in `app/app.py`

## 💡 Tips for Best Results

- Keep applicant age between 18-80 years
- Ensure job classification is valid (0-3)
- Select appropriate values for categorical features
- Credit amount should be realistic and positive

## 📝 Notes

- The model predicts based on German credit standards
- Results are probabilistic predictions, not financial advice
- Always validate model predictions with domain experts
- Regular model retraining recommended as new data becomes available

## 👨‍💻 Development

To modify or improve the model:

1. Open `notebooks/analysis_model.ipynb`
2. Explore data and experiment with features
3. Retrain the model if needed
4. Update model and encoder pickle files
5. Test with the Streamlit app

## 📞 Support

For issues or improvements, refer to:
- Notebook analysis: `notebooks/analysis_model.ipynb`
- App code: `app/app.py`
- Dataset: `raw data/german_credit_data.csv`

---

**Last Updated**: May 2026  
**Status**: Production Ready
