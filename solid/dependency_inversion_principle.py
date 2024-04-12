# This is a common violation of DIP


class DataFetcher:
    def fetch_data(self):
        # Imagine fetching data from a database
        return "Data from the database"

class ReportGenerator:
    def __init__(self):
        self.fetcher = DataFetcher()  # Direct dependency on a low-level module

    def create_report(self):
        data = self.fetcher.fetch_data()
        return f"Report with {data}"

# Usage
report_generator = ReportGenerator()
print(report_generator.create_report())
