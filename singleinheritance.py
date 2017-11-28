class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us log on to", self.contactWebsite)

class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("This Macbook was manufactured in {} by {}".format(self.yearOfManufacture, self.manufacturer))


macBook = MacBook()
macBook.manufactureDetails()
macBook.contactDetails()