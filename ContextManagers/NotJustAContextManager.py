class DataIterator:
    # it implements context manager protocol and iterator protocol
    def __init__(self, fname):
        self._fname = fname
        self._f = None

    def __iter__(self):
        return self

    def __next__(self):
        row = next(self._f)
        return row.strip('\n').split(',')

    def __enter__(self):
        self._f = open(self._fname)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False
# DataIterator is not just a context manager is also an iterator
with DataIterator('text2.csv') as data: # it return an instance of DataIterator('text2.csv')
    for row in data:
        print(row)

data = DataIterator('text2.csv')
# for row in data:
#     print(row) # type error the file was not opened

with data as rows:
    for row in rows:
        print(row)