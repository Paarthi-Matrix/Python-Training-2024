class CSVIterator:
    def __init__(self, file_name):
        self.file = open(file_name, "r")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line
