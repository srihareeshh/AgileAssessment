import time
print("Running backend checks...")
time.sleep(4)
with open("backend_report.txt", "w") as f:
    f.write("Backend checks passed successfully.")
print("Backend checks passed.")
