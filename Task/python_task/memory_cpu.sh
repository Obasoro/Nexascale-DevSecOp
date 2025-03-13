```
import psutil
import time

# Set the interval for monitoring (in seconds)
interval = 5

# Set the log file
log_file = "cpu.log"

while True:
    # Get CPU usage
    cpu_usage = psutil.cpu_percent()

    # Get memory usage
    memory_usage = psutil.virtual_memory().percent

    # Print usage
    print(f"CPU Usage: {cpu_usage}% Memory Usage: {memory_usage}%")

    # Log usage to file
    with open(log_file, "a") as f:
        f.write(f"{time.time()}: CPU Usage: {cpu_usage}% Memory Usage: {memory_usage}%\n")

    # Wait for the interval
    time.sleep(interval)

    ```
