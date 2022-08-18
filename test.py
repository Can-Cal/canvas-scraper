from handle_data import export_csv, split_digits, handle_data
from scraper import run
from create_json import create_json
from api import main

import os.path
import pytest

#@pytest.mark.skip("TODO")
def test_exists():
    assert export_csv
    assert handle_data
    assert split_digits
    assert run
    assert create_json
    assert main

#handle_data.py
def test_handle_data():
    #pass
    os.path.exists('current_graded_scores.csv')
    os.path.exists('not_grade_scores.csv')

#handle_data.py
def test_export_csv():
    os.path.exists('current_graded_scores.csv')
    os.path.exists('not_grade_scores.csv')

#create_json.py
def test_create_json():
    os.path.exists('events.json')

