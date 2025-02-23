import os
import csv
import json
import subprocess
from pathlib import Path

# Gewicht per testfunctie, bepaal zelf de waarden
TEST_WEIGHTS = {
}

def read_test_names_from_csv(csv_file):
    global TEST_WEIGHTS

    # Lees de testnamen uit het CSV-bestand
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Voeg de testnamen en de gewichten toe aan de globale TEST_WEIGHTS dictionary
        for row in reader:
            test_name = row[0]
            weight = int(row[1])  # Gewicht, altijd 1 voor de meeste tests

            # Voeg testnaam en gewicht toe aan de dictionary
            TEST_WEIGHTS[test_name] = weight

def run_pytest():
    """Voer pytest uit en retourneer de resultaten."""
    result = subprocess.run(
        ["pytest", "--tb=short", "--disable-warnings", "--json-report"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    report_path = Path(".report.json")
    if report_path.exists():
        with open(report_path, "r") as f:
            report = json.load(f)
            return report.get("tests", [])
    return []


def calculate_scores(tests):
    """Bereken scores op basis van de testresultaten."""
    scores = {test: 0 for test in TEST_WEIGHTS}
    total_score = 0
    max_score = sum(TEST_WEIGHTS.values())

    for test in tests:
        test_name = test["nodeid"]
        if test_name in TEST_WEIGHTS:
            if test["outcome"] == "passed":
                scores[test_name] += TEST_WEIGHTS[test_name]
                total_score += TEST_WEIGHTS[test_name]
            elif test["outcome"] == "failed":
                print(f"Fout in test {test_name}: Verwacht correct resultaat.")

    return scores, total_score, max_score


def display_scores(scores, total_score, max_score):
    """Toon de scores aan de student."""
    print("\nUw resultaten:")
    print("====================")
    for test_name, score in scores.items():
        print(f"{test_name}: {score} op {TEST_WEIGHTS[test_name]} punten")
    print("--------------------")
    print(f"Totaalscore: {total_score} op {max_score} punten")


def main():
    read_test_names_from_csv("testen.csv")
    tests = run_pytest()
    scores, total_score, max_score = calculate_scores(tests)
    display_scores(scores, total_score, max_score)


if __name__ == "__main__":
    main()
