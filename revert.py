import csv
import sys
import time
from itertools import combinations

target_sum = int(sys.argv[2])
csv_file = sys.argv[1]

def calculate_combinations():
    numbers = []
    with open(csv_file, "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            name, number = row
            numbers.append((name, int(number)))

    print(f"Research {target_sum} on {csv_file}")
    attempt_count = 0
    occurrence_count = 0
    with open("results.txt", "w") as results_file:
        start_time = time.time()
        last_time = start_time
        for r in range(1, len(numbers) + 1):
            for combination in combinations(numbers, r):
                attempt_count += 1
                current_sum = sum(number for _, number in combination)
                if current_sum == target_sum:
                    occurrence_count += 1
                    result = ", ".join(f"{name} ({number})" for name, number in combination)
                    results_file.write(f"Result: {result}\n")

                current_time = time.time()
                if current_time - last_time >= 5:
                    elapsed_time = current_time - start_time
                    print(f"Running time: {elapsed_time:.0f} seconds", end="\r")
                    last_time = current_time

    end_time = time.time()
    running_time = end_time - start_time

    print("\n--- Calculation Completed ---")
    print(f"Running time: {running_time:.2f} seconds")
    print(f"Number of tries: {attempt_count}")
    print(f"Number of occurrences found: {occurrence_count}")

    time.sleep(2)

    print("\n--- Contents of results.txt ---")
    with open("results.txt", "r") as results_file:
        print(results_file.read())

calculate_combinations()
