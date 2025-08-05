"""
Deep Drift Detection using Evidently and Airflow
"""

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd

# Load reference and current datasets
ref = pd.read_csv("reference.csv")
cur = pd.read_csv("current.csv")

# Generate drift report
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref, current_data=cur)
report.save_html("drift_report.html")

print("Drift report generated and saved.")
