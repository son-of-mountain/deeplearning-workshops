# Stock Price Prediction using PyTorch

## 📌 Project Overview
This project builds a deep learning model using PyTorch to predict stock closing prices based on historical data.

## 📊 Dataset
- Dataset: **New York Stock Exchange Prices**
- Features used: `open`, `high`, `low`, `volume`
- Target variable: `close`

## 🚀 Model Summary
- **Architecture:** 2 hidden layers (64 & 32 neurons)
- **Activation function:** ReLU
- **Loss function:** MSE Loss
- **Optimizer:** Adam (learning rate: 0.001)
- **Regularization:** Dropout (0.2), L2 weight decay

## 🔍 Results
| Metric | Value |
|--------|-------|
| Mean Absolute Error (MAE) | 58.6374 |
| Mean Squared Error (MSE) | 3443.5181 |
| Root Mean Squared Error (RMSE) | 58.6815 |

## 🔧 Improvements & Regularization
- **Tuned learning rate** (reduced from 0.01 → 0.001)
- **Added Dropout layers** to reduce overfitting
- **Applied L2 regularization** (weight decay)

## 🛠 How to Run
1. Clone this repository:
``git clone https://github.com/son-of-mountain/stock-price-prediction.git``
2. Open **Google Colab** and upload the dataset.
3. Run the notebook.

## 📢 What I Learned
- How to preprocess stock data for machine learning.
- How to build and optimize a **Deep Neural Network (DNN)** using PyTorch.
- How to apply **GridSearch, dropout, and L2 regularization** to improve model performance.
"""
