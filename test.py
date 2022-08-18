from handle_data import export_csv, split_digits, add, handle_data
from scraper import run
from create_json import create_json
from api import main
import pytest

def test_exists():
    assert export_csv
    assert handle_data
    assert split_digits
    assert run
    assert create_json
    assert main

def test_add():
    #add(1,2)
    actual = add(1,2)
    expected = 3
    assert expected == actual

def test_handle_data():
    pass

def test_split_digits():
    pass

def test_export_csv():
    pass

def test_run():
    pass

def test_create_json():
    pass

def test_main():
    pass