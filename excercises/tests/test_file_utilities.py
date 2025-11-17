from exercises.file_utilities import file_exists, get_file_size, delete_file

def test_file_utilities(tmp_path):
    temp_file = tmp_path / "temp.txt"
    temp_file.write_text("data", encoding='utf-8')

    assert file_exists(temp_file)
    assert get_file_size(temp_file) > 0

    delete_result = delete_file(temp_file)
    assert delete_result is True
    assert not file_exists(temp_file)
