from file_manager import write_file, read_file

write_file('test.txt', 'Hola CI/CD')
print(read_file('test.txt'))
