from datetime import datetime

# Module 1: Log Ingestion
def ingest_logs(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Module 2: Pattern Recognition & Anomaly Detection
def detect_anomalies(logs):
    error_count = {}
    for line in logs:
        if "ERROR" in line:
            timestamp = line[1:20]
            minute = timestamp[:16]
            error_count[minute] = error_count.get(minute, 0) + 1

    anomalies = []
    for time, count in error_count.items():
        if count >= 3:
            severity = "High" if count >= 5 else "Medium"
            anomalies.append((time, count, severity))
    return anomalies

# Module 3: Alert Generation
def generate_alerts(anomalies):
    with open("alerts.txt", "w") as alert_file:
        for time, count, severity in anomalies:
            message = (f"ALERT: Incident predicted at {time}:00 | "
                       f"Errors: {count} | Severity: {severity}")
            print(message)
            alert_file.write(message + "\n")

# Main Runner
if __name__ == "__main__":
    logs = ingest_logs("logs.txt")
    anomaly_data = detect_anomalies(logs)
    generate_alerts(anomaly_data)
