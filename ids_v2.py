import time
import re
from collections import defaultdict

LOG_FILE = "sample_auth.log"
THRESHOLD = 3  # عدد المحاولات اللي لو اتعدى يبقى خطر

failed_attempts = defaultdict(int)
blocked_ips = set()

def follow(file):
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

def extract_ip(line):
    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
    if match:
        return match.group(1)
    return None

with open(LOG_FILE, "r") as f:
    print("بدأ المراقبة الحية... (اضغط Ctrl+C للخروج)")
    for line in follow(f):
        if "Failed password" in line:
            ip = extract_ip(line)
            if ip and ip not in blocked_ips:
                failed_attempts[ip] += 1
                print(f"[ALERT] محاولة فاشلة من {ip} (عدد المحاولات: {failed_attempts[ip]})")

                if failed_attempts[ip] >= THRESHOLD:
                    print(f"[DANGER] تم رصد هجوم Brute Force محتمل من {ip} !!")
                    blocked_ips.add(ip)
