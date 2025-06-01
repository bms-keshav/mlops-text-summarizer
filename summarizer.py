import mlflow
from transformers import pipeline

# Load the summarization model (not logged as MLflow model, but track usage)
summarizer = pipeline("summarization", model="t5-small")

def generate_summary(text):
    with mlflow.start_run():
        # Track input text length
        mlflow.log_param("input_length", len(text))

        # Run the summarization pipeline
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
        summary_text = summary[0]['summary_text']

        # Track output summary length
        mlflow.log_metric("summary_length", len(summary_text))

        # Log the summary itself (just for reference)
        mlflow.log_text(summary_text, "summary.txt")

    return summary_text
