from transformers import pipeline

def detect_emotion(text):
    # Load emotion classification pipeline
    classifier = pipeline('text-classification', 
                          model='j-hartmann/emotion-english-distilroberta-base',
                          return_all_scores=True)
    
    # Get predictions
    result = classifier(text)[0]
    # Sort by score
    result = sorted(result, key=lambda x: x['score'], reverse=True)
    # Get top prediction
    top_emotion = result[0]
    
    print(f"Detected Emotion: {top_emotion['label']} (Confidence: {top_emotion['score']:.2f})")
    print("All predictions:")
    for emotion in result:
        print(f"- {emotion['label']} : {emotion['score']:.2f}")

if __name__ == "__main__":
    text = input("Enter text: ")
    detect_emotion(text)