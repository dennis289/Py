class Book:
    def __init__(self,title,author,publicationYear):
        self.title=title
        self.author=author
        self.publicationYear=publicationYear
    def display_info(self):
        pass
class Fiction(Book):
    def __init__(self,title,author,publicationYear,genre):
        super().__init__(title,author,publicationYear)
        self.genre=genre
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publicationYear}\nGenre: {self.genre}")
class NonFiction(Book):
    def __init__(self,title,author,publicationYear,topic):
        super().__init__(title,author,publicationYear)
        self.topic=topic
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publicationYear}\nTopic: {self.topic}")
# Test the classes
title= input("Enter the title of the book: ")
author= input("Enter the author of the book: ")
publicationYear= input("Enter the publication year of the book: ")
genre= input("Enter the genre of the book: ")
topic= input("Enter the topic of the book: ")
fiction= Fiction(title,author,publicationYear,genre)
nonfiction= NonFiction(title,author,publicationYear,topic)
fiction.display_info()
nonfiction.display_info()
# Output
# Enter the title of the book: The Alchemist    
# Enter the author of the book: Paulo Coelho
# Enter the publication year of the book: 1988
# Enter the genre of the book: Fiction
# Enter the topic of the book: Self-help
# Title: The Alchemist

        