from typing import Protocol

class Printer(Protocol):
    def print_document(self, document: str) -> None:
        ...

class Scanner(Protocol):
    def scan_document(self, document: str) -> None:
        ...

class FaxMachine(Protocol):
    def fax_document(self, document: str) -> None:
        ...

class SimplePrinter:
    def print_document(self, document: str) -> None:
        print("Printing document.")

class Photocopier:
    def print_document(self, document: str) -> None:
        print("Printing document.")
    
    def scan_document(self, document: str) -> None:
        print("Scanning document.")

class MultiFunctionPrinter:
    def print_document(self, document: str) -> None:
        print("Printing document.")

    def scan_document(self, document: str) -> None:
        print("Scanning document.")

    def fax_document(self, document: str) -> None:
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
