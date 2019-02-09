# http://pythontesting.net/framework/pytest/pytest-introduction/#example

## ----------------------------------------------------------------------------
# How to run the test
# python -m pytest test_um_pytest.py
# py.test test_um_pytest.py
# py.test -v test_um_pytest.py  ## verbose output

from unnecessary_math import multiply

def test_numbers_3_4():
    assert multiply(3, 4) == 12
    
def test_string_a_3():
    assert multiply('a', 3) == 'aaa'
    