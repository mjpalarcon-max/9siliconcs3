class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if type(number_pages) is int and number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("The number of pages must be positive.")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if type(issue_number) is int and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

pub1 = Publication(
    "Beyond the Galaxy",
    "Ethan Siegel"
)
book1 = Book("They Both Die at the End", "Adam Silvera", 368 to 389)
mag1 = Magazine("National Geographic", "Various Authors", 202)
print("Publication Information:")
pub1.display_info()
print()
print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print("Number of pages:", book1.get_number_of_pages())
print()
print("\nMagazine Information:")
print("The issue number must be positive.")
mag1.display_info()
print("Issue number:", mag1.get_issue_number())
print()
