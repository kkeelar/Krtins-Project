from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

try:
    summary = summarizer("Your test text here", max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    print(summary)
except Exception as e:
    print("Error:", e)
