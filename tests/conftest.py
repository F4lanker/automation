import pytest
@pytest.fixture(autouse=True)
def clean_text():
    with open('test_prodfile.txt', "w"):
        pass