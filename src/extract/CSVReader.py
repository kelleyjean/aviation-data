import csv

class CSVReader:
    def __init__(self, filename, delimiter=',', quotechar='"', encoding='utf-8'):
        self.filename = filename
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.encoding = encoding
        self.headers = []
        self.rows = []

    def read_csv(self):
        """Reads the CSV file and stores the data in headers and rows."""
        with open(self.filename, 'r', encoding=self.encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=self.delimiter, quotechar=self.quotechar)
            self.headers = next(reader)  # Store the first row as headers
            self.rows = list(reader)  # Store the remaining rows

    def get_headers(self):
        """Returns the list of headers (column names)."""
        return self.headers

    def get_rows(self):
        """Returns the list of data rows."""
        return self.rows