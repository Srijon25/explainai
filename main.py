import gradio as gr
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def explain(text, candidate_labels):
    labels = [label.strip() for label in candidate_labels.split(",")]
    result = classifier(text, labels)
    output = "\n".join([f"{label}: {score:.2f}" for label, score in zip(result["labels"], result["scores"])])
    return output
