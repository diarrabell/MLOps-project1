# Emotion Classifier

This project uses Github Actions to set up Continuous Integration. The main function is a command line tool that uses the [Emotion English DistilRoBERTa-base](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) model to perform sentiment analysis and classify text into of 7 different emotions: anger, disgust, fear, joy, neutral, sadness, and suprise.
To use this tool, input the chosen text and the tool will return the top predicted emotion.


## How to use:
- `make install` Install dependencies for project
- run `main.py --text "INSERT TEXT HERE"` to run project!

## References:
Jochen Hartmann, "Emotion English DistilRoBERTa-base". https://huggingface.co/j-hartmann/emotion-english-distilroberta-base/, 2022.

