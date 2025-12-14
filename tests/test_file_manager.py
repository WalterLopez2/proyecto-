from app.file_manager import write_file, read_file
import os

def test_write_and_read_file():
    filename = 'test_unit.txt'
    write_file(filename, 'Prueba CI/CD')
    content = read_file(filename)
    assert content == 'Prueba CI/CD'
    os.remove(filename)
