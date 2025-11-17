from exercises.read_from_file import read_text_from_file, read_lines_from_file

def test_read_text_from_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Line1\nLine2", encoding='utf-8')
    content = read_text_from_file(file_path)
    assert "Line1" in content

def test_read_lines_from_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("A\nB\nC", encoding='utf-8')
    lines = read_lines_from_file(file_path)
    assert lines == ["A", "B", "C"]
