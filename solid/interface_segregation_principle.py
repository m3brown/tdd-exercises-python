# This is a common violation of ISP


class MultiFunctionDevice:
    def print_document(self, document):
        pass

    def scan_document(self, document):
        pass

    def fax_document(self, document):
        pass


class MultiFunctionPrinter(MultiFunctionDevice):
    def print_document(self, document):
        print("Printing document.")

    def scan_document(self, document):
        print("Scanning document.")

    def fax_document(self, document):
        print("Faxing document.")
