import sys
import time

def print_progress_bar(iteration, total, length=50):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = "=" * filled_length + "-" * (length - filled_length)
    sys.stdout.write(f"\r|{bar}| {percent}")
    sys.stdout.flush()

# Przykładowe użycie
total = 100
for i in range(total + 1):
    time.sleep(0.1)
    print_progress_bar(i, total)
