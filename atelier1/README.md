# Stock Price Prediction using PyTorch

## 📌 Regression Project Overview
This project builds a deep learning model using PyTorch to predict stock closing prices based on historical data.

### 📊 Dataset Exploration
- Dataset: **New York Stock Exchange Prices**
![image](https://github.com/user-attachments/assets/d05c0005-6020-49c6-91d9-92b3d22ab613)

- Features used: `open`, `high`, `low`, `volume`
- Target variable: `close`
  
![image](https://github.com/user-attachments/assets/1233d593-d3fa-4c34-b528-eb163d5db19f)

### Obtained result vs Actual model
![image](https://github.com/user-attachments/assets/2162c6f0-ec85-49d7-b6e6-9d6dde777bb0)


### 🚀 Model Summary
- **Architecture:** 2 hidden layers (64 & 32 neurons)
- **Activation function:** ReLU
- **Loss function:** MSE Loss
- **Optimizer:** Adam (learning rate: 0.001)
- **Regularization:** Dropout (0.2), L2 weight decay

### 🔍 Results
| Metric | Value |
|--------|-------|
| Mean Absolute Error (MAE) | 0.5513 |
| Mean Squared Error (MSE) | 0.5234 |
| Root Mean Squared Error (RMSE) | 0.7234 |

## 📌 Classification Part Overview
Class Distribution of Failure Types (Excluding No Failure)
![image](https://github.com/user-attachments/assets/75e4e415-a16c-469a-a7fb-d9448a6d149f)

Compute Classification Metrics
![image](https://github.com/user-attachments/assets/f20bae75-7636-4741-b34e-94ef424cdcc5)







## 🔧 Improvements & Regularization
- **Tuned learning rate** (reduced from 0.01 → 0.001)
- **Added Dropout layers** to reduce overfitting
- **Applied L2 regularization** (weight decay)

## 🛠 How to Run
1. Clone this repository:
``git clone https://github.com/son-of-mountain/deeplearning-workshops/blob/main/atelier1/``
2. Open **Google Colab** and upload the dataset.
3. Run the notebook.

## 📢 What I Learned
- How to preprocess stock data for machine learning.
- How to build and optimize a **Deep Neural Network (DNN)** using PyTorch.
- How to apply **GridSearch, dropout, and L2 regularization** to improve model performance.
"""
