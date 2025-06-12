
from src.math_operation import add,sub

def test_add():
    assert(2,3) == 5
    assert(-1,1) == 0


def test_sub():
    assert(5,3) == 2
    assert(2,2) == 0
    assert(-1,1) == -2

    
