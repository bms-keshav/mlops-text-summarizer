import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from datetime import datetime
import os

# Sample paths – adjust these for your use
REFERENCE_FILE = "monitoring_data/reference.csv"
CURRENT_FILE = "monitoring_data/current.csv"
REPORT_DIR = "monitoring_reports"
os.makedirs(REPORT_DIR, exist_ok=True)

# Load reference and current data
reference_data = pd.read_csv(REFERENCE_FILE)
current_data = pd.read_csv(CURRENT_FILE)

# Create a data drift report
report = Report(metrics=[DataDriftPreset()])

report.run(reference_data=reference_data, current_data=current_data)

# Save HTML report
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_path = os.path.join(REPORT_DIR, f"data_drift_report_{timestamp}.html")
report.save_html(report_path)

print(f"✅ Drift report saved to: {report_path}")
