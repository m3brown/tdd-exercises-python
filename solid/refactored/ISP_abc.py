from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass

class SimplePrinter(Printer):
    def print_document(self, document):
        print("Printing document.")

class Photocopier(Printer, Scanner):
    def print_document(self, document):
        print("Printing document.")
    
    def scan_document(self, document):
        print("Scanning document.")

class MultiFunctionPrinter(Printer, Scanner, FaxMachine):
    def print_document(self, document):
        print("Printing document.")

    def scan_document(self, document):
        print("Scanning document.")

    def fax_document(self, document):
        print("Faxing document.")

# Usage
simple_printer = SimplePrinter()
simple_printer.print_document("Sample Document")

photocopier = Photocopier()
photocopier.print_document("Sample Document")
photocopier.scan_document("Sample Document")

multi_function_printer = MultiFunctionPrinter()
multi_function_printer.print_document("Sample Document")
multi_function_printer.scan_document("Sample Document")
multi_function_printer.fax_document("Sample Document")
