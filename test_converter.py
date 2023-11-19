from converter import cm_to_inches

def test_positive_conversion():
    assert cm_to_inches(10) == 3.94

def test_negative_conversion():
    assert cm_to_inches(-10) == 10

def test_decimal_conversion():
    assert cm_to_inches(0.03) == 0.01