from abc import ABC, abstractmethod


class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self):
        pass


class DatabaseFetcher(DataFetcher):
    def fetch_data(self):
        return "Data from the database"


class FileFetcher(DataFetcher):
    def fetch_data(self):
        return "Data from the file system"


class ReportGenerator:
    def __init__(self, fetcher: DataFetcher):
        self.fetcher = fetcher  # Dependency inversion using an abstract interface

    def create_report(self):
        data = self.fetcher.fetch_data()
        return f"Report with {data}"


# Usage
database_fetcher = DatabaseFetcher()
report_generator = ReportGenerator(fetcher=database_fetcher)
print(report_generator.create_report())
