import csv
import os

LOG_FILE = "Linux_2k.log"
CSV_FILE = "suspicious_logs.csv"

if not os.path.exists(LOG_FILE):
    print("Error: Linux_2k.log not found.")
    print("Place Linux_2k.log in the same folder as log_analysis.py.")
    exit()

with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as file:
    logs = file.readlines()

subset_logs = logs[199:500]

suspicious_entries = []

for line in subset_logs:
    if "Failed password" in line:
        suspicious_entries.append(("Failed Login", line.strip()))
    elif "authentication failure" in line:
        suspicious_entries.append(("Authentication Failure", line.strip()))
    elif "user unknown" in line:
        suspicious_entries.append(("Unknown User", line.strip()))
    elif "invalid user" in line:
        suspicious_entries.append(("Invalid User", line.strip()))

print("")
print("=== Suspicious Log Entries: Lines 200-500 ===")
print("")

if len(suspicious_entries) > 0:
    for entry_type, entry in suspicious_entries:
        print("[" + entry_type + "] " + entry)
else:
    print("No suspicious entries found.")

print("")
print("Total suspicious entries found: " + str(len(suspicious_entries)))
print("")

with open(CSV_FILE, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Type", "Log Entry"])
    writer.writerows(suspicious_entries)

print("Results saved to: " + CSV_FILE)

