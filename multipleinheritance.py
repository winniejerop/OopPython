class OperatingSystem:
    multitasking = True
    name = "Mac Os"

class Apple:
    website = "www.apple.com"
    name = "Apple"


class MacBook(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more details".format(self.website))
            print("Name: " + self.name)


macBook = MacBook()
