from lesson_25 import *
import time


def test_search():
    window = get_python()
    elem2 = search_field(window)
    input_to(elem2, "python")
    time.sleep(1)
    element = found_results(window)
    assert "No results found" not in element.text


def test_hillel():
    window = get_hillel_test()
