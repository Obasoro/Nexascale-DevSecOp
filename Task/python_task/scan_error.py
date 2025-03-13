def count_errors_in_log(file_path):
    try:
        with open(file_path, "r") as file:
            log_lines = file.readlines()
        
        # Count occurrences of "ERROR"
        error_count = sum(1 for line in log_lines if "ERROR" in line)
        
        print(f"Found {error_count} occurrences of 'ERROR' in logs.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Replace 'sample.log' with the path to your .log file
log_file = "scan.log"
count_errors_in_log(log_file)
