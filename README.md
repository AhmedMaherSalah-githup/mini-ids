# Mini IDS: Real-Time SSH Brute-Force Detector

A lightweight intrusion detection tool written in Python. It monitors an SSH
authentication log in real time, counts failed login attempts per IP address,
and flags IPs that exceed a threshold as potential brute-force attackers.

## Features
- Real-time log monitoring (tail-style, no restart needed)
- Regex-based IP extraction from log lines
- Per-IP failed-attempt counting with a configurable threshold
- Alert generation when a threshold is exceeded

## Project Structure
- `ids_v1.py`: live log monitoring (alerts on every failed attempt)
- `ids_v2.py`: adds per-IP counting and threshold-based detection
- `sample_auth.log`: sample log data (synthetic, for testing only)

## Usage
```bash
python3 -m venv venv
source venv/bin/activate
python3 ids_v2.py
```

Then, in another terminal, append test lines to `sample_auth.log` to simulate attempts.

## Sample Log Format
```
Sep 20 04:01:01 server sshd[1001]: Failed password for root from 203.0.113.9 port 6001 ssh2
```

## Disclaimer
This tool is for **educational purposes only**. Use it only on systems you own
or have explicit written permission to monitor. All IP addresses in the sample
log belong to reserved ranges (RFC 5737 documentation addresses and RFC 1918
private addresses).

## Skills Demonstrated
- Python: file I/O, generators, regular expressions, `defaultdict`
- Linux: log analysis, virtual environments
- Security: brute-force detection concepts, SOC-style alerting
