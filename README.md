# Linux Log Analysis, Detection Automation & SIEM Visualization

## Project Overview

This project demonstrates a complete Security Operations Center (SOC) workflow for detecting suspicious authentication activity within Linux systems.

The project combines:

- Manual log analysis
- Python-based threat detection automation
- CSV reporting
- SIEM investigation using Splunk Enterprise
- Security visualization and threat analysis

The objective was to identify indicators of brute-force attacks, authentication failures, and unauthorized access attempts from Linux authentication logs.

---

## Project Architecture

```text
Linux Authentication Logs
            │
            ▼
 Manual Log Analysis
            │
            ▼
 Suspicious Events Identified
            │
            ▼
 Python Detection Script
            │
            ▼
 CSV Report Generation
            │
            ▼
 Splunk SIEM Ingestion
            │
            ▼
 Search & Investigation
            │
            ▼
 Visualization & Reporting
```

---

## Tools & Technologies

| Tool | Purpose |
|--------|---------|
| Linux Authentication Logs | Event Source |
| Python 3 | Detection Automation |
| VS Code | Development Environment |
| CSV Reporting | Data Export |
| Splunk Enterprise | SIEM Investigation |
| Excel | Findings Analysis |

---

## Skills Demonstrated

### Security Operations (SOC)

- Security Monitoring
- Threat Hunting
- Incident Investigation
- Log Analysis
- Event Correlation
- Security Reporting

### Detection Engineering

- Authentication Failure Detection
- Brute Force Detection
- Pattern Identification
- Security Automation

### SIEM

- Splunk Search Processing Language (SPL)
- Event Analysis
- Statistics Reporting
- Security Visualization

### Scripting

- Python Automation
- Data Processing
- CSV Export
- Pattern Matching

---

# Phase 1: Manual Threat Investigation

## Objective

Analyze Linux authentication logs to identify suspicious activity.

## Activities Performed

- Reviewed Linux authentication logs
- Investigated failed login attempts
- Identified invalid user activity
- Tracked repeated authentication failures
- Documented suspicious events

## Findings

Several suspicious authentication events were identified:

- Repeated login attempts against the root account
- Authentication failures originating from external IP addresses
- Invalid username enumeration attempts
- Evidence consistent with brute-force behavior

### Screenshot

![Manual Analysis](screenshots/manual-analysis.png)

---

# Phase 2: Detection Automation Using Python

## Objective

Automate the identification of suspicious authentication events.

## Detection Logic

The Python script was designed to detect:

- Failed Password Attempts
- Authentication Failures
- Invalid User Activity
- Unknown User Logins

## Key Features

- Reads Linux authentication logs
- Parses selected log ranges
- Flags suspicious entries
- Categorizes security events
- Exports findings to CSV

### Screenshot

![Python Script](screenshots/python-script.png)

### Detection Output

![Terminal Output](screenshots/terminal-output.png)

---

# Phase 3: Security Reporting

## Objective

Generate structured reports for easier investigation.

The detected security events were exported into CSV format for further analysis and reporting.

### Screenshot

![CSV Results](screenshots/csv-results.png)

---

# Phase 4: SIEM Investigation Using Splunk

## Objective

Validate findings using Splunk Enterprise and visualize attack patterns.

### Log Ingestion

Linux authentication logs were ingested into Splunk Enterprise for centralized analysis.

### SPL Query

```spl
source="Linux2k.log"
("Failed password" OR
"authentication failure" OR
"invalid user" OR
"user unknown")
```

### Security Events View

![Splunk Events](screenshots/splunk-events.png)

### Statistics Analysis

The Statistics View was used to:

- Group events by IP address
- Identify high-frequency attack sources
- Analyze targeted usernames
- Measure event volume

![Splunk Statistics](screenshots/splunk-statistics.png)

### Visualization

Authentication failures were visualized over time to identify attack spikes and brute-force behavior.

![Splunk Visualization](screenshots/splunk-visualization.png)

---

# Security Findings

## Finding 1: Brute Force Authentication Attempts

### Observation

Repeated authentication failures were observed against privileged accounts.

### Impact

Attackers may be attempting to gain unauthorized access through password guessing.

### Risk Level

High

### MITRE ATT&CK

T1110 – Brute Force

---

## Finding 2: Username Enumeration Activity

### Observation

Multiple invalid user login attempts were detected.

### Impact

Indicates reconnaissance activity to identify valid accounts.

### Risk Level

Medium

### MITRE ATT&CK

T1589 – Gather Victim Identity Information

---

## Finding 3: Privileged Account Targeting

### Observation

The root account was repeatedly targeted.

### Impact

Successful compromise would provide administrative access.

### Risk Level

High

### MITRE ATT&CK

T1078 – Valid Accounts

---

# MITRE ATT&CK Mapping

| Activity | ATT&CK Technique |
|------------|----------------|
| Failed Login Attempts | T1110 |
| Brute Force Attempts | T1110 |
| Invalid User Enumeration | T1589 |
| Root Account Targeting | T1078 |
| Authentication Abuse | T1078 |

---

# Project Outcomes

This project demonstrates the ability to:

- Analyze Linux authentication logs
- Identify suspicious security events
- Automate threat detection using Python
- Generate investigation reports
- Use Splunk for SIEM analysis
- Visualize attack patterns
- Produce actionable security findings

---

# Future Improvements

- Real-time log monitoring
- Automated alert generation
- Integration with Syslog servers
- Dashboard development in Splunk
- Threat intelligence enrichment
- Geo-IP analysis of source addresses

---

# Author

Ruchi

Cybersecurity Analyst | SOC Operations | Threat Detection | Security Monitoring

LinkedIn: YOUR_LINKEDIN_URL

GitHub: YOUR_GITHUB_URL
