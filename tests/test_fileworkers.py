from my_functions.file_workers import read_from_file

def create_data(test_data):
    with open ("test_prodfile.txt", "a") as f_o:
        f_o.writelines(test_data)
def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    create_data(test_data)
    assert test_data == read_from_file("test_prodfile.txt")