import mlflow
from transformers import pipeline
import os

# Load the summarizer
summarizer = pipeline("summarization", model="t5-small")

def generate_summary(text):
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    summary_text = summary[0]['summary_text']

    # Optional logging (only if allowed)
    if os.getenv("MLFLOW_TRACKING_URI") and not os.getenv("IS_STREAMLIT_CLOUD"):
        with mlflow.start_run():
            mlflow.log_param("input_length", len(text))
            mlflow.log_metric("summary_length", len(summary_text))
            try:
                mlflow.log_text(summary_text, "summary.txt")
            except PermissionError:
                pass  # Skip if not permitted

    return summary_text
