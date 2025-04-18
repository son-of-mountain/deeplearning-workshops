# 🔥 Deep Learning Lab 3 — RNN & Transformers for Arabic Text

### 📚 LSI — Université Abdelmalek Essaâdi  
**Course**: Deep Learning  
**Instructor**: Pr. ELAACHAK LOTFI  
**Lab**: 03 — Sequence Models and Transformer-based Text Generation

---

## 🧠 Objective

This lab focuses on building deep neural network architectures for **Natural Language Processing (NLP)** using **PyTorch**. The goal is to:
- Build a sequence model to classify Arabic texts by relevance score.
- Fine-tune a transformer (GPT-2) to generate Arabic text based on prompts.

---

## 📁 Project Structure

This project includes two main parts:

### Part 1: Text Classification with Sequence Models

We develop and train multiple RNN-based architectures:
- Vanilla RNN
- Bidirectional RNN
- GRU
- LSTM

on a custom dataset of Arabic texts, each labeled with a **relevance score** from "0" to "10".

---

## 🔧 Tools & Libraries Used

- "PyTorch" (model development and training)
- "sklearn" (dataset splitting and evaluation)
- "nltk" (BLEU score calculation)
- "numpy", "pandas" (data handling)
- "matplotlib" (optional for visualization)
- "transformers" (for GPT-2 model fine-tuning)
- "BeautifulSoup4" or "Scrapy" (for web scraping)

---

## 🛠️ Data Preparation

Arabic text data was collected from online sources using **web scraping** techniques. Each text was manually annotated with a score reflecting its relevance to the topic.

Preprocessing steps included:
- Tokenization
- Stop word removal
- Lemmatization / Stemming (using Arabic NLP tools)
- Discretization of score labels

The dataset was then converted into tensors to train the models.

---

## 🧪 Model Architectures & Training

### 🔁 RNN Architecture

"python
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])
        return out
"

Other models followed the same pattern, using "nn.GRU", "nn.LSTM", and bidirectional wrappers.

---

### ⚙️ Training Loop Summary

1. Inputs and labels converted to PyTorch tensors.
2. Model initialized with:
   - Loss function: "MSELoss"
   - Optimizer: "Adam"
3. Training loop included:
   - Forward pass
   - Loss computation
   - Backward pass
   - Parameter updates

---

## 📏 Evaluation

The models were evaluated using:
- Mean Squared Error (MSE)
- Accuracy on rounded scores
- **BLEU score** (for text similarity assessment)

"python
from nltk.translate.bleu_score import sentence_bleu
"

*Note: BLEU was more relevant for Part 2, but provides insights for generation quality.*

---

## ✨ Part 2: GPT-2 Text Generation

Using the HuggingFace "transformers" library, we:
1. Loaded the pre-trained GPT-2 model
2. Fine-tuned it on a small Arabic dataset (poems, news, etc.)
3. Prompted it with a sentence and generated continuation paragraphs

### GPT-2 Code Snippet

"python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

inputs = tokenizer("البداية كانت", return_tensors="pt")
outputs = model.generate(inputs["input_ids"], max_length=50)
print(tokenizer.decode(outputs[0]))
"

---

## 📌 Notes

- Each student was required to synthesize their learnings at the end.
- All code and results were pushed to GitHub.
- Google Colab was used for development and testing.

---

## 📚 Key Learnings

- Understanding and implementing sequential models like **RNN, GRU, and LSTM**
- Preprocessing Arabic text and building custom datasets
- Fine-tuning large **transformer models** like GPT-2
- Evaluating NLP models using both traditional and generation-specific metrics (BLEU)
- Building complete machine learning pipelines in **PyTorch**

---

## 🔗 Resources

- [HuggingFace Transformers Documentation](https://huggingface.co/transformers/)
- [PyTorch RNN Tutorial](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html)
- [BLEU Score Explanation](https://cloud.google.com/translate/automl/docs/evaluate)
- [Arabic NLP Tools](https://github.com/ARBML/awesome-arabic-nlp)

---

## 🧾 Author

🧑‍🎓 Student: _Mouaad ELHANSALI_  
🎓 LSI – Université Abdelmalek Essaâdi  
📅 April 2025

---
