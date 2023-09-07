import os
import file_operations

def test_save_and_get_note():
    title = "test_save_get_note"
    key_hint = "hint"
    note = "This is a test note."

    file_operations.save_note_to_file(key_hint, note, title)
    retrieved_key_hint, retrieved_note = file_operations.get_note_from_file(title)

    assert key_hint == retrieved_key_hint
    assert note == retrieved_note

    file_operations.delete_file(title)

def test_get_titles():
    titles = file_operations.get_titles()
    assert isinstance(titles, list)

def test_delete_file():
    title = "test_delete_note"
    key_hint = "hint"
    note = "This is a test note."
    file_operations.save_note_to_file(key_hint, note, title)
    file_operations.delete_file(title)

    assert not os.path.exists(title + ".txt")

def test_backup_notes():
    title = "test_note_for_backup"
    key_hint = "hint"
    note = "This is a test note for backup."

    file_operations.save_note_to_file(key_hint, note, title)
    result = file_operations.backup_notes()

    assert result is True

    backup_files = os.listdir(file_operations.current_directory + "/secret_backup")
    assert title + ".txt" in backup_files

    os.remove(file_operations.current_directory + "/secret_backup/" + title + ".txt")
    file_operations.delete_file(title)

if __name__ == "__main__":
    test_save_and_get_note()
    test_get_titles()
    test_delete_file()
    test_backup_notes()

