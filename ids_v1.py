import time

LOG_FILE = "sample_auth.log"

def follow(file):
    file.seek(0, 2)  # روح لآخر الملف مباشرة
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

with open(LOG_FILE, "r") as f:
    print("بدأ المراقبة الحية... (اضغط Ctrl+C للخروج)")
    for line in follow(f):
        if "Failed password" in line:
            print(f"[ALERT] {line.strip()}")


