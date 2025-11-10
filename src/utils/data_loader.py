from pathlib import Path
import json


def load_test_data(filename):
    file_path = Path(__file__).resolve().parent.parent / "data" / filename
    with open(file_path, "r") as f:
        return json.load(f)

