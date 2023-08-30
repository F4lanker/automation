from my_functions.devision_feautre import div

import pytest
@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5), (20, 10 ,2), (3, 2, 1.5)])
def test_divisiton_positive(a, b, expected_result):
    assert div(a, b) == expected_result
@pytest.mark.parametrize("divisionable, devider, expected" ,[(10, 0, ZeroDivisionError),(2, "1",   TypeError)])
def test_zero_dev(divisionable, devider, expected):
    with pytest.raises(expected):
        assert div(divisionable, devider)
