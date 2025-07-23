class Comic:
    def __init__(
            self,
            id: str,
            title: str,
            isbn: str,
            image: str,
            extension: str,
            description: str
    ):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.image = image
        self.extension = extension
        self.description = description