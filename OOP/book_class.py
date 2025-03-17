class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when an instance is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for informal display"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation for recreating the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
