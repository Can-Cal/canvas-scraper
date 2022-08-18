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

@pytest.mark.skip("TODO")
def test_add():
    #add(1,2)
    actual = add(1,2)
    expected = 3
    assert expected == actual


#handle_data.py
def test_handle_data():
    #pass
    os.path.exists('current_graded_scores.csv')
    os.path.exists('not_grade_scores.csv')

#handle_data.py
def test_split_digits():
    pass


#handle_data.py
def test_export_csv():
    os.path.exists('current_graded_scores.csv')
    os.path.exists('not_grade_scores.csv')


#scraper.py
def test_run():
    pass


#create_json.py
def test_create_json():
    pass


#api.py
def test_main():
    pass