import pytest 
from main import get_string_with, generate_data
def test_generate_data():
    r_string = get_string_with(5,65)
    assert len(r_string) == 5
    assert r_string == "AAAAA"

    r_string = get_string_with(3,66)
    assert len(r_string) == 3
    assert r_string == "bbb"

    offsets = ("4","5","3")
    data = generate_data(offsets,2)
    assert len(data) == 2
    assert len(data[0]) == len(offsets)
    assert len(data[1]) == len(offsets)
    assert data[0][0] == "AAAA"
    assert data[0][1] == "bbbbb"
    assert data[0][2] == "CCC"