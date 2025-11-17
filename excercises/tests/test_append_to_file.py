from exercises.append_to_file import append_text_to_file

def test_append_text_to_file(tmp_path):
    file_path = tmp_path / "append.txt"
    file_path.write_text("Start", encoding='utf-8')
    append_text_to_file(file_path, "Added line")
    content = file_path.read_text(encoding='utf-8')
    assert "Added line" in content
