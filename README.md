# Emotion Detection from Text

## Overview
Emotion Detection from Text is a Python project that leverages advanced Natural Language Processing (NLP) techniques to classify and detect the emotional tone present in a given sentence or paragraph. The system uses a pre-trained transformer-based model to analyze the textual input and outputs both the predicted emotion and confidence scores.

## Features
- Detects common emotions such as: anger, joy, sadness, fear, surprise, disgust, and neutral.
- Utilizes a robust state-of-the-art model from Hugging Face's Transformers library.
- Simple command-line interface for ease of use.

## Requirements
- Python 3.7 or above
- pip (Python package installer)

### Python Dependencies
- torch
- transformers

## Installation
1. Clone the repository or copy the source files to your working directory.

2. (Recommended) Create and activate a virtual environment:

bash
python -m venv emo-env
 On Windows
emo-env\Scripts\activate
 On macOS/Linux
 source emo-env/bin/activate

## Install the required packages:
BASH

pip install torch transformers
## Usage
Run the main script:

BASH

python detect_emotion.py
Input your text when prompted.

View the output, which displays the predicted emotion, confidence score, and scores for all supported emotions.

## Example:

Enter text: I am so excited for the concert!
Detected Emotion: joy (Confidence: 0.94)
All predictions:
- joy : 0.94
- surprise : 0.02
- neutral : 0.02
- others...


## Notes
Ensure your Python interpreter is using the correct virtual environment, especially if using an IDE like VS Code.
Large models may require an active internet connection on first run (models are downloaded from huggingface.co).
For issues with installing dependencies, see the troubleshooting section below.
Troubleshooting
ModuleNotFoundError:
Ensure you have activated your virtual environment and installed all dependencies inside it.

## Permission errors:
Try running your terminal or command prompt as an administrator.

## Model loading problems:
Verify your internet connection, and check that torch and transformers are installed properly.

## Credits
Pre-trained model: j-hartmann/emotion-english-distilroberta-base © Hugging Face

## License
This project is for educational and demonstration purposes.
