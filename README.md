# SMS Spam Detector

A simple **SMS Spam Detection** project built using **Python**, **Natural Language Processing (NLP)** techniques, **NLTK**, **scikit-learn**, and **Streamlit**. The project employs a trained **TF-IDF vectorizer** combined with a **Logistic Regression** classifier to categorize text messages as **Spam** or **Not Spam**.

---

## Requirements

Ensure that **Python 3.9 or higher** is installed on your system.

Install the required dependencies using pip:

```bash
pip install streamlit nltk scikit-learn
```

---

## NLTK Setup

When the project is executed for the first time, NLTK will automatically download the necessary linguistic resources:

* punkt
* stopwords

No additional manual configuration is required.

---

## Running the Application

From the **project root directory**, execute the following command:

```bash
streamlit run frontend/app.py
```

This command will:

* Launch a local Streamlit server
* Open the SMS Spam Detector in the default web browser

---

## How It Works

1. The user enters an SMS message through the web interface.
2. The message undergoes Natural Language Processing (NLP) steps:
   * Conversion to lowercase
   * Tokenization of text into individual words
   * Removal of common English stopwords
   * Stemming using the Porter Stemmer to reduce words to their root form
3. The processed text is transformed into numerical feature vectors using **Term Frequency–Inverse Document Frequency (TF-IDF)**.
4. A trained **Logistic Regression** model analyzes the feature vectors to:
   * Classify the message as Spam or Not Spam
   * Produce a probability score indicating the likelihood of spam

---

## Why Logistic Regression

Logistic Regression is used in this project because it is:

* Well-suited for **binary classification** tasks such as spam detection
* Computationally efficient and performs well on high-dimensional sparse data produced by TF-IDF
* Interpretable, allowing probability-based decision making
* A widely accepted baseline algorithm for text classification problems

---

## Output

The application displays:

* Final classification result (SPAM or NOT SPAM)
* Spam probability percentage
* Regular message probability percentage

---

## Development Notes

* The trained model and TF-IDF vectorizer are loaded from the `backend/model/` directory
* Core preprocessing and prediction logic is implemented in `backend/main.py`
* The user interface is developed using **Streamlit** and located in `frontend/app.py`

---
