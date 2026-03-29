# Vision2Text-AI-Powered-Image-Caption-Generator 🌐

## Table of Contents 📌 :

* [Project Overview](#project-overview)
* [Features](#features)
* [Architecture](#architecture)
* [System Capabilities](#system-capabilities)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Configuration](#configuration)
* [Usage](#usage)
* [Dataset](#dataset)
* [Learning Outcomes](#learning-outcomes)
* [Future Improvements](#future-improvements)
* [FAQ](#faq)
* [Acknowledgements](#acknowledgements)
* [Author](#author)
* [License](#license)
* [Changelog](#changelog)


## Project Overview 🚀 :

Vision2Text is an AI-powered image caption generator combining CNN (VGG16) and LSTM to generate meaningful descriptions from images. Trained on the Flickr8k dataset, it uses feature extraction, sequence modeling, and BLEU score evaluation to produce context-aware captions.

## Features ✨ :
- Automatic image caption generation
- CNN (VGG16) + LSTM based deep learning architecture
- Sequence-to-sequence learning for caption generation
- Top-K sampling for improved caption quality
- BLEU score evaluation for performance measurement
- Memory-efficient training using data generator
- Streamlit-based interactive web application
- Real-time image upload and caption generation
- End-to-end pipeline from data processing to deployment

## Architecture 🧠 :

```
Image → CNN (VGG16) → Feature Vector
       + Text Sequence → LSTM → Next Word Prediction
       → Repeat → Final Caption
```

## System Capabilities ⚙️ :

- Understands visual content from images
- Generates meaningful and context-aware captions
- Handles large datasets using generators
- Produces captions in real-time via UI

## Tech Stack 🛠️ :

- Python
- TensorFlow / Keras
- NumPy, Pandas
- Matplotlib
- NLTK
- Streamlit
- VGG16 (CNN)
- LSTM (RNN)

## Prerequisites 📋 :

Make sure you have:

- Python (>= 3.8)
- pip installed
- Basic understanding of Deep Learning

## Installation ⚙️ :

```
git clone https://github.com/msns-1927/Vision2Text.git
cd Vision2Text
pip install -r requirements.txt
```

## Configuration 🔧 :

Download required files:

- Dataset (Flickr8k)
- Model file (best_model.h5)
- Tokenizer (tokenizer.pkl)

Place them in the project root directory.

## Usage ▶️ :

Run the Streamlit app:

``` streamlit run vision2text_app.py ```

Steps:

- Upload an image
- Click "Generate Caption"
- View generated caption

## Dataset 📂 :
- Name: Flickr8k Dataset
- Source: Kaggle
- Link: https://www.kaggle.com/datasets/adityajn105/flickr8k
- 8,000 images
- 5 captions per image
