class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# Пример использования
with FileWriter('1.example.txt') as file:
    file.write("Hello, World!")