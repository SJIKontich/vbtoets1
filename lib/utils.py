# python
import os
import pytest
import inspect
from io import StringIO
import sys
import json
from pathlib import Path
import getpass


def get_name_of_user():
    return getpass.getuser()

def check_function_exists(module, function_name):
    if not hasattr(module, function_name):
        pytest.fail(f"De functie '{function_name}' is niet gedefinieerd.")


def check_exact_match(module, function_name, args, expected_result):
    check_function_exists(module, function_name)
    function = getattr(module, function_name)
    result = function(*args)
    if result != expected_result:
        red = "\033[91m"
        reset = "\033[0m"
        print()
        print()
        print(f"{red}E        De functie '{function_name}{args}' geeft niet het verwachte resultaat.{reset}")
        print(f"{red}E        Verwacht: {expected_result}{reset}")
        print(f"{red}E        Gekregen: {result}{reset}")
        assert False

    # Als de test slaagt, log de voortgang
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename

def check_assertion(module, function_name, assertion_condition, error_message):
    check_function_exists(module, function_name)
    if not assertion_condition:
        red = "\033[91m"
        reset = "\033[0m"
        print()
        print()
        print(f"{red}E        {error_message}{reset}")
        assert False

    # Als de test slaagt, log de voortgang
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename

def check_approx_match(module, function_name, args, expected_result, tolerance=1e-6):
    check_function_exists(module, function_name)
    function = getattr(module, function_name)
    result = function(*args)
    if not (expected_result - tolerance <= result <= expected_result + tolerance):
        red = "\033[91m"
        reset = "\033[0m"
        print()
        print()
        print(f"{red}E        De functie '{function_name}' geeft niet het verwachte resultaat binnen de tolerantie.{reset}")
        print(f"{red}E        Verwacht: {expected_result} ± {tolerance}{reset}")
        print(f"{red}E        Gekregen: {result}{reset}")
        assert False

    # Als de test slaagt, log de voortgang
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename

# def run_student_code_and_compare():
#     # Get the file path of the calling test file
#     caller_frame = inspect.stack()[1]
#     test_file_path = caller_frame.filename
#
#     test_dir = os.path.dirname(test_file_path)
#     base_dir = os.path.dirname(test_dir)
#     vraag_file = os.path.join(base_dir, f"vraag{vraag_nummer:02}.py")
#     if not os.path.exists(vraag_file):
#         pytest.fail(f"Het bestand '{vraag_file}' bestaat niet.")
#
#     # Capture the student's output
#     output_capture = StringIO()
#     sys.stdout = output_capture
#
#     # Execute the entire student's code
#     student_file_path = vraag_file
#     with open(student_file_path, "r") as student_code:
#         code = student_code.read()
#         exec(code, globals())
#
#     sys.stdout = sys.__stdout__
#
#     # Verwachte output uit het .out-bestand lezen
#     output_file_path = os.path.join(test_dir, f"vraag{vraag_nummer:02}.out")
#     if not os.path.exists(output_file_path):
#         pytest.fail(f"Het bestand '{output_file_path}' met verwachte output bestaat niet.")
#
#     with open(output_file_path, "r") as output_file:
#         expected_output = output_file.read().strip()
#
#     # Prepare outputs for comparison
#     generated_output = output_capture.getvalue().strip()
#
#     # Assert with detailed output on failure
#     if generated_output != expected_output:
#         print("\n\n------- Verwacht -------\n\n" + expected_output)
#         print("\n------- Gekregen -------\n\n" + generated_output)
#         print("\n------- Verschil -------:\n")
#         for expected, actual in zip(expected_output.splitlines(), generated_output.splitlines()):
#             print(f"Verwacht: {expected}")
#             print(f"Gekregen:   {actual}")
#             print()
#         assert False, "De output komt niet overeen, zie hierboven voor details."

def extract_vraag(test_file_path):
    """Extract vraag number from the test file path."""
    path_parts = Path(test_file_path).parts
    try:
        test_file_name = path_parts[-1]
        if not test_file_name.startswith("test_vraag") or not test_file_name.endswith(".py"):
            pytest.fail(f"Ongeldig testbestand: '{test_file_name}'. Naam moet 'test_vraagYY.py' zijn.")
        vraag_nummer = int(test_file_name.replace("test_vraag", "").replace(".py", ""))
        return vraag_nummer
    except (IndexError, ValueError):
        pytest.fail(f"Kan vraagnummer niet bepalen uit pad: {test_file_path}")

def check_if_code_contains(snippet, snippetmessage):
    # Get the file path of the calling test file
    caller_frame = inspect.stack()[1]
    test_file_path = caller_frame.filename

    # Determine reeks and vraag_nummer from the file path
    vraag_nummer = extract_vraag(test_file_path)

    test_dir = os.path.dirname(test_file_path)
    base_dir = os.path.dirname(test_dir)
    vraag_file = os.path.join(base_dir, f"vraag{vraag_nummer:02}.py")
    if not os.path.exists(vraag_file):
        pytest.fail(f"Het bestand '{vraag_file}' bestaat niet.")

    # haal de source code van de student op, maar zonder commentaar uit het bestand vraag_file en steek het resultaat in de variabele source
    with open(vraag_file, "r") as student_code:
        source = student_code.read()
        source = "\n".join([line for line in source.splitlines() if not line.strip().startswith("#")])

    if snippet not in source:
        red = "\033[91m"
        reset = "\033[0m"
        print()
        print()
        print(f"{red}E        De code bevat geen {snippetmessage}.{reset}")
        assert False

