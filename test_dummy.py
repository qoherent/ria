def test_dummy():
    assert True

# def test_another_dummy():
    # assert False, "This test intentionally fails"

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 == 2

def test_multiplication():
    assert 2 * 3 == 6

def test_division():
    assert 6 / 3 == 2

def test_strings():
    assert "hello" == "hello"

def test_lists():
    assert [1, 2, 3] == [1, 2, 3]

def test_dicts():
    assert {"key": "value"} == {"key": "value"}

def test_none():
    assert None is None