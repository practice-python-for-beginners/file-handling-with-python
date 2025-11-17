import os
from exercises.write_to_file import write_text_to_file

def test_write_text_to_file(tmp_path):
    file_path = tmp_path / "test.txt"
    content = "This is test content."
    result = write_text_to_file(file_path, content)

    assert result is True
    assert file_path.exists()
    assert file_path.read_text(encoding='utf-8') == content
