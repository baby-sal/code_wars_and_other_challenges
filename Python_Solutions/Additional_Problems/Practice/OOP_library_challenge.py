from abc import abstractmethod, ABC

class LibraryItem(ABC):
    def __init__(self, title, author, publication_year, item_id):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.item_id = item_id

    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, genre, total_pages):
        super().__init__(title, author, publication_year, item_id)
        self.genre = genre
        self.total_pages = total_pages

    def display_info(self):
        return f"Name:{self.title}\nWritten by:{self.author}\nYear:{self.publication_year}\nid:{self.item_id}\ngenre:{self.genre}\ntotal_pages:{self.total_pages}"


class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, issue_number, publisher):
        super().__init__(title, author, publication_year,item_id)
        self.issue_number = issue_number
        self.publisher = publisher

    def display_info(self):
        return f"Name:{self.title}\nWritten by:{self.author}\nYear:{self.publication_year}\nid:{self.item_id}\nissue:{self.issue_number}\npublisher:{self.publisher}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print (f"Item with id: {item_id} successfully removed")
                return
        print("No such item here")

    def find_item_title(self, title):
        for item in self.items:
            if item.title.lower() == title.lower():
                item.display_info()
        else:
            print("Title not available")

    def display_all_items(self):
        if not self.items:
            print("The library is empty.")
        else:
            for item in self.items:
                item.display_info()

